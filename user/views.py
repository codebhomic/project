from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from user.models import MyUser
from user.forms import UserRegistrationForm

def register(request):
    return render(request, 'user/investororentreprenaur.html')

def startup_register(request):
    context = {"register":"Registration For Startup"}
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_startup')
    else:
        form = UserRegistrationForm()
    context['form'] = form
    return render(request, 'users/registerpage.html',context=context)
    
def investor_register(request):
    context = {"register":"Registration For Investor"}
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_investor = True  # Set the is_investor field
            form.save()
            return redirect('dashboard_investor')
    else:
        form = UserRegistrationForm()
    context['form'] = form
    # return render(request, 'users/createaccinvestor.html')
    return render(request, 'users/registerpage.html',context=context)

def home(request):
    return render(request,'user/landingpage.html')

def login(request):
    return render(request,'base.html')

def logout(request):
    return render(request,'base.html')
