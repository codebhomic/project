from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from investor.models import investorDetail
from investor.forms import investorDetailForm
from django.contrib import messages

@login_required
def dashboard(request):
    if not request.user.is_investor:
        messages.error(request, "You cant access this page.")
        return redirect("/startup/dashboard/")
    uid = request.user.id
    data = investorDetail.objects.filter(user=uid).first() # checking if investor had entered his detail and created full profile to start investing
    if data is None:
        return redirect("/investor/profile/edit")
    return render(request,'investor/dashboard.html')

# edit profile and add profile to investor
@login_required
def editprofile(request):
    if not request.user.is_investor: 
        return redirect("/startup/dashboard/")
     # Try to get the existing startup detail for the user
    investordetail = investorDetail.objects.filter(user=request.user).first()
    
    if request.method == "POST":
        form = investorDetailForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            profilepic = form.cleaned_data['profilepic']
            investor_name = form.cleaned_data['investor_name']
            investor_experince = form.cleaned_data['investor_experince']
            investor_amount = form.cleaned_data['investor_amount']
            investor_detail =form.cleaned_data['investor_detail']
            resume = form.cleaned_data['resume']
            additional_details = form.cleaned_data['additional_details']
            if not investordetail:
                investorDetail.objects.create(
                    user=request.user,profilepic=profilepic,investor_name=investor_name,
                    investor_experince=investor_experince,investor_amount=investor_amount,
                    investor_detail=investor_detail,resume=resume,
                    additional_details=additional_details,
                )
                messages.info(request, "Profile details Added, after approving detils, you cant start investing.")
            else:
                investorDetail.objects.update(
                    user=request.user,profilepic=profilepic,investor_name=investor_name,
                    investor_experince=investor_experince,investor_amount=investor_amount,
                    investor_detail=investor_detail,resume=resume,
                    additional_details=additional_details,
                )
                messages.success(request, "Profile details updated.")
            
            return redirect("/investor/dashboard/")
    else:
        form = investorDetailForm(instance=investordetail)

    context = {
        'form': form,
        'page_title': "Add Investor Detail" if investordetail is None else "Edit Investor Detail"
    }
    return render(request,'investor/editprofile.html', context)
