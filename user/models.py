# from django.db import models

# # class SocialMediaAccount(models.Model):
# #     PLATFORM_CHOICES = [
# #         ('facebook', 'Facebook'),
# #         ('twitter', 'Twitter'),
# #         ('linkedin', 'LinkedIn'),
# #         ('instagram', 'Instagram'),
# #         # Add other platforms as needed
# #     ]
# #     user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='social_media_accounts')
# #     platform = models.CharField(max_length=30, choices=PLATFORM_CHOICES)
# #     url = models.URLField(max_length=200)

# #     def __str__(self):
# #         return f"{self.platform}: {self.url}"

# # class AdditionalDetails(models.Model):
# #     user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='additional_details')
# #     details = models.TextField()

# #     def __str__(self):
# #         return self.details[:50]  # Return a snippet of the details for readability

# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     resume = models.FileField(upload_to='resumes/')
#     profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)

#     class Meta:
#         abstract = True

# class Investor(User):
#     # Additional fields for Investor can be added here
#     pass

# class Startup(User):
#     business_idea = models.TextField(blank=True, null=True)
#     startup_name = models.CharField(max_length=100, blank=True, null=True)
#     # Additional fields for Startup can be added here
#     pass
