from django.urls import path
from business.views import (
    dashboard
)
urlpatterns = [
    path('', dashboard, name='startup_dashboard'),
]
