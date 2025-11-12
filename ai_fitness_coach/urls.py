from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("users:login")),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('diet/', include('diet.urls')),
]
