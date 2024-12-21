from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth import get_user_model, load_backend
import requests
import json
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Court
from .models import CustomUser

#sample data for notifications and profile
sample_notifications = [
    {"title": "Booking Confirmed", "message": "Your booking at Court 1 is confirmed.", "read": False},
    {"title": "Payment Reminder", "message": "Your payment for Court 2 is pending.", "read": True},
]

sample_user_profile = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "bookings": [
        {"court": "Court 1", "date": "2024-12-01", "time": "10:00 AM"},
        {"court": "Court 2", "date": "2024-12-05", "time": "3:00 PM"},
    ],
}

#schedules for each court by ID
court_schedules = {
    1: [
        {'time': '08:00 AM - 09:00 AM', 'status': 'Available'},
        {'time': '09:00 AM - 10:00 AM', 'status': 'Available'},
        {'time': '10:00 AM - 11:00 AM', 'status': 'Available'},
        {'time': '11:00 AM - 12:00 PM', 'status': 'Available'},
        {'time': '12:00 PM - 01:00 PM', 'status': 'Available'},
        {'time': '01:00 PM - 02:00 PM', 'status': 'Available'},
        {'time': '02:00 PM - 03:00 PM', 'status': 'Available'},
        {'time': '03:00 PM - 04:00 PM', 'status': 'Available'},
        {'time': '04:00 PM - 05:00 PM', 'status': 'Available'},
        {'time': '05:00 PM - 06:00 PM', 'status': 'Available'},
    ],
    2: [
        {'time': '08:00 AM - 09:00 AM', 'status': 'Available'},
        {'time': '09:00 AM - 10:00 AM', 'status': 'Available'},
        {'time': '10:00 AM - 11:00 AM', 'status': 'Available'},
        {'time': '11:00 AM - 12:00 PM', 'status': 'Available'},
        {'time': '12:00 PM - 01:00 PM', 'status': 'Available'},
        {'time': '01:00 PM - 02:00 PM', 'status': 'Available'},
        {'time': '02:00 PM - 03:00 PM', 'status': 'Available'},
        {'time': '03:00 PM - 04:00 PM', 'status': 'Available'},
        {'time': '04:00 PM - 05:00 PM', 'status': 'Available'},
        {'time': '05:00 PM - 06:00 PM', 'status': 'Available'},
    ],
}

#views


def guest_login(request):
    messages.success(request, "Logged in as Guest.") #to show a success message.
    return redirect('main_page') #to redirect to the main page.

def entry_page(request):
    return render(request, 'EntryPage.html')

def book_page(request):
    return render(request, 'Book_Page.html')


from django.shortcuts import render, get_object_or_404
from .models import Court

def court_info(request, court_id):
    court = get_object_or_404(Court, id=court_id) #to get the court for the id.
    context = {
        'court_id': court.id,
        'court_name': court.name,
        'details': court.details.split(','), 
        'pricing': court.pricing,
        'location': court.location,
        'contact': {'phone': court.contact_phone, 'email': court.contact_email},
        'reviews': court.reviews,
    }
    return render(request, 'Court_Info.html', context)

