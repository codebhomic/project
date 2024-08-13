from django.urls import path
from investor.views import (
    dashboard
)
urlpatterns = [
    path('', dashboard, name='investor_dashboard'),
]
