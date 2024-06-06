from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('AppCafe/',include('AppCafe.urls')),
    path('admin/', admin.site.urls),
]
