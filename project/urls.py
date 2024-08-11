from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path("investor/",include('investor.urls')),
    path("startup/",include('business.urls')),
]
