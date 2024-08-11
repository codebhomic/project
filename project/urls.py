from django.contrib import admin
from django.urls import path,include
from user.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('auth/', include('user.urls')),
    path("investor/",include('investor.urls')),
    path("startup/",include('business.urls')),
]
