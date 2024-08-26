from django.urls import path
from business.views import (
    dashboard,profile,editprofile
)
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard_startup'),
    path('profile/', profile, name='profile_startup'),
    path('editprofile/', editprofile, name='editprofile_startup'),
]
