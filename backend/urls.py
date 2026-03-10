from django.contrib import admin #type: ignore
from django.urls import path, include # type: ignore
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('accounts/', include('allauth.urls')),  # URLs do django-allauth
]
