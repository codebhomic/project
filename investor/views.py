from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if not request.user.is_investor:
        return redirect("/startup/dashboard/")
    return render(request,'investordashboard.html')