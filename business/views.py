# including modules to be used in function 
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from business.models import StartupDetail
from business.forms import StartupDetailForm
from django.contrib import messages

# dashboard page
@login_required
def dashboard(request):
    context={} # context to be passed in templates to be used in projects
    if request.user.is_investor: # checking if user is investor then redirecting to investor dashboard
        messages.error(request, "You cant access this page.")
        return redirect("/investor/dashboard/")
    data = StartupDetail.objects.filter(user=request.user).first() # checking if user had entered his detail
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
    
    # Try to get the existing startup detail for the user
    startup_detail = StartupDetail.objects.filter(user=request.user).first()
    
    if request.method == "POST":
        form = StartupDetailForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            profilepic = form.cleaned_data['profilepic']
            startup_name = form.cleaned_data['startup_name']
            founder_name = form.cleaned_data['founder_name']
            founder_detail = form.cleaned_data['founder_detail']
            co_founders = form.cleaned_data['co_founders']
            co_founders_details = form.cleaned_data['co_founders_details']
            team = form.cleaned_data['team']
            team_details = form.cleaned_data['team_details']
            business_model = form.cleaned_data['business_model']
            resume = form.cleaned_data['resume']
            additional_details = form.cleaned_data['additional_details']
            if not startup_detail:
                datasaved = StartupDetail.objects.create(
                    user=request.user,profilepic=profilepic,startup_name=startup_name,
                    founder_name=founder_name,founder_detail=founder_detail,
                    co_founders=co_founders,co_founders_details=co_founders_details,team=team,
                    team_details=team_details,business_model=business_model,resume=resume,
                    additional_details=additional_details,
                )
                datasaved.save()
            else:
                datasaved = StartupDetail.objects.update(user=request.user,profilepic=profilepic,startup_name=startup_name,
                founder_name=founder_name,founder_detail=founder_detail,co_founders=co_founders,
                co_founders_details=co_founders_details,team=team,team_details=team_details,business_model=business_model,
                resume=resume,additional_details=additional_details,
                )
                datasaved.save()
            return redirect("/startup/dashboard/")
    else:
        form = StartupDetailForm(instance=startup_detail)

    context = {
        'form': form,
        'page_title': "Add Startup Detail" if startup_detail is None else "Edit Startup Detail"
    }
    return render(request, "startup/editprofile.html", context)

@login_required
def settings(request):
    context={}
    return render(request,"dashboard.html",context)

