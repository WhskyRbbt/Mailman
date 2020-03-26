from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("main_app.urls")),
    path("", include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
]