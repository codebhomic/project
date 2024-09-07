from django.contrib import admin
from django.urls import path,include
from user.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('auth/', include('user.urls')),
    path("investor/",include('investor.urls')),
    path("startup/",include('business.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)