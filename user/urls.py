from django.urls import path
from user.views import (
    # CustomLoginView, CustomLogoutView,
    home, register, login, logout,
    startup_register,investor_register,
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('register/investor/', startup_register, name='startup_register'),
    path('register/startup/', investor_register, name='investor_register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
