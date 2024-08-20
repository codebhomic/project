from django.urls import path
from user.views import (
    # CustomLoginView, CustomLogoutView,
    home, register, login, logout,
    startup_register,investor_register,
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('register/investor/', startup_register, name='register_startup'),
    path('register/startup/', investor_register, name='register_investor'),
    path('login/startup', login, name='login_startup'),
    path('login/investor', login, name='login_investor'),
    path('logout/', logout, name='logout'),
]
