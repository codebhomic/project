from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from business.models import StartupDetail
from business.forms import StartupDetailForm

@login_required
def dashboard(request):
    context={}
    if request.user.is_investor:
        return redirect("/investor/dashboard/")
    data = StartupDetail.objects.filter(user=request.user).first()
    if data is None:
        return redirect("/startup/editprofile/")
    return render(request,'startup/dashboard.html',context)

@login_required
def profile(request):
    context={}
    if request.user.is_investor:
        return redirect("/investor/dashboard/")
    return render(request,"startup/editprofile.html",context)

@login_required
def editprofile(request):
    if request.user.is_investor:
        return redirect("/investor/dashboard/")
    context={}
    form = StartupDetailForm()
    if request.method == "POST":
        form = StartupDetailForm(request.POST)
        if form.is_valid():
            return HttpResponse("form is valid")
        
    context['form'] = form
    data = StartupDetail.objects.filter(user=request.user).first()
    context['page_title'] = "Add Startup Detail" if data is None else "Edit Startup Detail"
    return render(request,"startup/editprofile.html",context)

@login_required
def settings(request):
    context={}
    return render(request,"dashboard.html",context)

