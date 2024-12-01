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
    """
    Model representing a court.
    Contains details about the court such as name, details, pricing, location, contact information, and reviews.
    """
    name = models.CharField(max_length=100)  # Name of the court
    details = models.TextField()  # Detailed description of the court
    pricing = models.CharField(max_length=50)  # Pricing information for the court
    location = models.CharField(max_length=100)  # Location of the court
    contact_phone = models.CharField(max_length=15)  # Contact phone number for the court
    contact_email = models.EmailField()  # Contact email for the court
    reviews = models.CharField(max_length=50)  # Reviews for the court

    def __str__(self):
        return self.name  # String representation of the court

class Schedule(models.Model):
    """
    Model representing the schedule for a court.
    Contains information about the court, time, and status of the schedule.
    """
    court = models.ForeignKey(Court, on_delete=models.CASCADE)  # Foreign key to the Court model
    time = models.CharField(max_length=50)  # Time slot for the schedule
    status = models.CharField(max_length=20, default='Available')  # Status of the schedule (e.g., Available, Booked)

    def __str__(self):
        return f"{self.court.name} - {self.time}"  # String representation of the schedule