from django import forms
from user.models import MyUser
from business.models import StartupDetail,Pitch

class StartupDetailForm(forms.ModelForm):
   
   class Meta:
        model = StartupDetail
        fields = (
            'profilepic','startup_name','founder_name','founder_detail',
            'co_founders','co_founders_details','team','team_details',
            'business_model','resume','additional_details',
        )
        help_texts = {
            'profilepic':'Profile Pic For Startup',
            'startup_name':'Enter Your Startup Name',
            'founder_name':'Enter Founder Name of startup',
            'founder_detail':'Enter Founders Details',
            'co_founders':'Do Your Startup Have Co Founders?? tick if you have',
            'co_founders_details':'Enter Co founders details',
            'team':'Do You Have team??',
            'team_details':'Enter your teams details',
            'business_model':'What is Your Business Model Explain',
            'resume':'Add Startup Resume if want to...',
            'additional_details':'Add a file in which your additional details about your startup is mentioned',

        }

class PitchForm(forms.ModelForm):
    
    class Meta:
        model = Pitch
