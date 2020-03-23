from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin 

# Register your models here.
from .models import User, Package
admin.site.register(User)
admin.site.register(Package)

admin.site.unregister(User)
admin.site.unregister(Package)


@admin.register(User)
class LocationAdmin(OSMGeoAdmin):
    display = ('origination')
@admin.register(Package)
class LocationAdmin(OSMGeoAdmin):
    display = ('origination')