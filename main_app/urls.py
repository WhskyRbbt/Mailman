from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("", views.login, name="login"),
    # path("show_signup/", views.show_signup, name="show_signup"),
    path("signup/", views.signup, name="signup"),
    path("home/", views.home, name="home"),
    path("shipment/", views.shipment, name="shipment"),
    path("create_shipment/", views.create_shipment, name="create_shipment"),
    path("profile/", views.profile, name="profile"),
]