def courts_list(request):
    city = request.GET.get('city') #to get the city from the request.   
    print(city)  
    courts = Court.objects.filter(city__icontains=city) #to get the courts for the city.
    print(courts)  
    context = {'city': city, 'courts': courts} #to pass the city and courts to the template.
    print(context)  
    return render(request, 'Courts_List.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CourtSchedule

def book_time(request, court_id):

    if request.method == 'POST':
        time_slot = request.POST.get('time_slot') #to book a time slot for a court.

        if not time_slot:
            messages.error(request, 'No time slot selected.') #if no time slot is selected.
            return redirect('court_schedule', court_id=court_id) #redirect to the court schedule page.

        try:
            slot = CourtSchedule.objects.get(court_id=court_id, time=time_slot) #to get the time slot for the court.
            if slot.status == 'Available': 
                slot.status = 'Booked' #to book the time slot.
                slot.save() #to save the time slot.
                messages.success(request, f'Time slot "{time_slot}" booked successfully!') #to show a success message.
            else:
                messages.error(request, f'Time slot "{time_slot}" is already booked.') #to show an error message.
        except CourtSchedule.DoesNotExist:
            messages.error(request, f'Time slot "{time_slot}" not found.')

        schedule = CourtSchedule.objects.filter(court_id=court_id) #to get the schedule for the court.
        return render(request, 'court_schedule.html', {'schedule': schedule, 'court_id': court_id}) #to render the court schedule page.

    return redirect('court_schedule', court_id=court_id)

def court_schedule(request, court_id):
    schedule = CourtSchedule.objects.filter(court_id=court_id) #to get the schedule for the court.
    context = {'schedule': schedule, 'court_id': court_id} #to pass the schedule to the template.
    return render(request, 'court_schedule.html', context) #to render the court schedule page.


def cancel_booking(request, court_id):
    if request.method == 'POST':
        time_slot = request.POST.get('time_slot') #to cancel a booking for a court. 
        court_schedule = get_object_or_404(CourtSchedule, court_id=court_id, time=time_slot) #to get the court schedule for the court.
        court_schedule.status = 'Available' #to set the status of the time slot to available.
        court_schedule.save() #to save the time slot.
        messages.success(request, 'Booking cancelled successfully.') #to show a success message.
        return redirect('court_schedule', court_id=court_id)
    return redirect('court_schedule', court_id=court_id)



def main_page(request):
    context = {
        "user_name": request.user.username if request.user.is_authenticated else "Guest",
    }
    return render(request, 'MainPage.html', context) 

@login_required
def user_profile(request): 
    context = {"profile": sample_user_profile}
    return render(request, 'user_profile.html', context)

def login_signup_page(request):
    user_type = request.GET.get('user_type', 'player')  #default to 'player'

    if request.method == "POST":
        action = request.POST.get('action')  #determine login or signup
        user_type = request.POST.get('user_type')  #get user type
        
        if action == "Login":
            form = CustomUserLoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                #authenticate user
                user = authenticate(username=username, password=password) 
                if user and ((user.is_player and user_type == 'player') or 
                             (user.is_admin and user_type == 'admin') or 
                             (user.is_court_owner and user_type == 'court_owner')): 
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend') #to login the user.
                    messages.success(request, f"Welcome back, {user.username}!") #to show a success message.
                    return redirect('main_page') #to redirect to the main page.
                else:
                    messages.error(request, "Invalid credentials or incorrect user type.")
            else:
                messages.error(request, "Login failed. Please check your input.") #to show an error message.
        elif action == "Signup":
            form = CustomUserCreationForm(request.POST) #to create a new user.
            if form.is_valid():
                user = form.save(commit=False) #to save the user without committing to the database.
                user.is_player = user_type == 'player'
                user.is_admin = user_type == 'admin'
                user.is_court_owner = user_type == 'court_owner'
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend') #to login the user.
                messages.success(request, "Account created successfully!") #to show a success message.
                return redirect('main_page') #to redirect to the main page.
            else:
                messages.error(request, "Signup failed. Please check your input.") #to show an error message.

    else:
        form = CustomUserLoginForm() #to create a new login form.

    return render(request, 'login_signup.html', {'user_type': user_type}) #to render the login signup page.



def add_court(request): 
    if request.method == 'POST': #if the request method is post.      
        name = request.POST['courtName']  
        location = request.POST['location'] 
        price = request.POST['price'] 
        city = request.POST['city'] 
        contact_phone = request.user.username
        contact_email = request.user.email  

        #save court to database
        Court.objects.create(
            name=name,
            location=location,
            pricing=price,
            city=city,  
            contact_phone=contact_phone,
            contact_email=contact_email,
            details='Details not provided', 
            reviews='No reviews yet',
        )
        messages.success(request, "Court added successfully!")
        return redirect('court_owner_dashboard')

    return render(request, 'owner.html') 

#view profits 
def view_profits(request):
    courts = Court.objects.filter(owner=request.user)
    total_profit = sum(booking.amount_paid for booking in Booking.objects.filter(court__in=courts))
    return render(request, 'court_owner/view_profits.html', {'total_profit': total_profit})


def notification_page(request): 
    return render(request, 'Notification.html')

from .models import Court 

def court_owner_dashboard(request): #to view the court owner dashboard.
    courts = Court.objects.filter(contact_email=request.user.email) #to get the courts for the user.    
    context = {'courts': courts} #to pass the courts to the template.
    return render(request, 'owner.html', context) 


from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def change_username(request): 
    if request.method == 'POST':
        new_username = request.POST['new_username']
        request.user.username = new_username
        request.user.save()
        messages.success(request, "Username updated successfully!")
    return redirect('user_profile')

from django.contrib.auth.forms import PasswordChangeForm

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST) #to create a new password change form.
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  #keeps the user logged in
            messages.success(request, "Password updated successfully!")
        else:
            messages.error(request, "Password update failed. Please check the form.")
    return redirect('user_profile')


