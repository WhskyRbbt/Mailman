from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin 

# Register your models here.
from .models import User, Package
admin.site.register(User)
admin.site.register(Package)

@admin.register(Package)
class pkgAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')