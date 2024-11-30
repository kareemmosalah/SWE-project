from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)

class Court(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    pricing = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    reviews = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='Available')

    def __str__(self):
        return f"{self.court.name} - {self.time}"