from django.urls import path
from business.views import (
    home
)
urlpatterns = [
    path('', home, name='home'),
]
