# users/urls.py

from django.urls import path
from user.views import (
    # CustomLoginView, CustomLogoutView,
    home, register, login, logout
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
