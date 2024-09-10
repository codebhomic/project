from django.urls import path
from investor.views import (
    dashboard
)
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard_investor'),
    path('profile/edit', dashboard, name='editprofile_investor'),
    path('profile/view', dashboard, name='viewprofile_investor'),
    path('settings/change-password', dashboard, name='change_password_investor'),
    path('settings/delete-account', dashboard, name='delete_account_investor'),
]
