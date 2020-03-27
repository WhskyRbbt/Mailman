from django.urls import path
from main_app import views

urlpatterns = [
    path("", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("home/", views.home, name="home"),
    path("package/<int:pkg_id>/", views.package_detail, name="detail"),
    path("profile/", views.profile, name="profile"),
    path("package/", views.package_create, name="package"),
    path("package/<int:pk>/update/", views.PackageUpdate.as_view(), name="package_update"),
    path("package/<int:pk>/delete/", views.PackageDelete.as_view(), name="package_delete"),
    path("package/<int:pkg_id>/assoc_driver/<int:user_id>/", views.assoc_driver, name="assoc_driver"),
]