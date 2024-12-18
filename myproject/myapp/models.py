from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model extending the default Django user model.
    Adds additional fields to distinguish between admin and player users.
    """
    is_admin = models.BooleanField(default=False)  # Indicates if the user is an admin
    is_player = models.BooleanField(default=False)  # Indicates if the user is a player

class Court(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    pricing = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    reviews = models.CharField(max_length=50)
    city = models.CharField(max_length=100)  # Add this line

    def __str__(self):
        return self.name
    def __str__(self):
        return self.name
class Schedule(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='Available')

    def __str__(self):
        return f"{self.court.name} - {self.time}"
    
class Datacsv(models.Model):  
    date = models.DateField()  
    average = models.FloatField()  

    class Meta: 
        ordering = ('date',)