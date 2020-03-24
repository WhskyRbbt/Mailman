from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin 

# Register your models here.
from .models import User, Package, Profile
admin.site.register(User)
admin.site.register(Package)

admin.site.unregister(User)
admin.site.unregister(Package)

@admin.register(User)
class UserAdmin(OSMGeoAdmin):
    display = ('display_name')

@admin.register(Package)
class PackageAdmin(OSMGeoAdmin):
    display = ('origination')

@admin.register(Profile)
class ProfileAdmin(OSMGeoAdmin):
    display = ('user')