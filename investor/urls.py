from django.urls import path
from investor.views import (
    dashboard
)
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard_investor'),
]
