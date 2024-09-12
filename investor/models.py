from django.db import models
from user.models import MyUser
from django.core.exceptions import ValidationError
from business.models import Pitch
from django.utils.translation import gettext_lazy as _

class investorDetail(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to="investor/profilepics/", blank=True, null=True, default="investor/profilepics/useravatar.png")
    investor_name = models.CharField(max_length=250)
    investor_experince = models.CharField(max_length=250)
    investor_amount = models.DecimalField(max_digits=12, decimal_places=2)  # If it's a number
    investor_detail = models.TextField()
    resume = models.FileField(upload_to="investor/resume/", max_length=150, blank=True, null=True)
    additional_details = models.FileField(upload_to="investor/additional_details/", max_length=150, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def clean(self):
        # Ensure that co_founders_details is required when co_founders is True
        pass

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method before saving the object
        super().save(*args, **kwargs)


class Investment(models.Model):
    investor = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='investments')
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE, related_name='investments')
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)  # Adjusted decimal places
    equity_required = models.DecimalField(max_digits=5, decimal_places=2)  # Smaller precision for equity
    date_invested = models.DateTimeField(auto_now_add=True)  # Only use auto_now_add

    def __str__(self):
        return f"{self.investor} invested in {self.pitch}"