def chart(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    data = Datacsv.objects.all() #to get the data from the database.

    if start:
        data = data.filter(date__gte=start) #to filter the data by start date.
    if end:
        data = data.filter(date__lte=end) #to filter the data by end date.

    fig = px.line(
        x=[c.date for c in data], 
        y=[c.average for c in data], 
        title="Average profit per year",
        labels={'x': 'Date', 'y': 'Profit'}
    )

    fig.update_layout(
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
        })
    
    chart = fig.to_html() #to convert the figure to html.
    context = {'chart': chart, 'form': DateForm()} #to pass the chart to the template.
    return render(request, 'myproject/myapp/templates/reportpage.html', context)

def view_courts(request):
    courts = Court.objects.filter(contact_email=request.user.email) #to get the courts for the user.
    return render(request, 'view_courts.html', {'courts': courts}) #to render the view courts page.

def settings_page(request):
    return render(request, 'settings.html')

def logout_view(request):
    logout(request)
    return redirect('entry_page')

def home_page(request):
    return render(request, 'home.html')



@login_required
def admin_dashboard(request):
    selected_city = request.GET.get('city', '') #to get the selected city.
    
    if selected_city: 
        courts = Court.objects.filter(city=selected_city) #to get the courts for the selected city.
    else:
        courts = Court.objects.all() #to get all the courts.
    
    if request.method == 'POST':
        if 'court_id' in request.POST:
            court_id = request.POST.get('court_id')
            if Court.objects.filter(id=court_id).exists(): 
                Court.objects.filter(id=court_id).delete() #to delete the court.
                messages.success(request, "Court deleted successfully!") #to show a success message.
            else:
                messages.error(request, "Court not found.") #to show an error message.
        elif 'user_id' in request.POST:
            user_id = request.POST.get('user_id')
            if CustomUser.objects.filter(id=user_id).exists():
                CustomUser.objects.filter(id=user_id).delete()
                messages.success(request, "User deleted successfully!")
            else:
                messages.error(request, "User not found.") #to show an error message.
        return redirect('admin_dashboard')

    cities = Court.objects.values_list('city', flat=True).distinct() #to get the cities from the courts.

    users = CustomUser.objects.all()

    context = {
        'courts': courts, 
        'cities': cities,
        'selected_city': selected_city,
        'users': users,
    }
    return render(request, 'admin_dashboard.html', context)

from django.shortcuts import render
import plotly.express as px
from .utils import generate_fake_profits  
def owner_profits_view(request): 
   data = generate_fake_profits() #to generate fake profits.
   emails = [d['email'] for d in data] #to get the emails from the data.
   total_profits = [sum(d['profits']) for d in data] #to get the total profits from the data.
   bar_fig = px.bar(
       x=emails,
       y=total_profits,
       labels={'x': 'Owner Email', 'y': 'Total Profit'},
       title='Total Profits by Owner'
   )
   pie_fig = px.pie(
       values=total_profits,
       names=emails,
       title='Profit Distribution Among Owners'
   )
   context = {
       'bar_chart': bar_fig.to_html(),
       'pie_chart': pie_fig.to_html(),
   }
   return render(request, 'owner_profits.html', context)
