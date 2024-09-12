from django.urls import path
from investor.views import (
    dashboard,editprofile
)
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard_investor'),
    path('profile/edit', editprofile, name='editprofile_investor'),
    path('profile/view', editprofile, name='viewprofile_investor'),
    path('settings/change-password', dashboard, name='change_password_investor'),
    path('settings/delete-account', dashboard, name='delete_account_investor'),
]
