from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.is_investor:
        return redirect("/investor/dashboard/")
    return render(request,'startup/dashboard.html')