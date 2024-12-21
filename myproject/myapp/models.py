from django.db import models
from django.contrib.auth.models import AbstractUser

#custom user model to extend the default django user model. 
class CustomUser(AbstractUser): 
    is_admin = models.BooleanField(default=False)  
    is_player = models.BooleanField(default=False) 
    is_court_owner = models.BooleanField(default=False) 

#court model to store the court details. 
class Court(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    pricing = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    reviews = models.CharField(max_length=50)
    city = models.CharField(max_length=100,default="Cairo")  

    def __str__(self):
        return self.name

#court schedule model to store the court schedule details. 
class CourtSchedule(models.Model):
    court= models.ForeignKey(Court, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    booked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Court {self.court.name} - {self.time} - {self.status}'
    
#datacsv model to store the data from the csv file. 
class Datacsv(models.Model):  
    date = models.DateField()  
    average = models.FloatField()  

    class Meta: 
        ordering = ('date',)

#owner model to store the owner details. 
class Owner(models.Model):
    email = models.EmailField(unique=True)

#method to calculate the total profits for the owner. 
    def calculate_total_profits(self):
        courts = Court.objects.filter(contact_email=self.email)
        total_profit = sum(
            booking.amount_paid for court in courts for booking in Booking.objects.filter(court=court)
        )
        return total_profit