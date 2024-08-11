from django.urls import path
from investor.views import (
    home
)
urlpatterns = [
    path('', home, name='home'),
]
