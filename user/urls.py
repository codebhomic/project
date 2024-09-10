from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import (
    # CustomLoginView, CustomLogoutView,
    home, register, userlogin, userlogout,activate,
    startup_register,investor_register,activation_sent,
    PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView,
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('register/startup/', startup_register, name='register_startup'),
    path('register/investor/', investor_register, name='register_investor'),
    path('login/startup/', userlogin, name='login_startup'),
    path('login/investor/', userlogin, name='login_investor'),
    path('logout/', userlogout, name='logout'),
    path('activation_sent/', activation_sent, name='activation_sent'),
    path('activate/<uidb64>/<token>/<user_type>', activate, name='activate'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView .as_view(), name='password_reset_complete'),
]
