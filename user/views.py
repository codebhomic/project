from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages

# class CustomLoginView(LoginView):
#     template_name = 'users/login.html'
#     authentication_form = UserLoginForm

# class CustomLogoutView(LogoutView):
#     template_name = 'users/logout.html'

def register(request):
    return render(request, 'user/investororentreprenaur.html')
    # return render(request, 'users/register.html')

def startup_register(request):
    return render(request, 'users/createentra.html')

def investor_register(request):
    return render(request, 'users/createaccinvestor.html')

def home(request):
    return render(request,'user/landingpage.html')

def login(request):
    return render(request,'base.html')

def logout(request):
    return render(request,'base.html')
