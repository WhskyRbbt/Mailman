from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Package(models.Model):
    dimensions = models.CharField(max_length=20)
    weight = models.IntegerField()
    is_fragile = models.BooleanField()
    destination = models.CharField(max_length=250)
    destination_length = models.IntegerField()
    cost_of_delivery = models.IntegerField()
    completed = models.BooleanField(default=False)
    users = models.ManyToManyField(User)