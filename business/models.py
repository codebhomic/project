from django.db import models
from user.models import MyUser
from django.core.exceptions import ValidationError

class StartupDetail(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to="startup/profilepics/",blank=True,null=True,default="startup/profilepics/useravatar.png")
    startup_name = models.CharField(max_length=250)
    startup_detail = models.TextField(blank=False,null=False)
    founder_name = models.CharField(max_length=250)
    founder_detail = models.TextField()
    co_founders = models.BooleanField(default=False)
    co_founders_details = models.TextField(blank=True, null=True)
    team = models.BooleanField(default=False)
    team_details = models.TextField(blank=True, null=True)
    business_model = models.TextField(blank=False,null=False)
    resume = models.FileField(upload_to="static/startup/", max_length=100,blank=True,null=True)
    additional_details = models.FileField(upload_to="static/startup/", max_length=100,blank=True,null=True)

    def clean(self):
        # Ensure that co_founders_details is required when co_founders is True
        if self.co_founders and not self.co_founders_details:
            raise ValidationError({
                'co_founders_details': 'This field is required when you said you have co founder.'
            })
        if self.team and not self.team_details:
            raise ValidationError({
                'co_founders_details': 'This field is required when you said you have team.'
            })

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method before saving the object
        super().save(*args, **kwargs)