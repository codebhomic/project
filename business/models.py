from django.db import models
from user.models import MyUser

# class StartupDetail(models.Model):
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='startups')
#     profilepic = models.ImageField(upload_to="media/startup/profilepics/",blank=True,null=True,default="image/useravatar.png")
#     startup_name = models.CharField(max_length=250)
#     founder_name = models.CharField(max_length=250)
#     bio = models.TextField(blank=False,null=False)
#     business_model = models.TextField(blank=False,null=False)
#     resume = models.FileField(upload_to="static/startup/", max_length=100)
#     additional_details = models.FileField(upload_to="static/startup/", max_length=100)