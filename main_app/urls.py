from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path("", views.login, name="landing"),
    path("", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    
]