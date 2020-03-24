from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from main_app import views

urlpatterns = [
    path("", views.login, name="login"),
    # path("show_signup/", views.show_signup, name="show_signup"),
    path("signup/", views.signup, name="signup"),
    path("home/", views.home, name="home"),
    path("package/", views.PackageCreate.as_view(), name="package"),
    path("profile/", views.profile, name="profile"),
    path("package/<int:pkg_id>/", views.package_detail, name="detail"),
    url(r'^signup/$',views.signup, name='signup'),
]