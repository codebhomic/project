from django.contrib.auth import get_user_model, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from user.models import MyUser
from user.forms import UserRegistrationForm,LoginForm
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from user.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from user.utils import send_activation_email

def activate(request, uidb64, token, user_type):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('/auth/login/'+user_type)  # Redirect to login page after successful activation
    else:
        return render(request, 'account_activation_invalid.html')


def register(request):
    return render(request, 'user/investororentreprenaur.html')

def startup_register(request):
    context = {"register":"Registration For Startup"}
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_activation_email(user,"startup", request)
            return redirect('/auth/activation_sent/')
    else:
        form = UserRegistrationForm()
    context['form'] = form
    context['user_type'] = "startup"
    return render(request, 'users/registerpage.html',context=context)
    
def investor_register(request):
    context = {"register":"Registration For Investor"}
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_investor = True
            user = form.save()
            send_activation_email(user,"investor", request)
            return redirect('/auth/activation_sent/')
    else:
        form = UserRegistrationForm()
    context['form'] = form
    context['user_type'] = "investor"
    return render(request, 'users/registerpage.html',context=context)

def home(request):
    return render(request,'user/landingpage.html')

def activation_sent(request):
    return render(request,'users/activation_sent.html')

def userlogin(request):
    if not request.user.is_anonymous:
        return redirect("/startup/dashboard/")
    form = LoginForm()
    context = {}
    context['register'] = "Login for investor" if "Login for investor" in request.build_absolute_uri().split('/') else "Login for startup"
    if request.method == 'POST':
        form = LoginForm(request.POST, request=request)
        if form.is_valid():
            user = form.cleaned_data['user']  # Assuming you've stored the user in cleaned_data
            login(request,user)
            if user.is_investor:
                return redirect("dashboard_investor")
            return redirect("dashboard_startup")
    context['form']= form
    return render(request, 'users/login.html', context=context)

def userlogout(request):
    logout(request=request)
    return redirect("dashboard_investor")
