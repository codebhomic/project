from django import forms
from user.models import MyUser
from investor.models import investorDetail

class investorDetailForm(forms.ModelForm):
   
   class Meta:
        model = investorDetail
        fields = (
            "profilepic","investor_name","investor_experince","investor_amount","investor_detail","resume","additional_details"
         )
        help_texts = {
            "profilepic":"",
            "investor_name":"",
            "investor_amount":"",
            "investor_experince":"",
            "investor_detail":"",
            "resume":"",
            "additional_details":""
        }

# class PitchForm(forms.ModelForm):
    
#     class Meta:
#         model = Pitch
