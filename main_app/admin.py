from django.contrib import admin

# Register your models here.
from .models import User, Package
admin.site.register(User)
admin.site.register(Package)