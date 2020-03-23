from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    display_name = models.CharField(max_length=15)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class Package(models.Model):
    dimensions = models.CharField(max_length=20)
    weight = models.IntegerField()
    is_fragile = models.BooleanField()
    origination = models.CharField(max_length=100, default="00000 Blank Street 00000 CA")
    destination = models.CharField(max_length=250)
    destination_length = models.IntegerField()
    cost_of_delivery = models.IntegerField()
    completed = models.BooleanField(default=False)
    users = models.ManyToManyField(User)
    
    
    class SignUpForm(UserCreationForm):
        first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    