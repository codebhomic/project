from django.urls import path
from business.views import (
    dashboard
)
urlpatterns = [
    path('dashboard', dashboard, name='dashboard_startup'),
]
