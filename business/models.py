from django.db import models
from user.models import MyUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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
                'team_details': 'This field is required when you said you have team.'
            })
        # Ensure that co_founders_details having text then co_founders must be true
        if not self.co_founders and self.co_founders_details:
            raise ValidationError({
                'co_founders': 'This field is required to be True or checked'
            })
        if not self.team and self.team_details:
            raise ValidationError({
                'team': 'This field is required to be True or checked'
            })

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method before saving the object
        super().save(*args, **kwargs)

class Pitch(models.Model):
    startup = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='pitches')
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)  # Adjusted decimal places
    equity_offer = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)  # Smaller precision for equity
    date_posted = models.DateTimeField(auto_now_add=True)  # Only use auto_now_add
    # Use TextChoices for status
    class Status(models.TextChoices):
        OPEN = 'open', _('Open')
        CLOSED = 'closed', _('Closed')
        FUNDED = 'funded', _('Funded')
        REJECTED = 'rejected', _('Rejected')

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.OPEN,
    )

    def __str__(self):
        return self.title
