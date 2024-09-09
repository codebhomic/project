from django.db import models
from user.models import MyUser
from django.core.exceptions import ValidationError

class investorDetail(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to="investor/profilepics/",blank=True,null=True,default="useravatar.png")
    investor_name = models.CharField(max_length=250)
    investor_experince = models.CharField(max_length=250,blank=False,null=False)
    investor_amount = models.CharField(max_length=250,blank=False,null=False)
    investor_detail = models.TextField(blank=False,null=False)
    resume = models.FileField(upload_to="static/startup/", max_length=100,blank=True,null=True)
    additional_details = models.FileField(upload_to="static/startup/", max_length=100,blank=True,null=True)
    is_approved = models.BooleanField(default=False)

    def clean(self):
        # Ensure that co_founders_details is required when co_founders is True
        pass

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method before saving the object
        super().save(*args, **kwargs)