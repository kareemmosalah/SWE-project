from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model extending the default Django user model.
    Adds additional fields to distinguish between admin and player users.
    """
    is_admin = models.BooleanField(default=False)  # Indicates if the user is an admin
    is_player = models.BooleanField(default=False)  # Indicates if the user is a player
    is_court_owner = models.BooleanField(default=False)  # Indicates if the user is a court owner
class Court(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    pricing = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    reviews = models.CharField(max_length=50)
    city = models.CharField(max_length=100,default="Cairo")  # Add this line

    def __str__(self):
        return self.name

class CourtSchedule(models.Model):
    court_id = models.ForeignKey(Court, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f'Court {self.court.name} - {self.time} - {self.status}'
    
class Datacsv(models.Model):  
    date = models.DateField()  
    average = models.FloatField()  

    class Meta: 
        ordering = ('date',)
        
class Owner(models.Model):
    email = models.EmailField(unique=True)

    def calculate_total_profits(self):
        courts = Court.objects.filter(contact_email=self.email)
        total_profit = sum(
            booking.amount_paid for court in courts for booking in Booking.objects.filter(court=court)
        )
        return total_profit