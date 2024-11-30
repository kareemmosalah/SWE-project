from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

# Sample data for notifications and profile
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

schedule = [
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
]

# Views

def guest_login(request):
    messages.success(request, "Logged in as Guest.")
    return redirect('main_page')

def entry_page(request):
    return render(request, 'EntryPage.html')

def book_page(request):
    return render(request, 'Book_Page.html')

def court_info(request, court_id):
    court_data = {
        1: {
            'court_name': 'Court 1',
            'details': ['Detail 1', 'Detail 2'],
            'availability': ['Available 1', 'Available 2'],
            'pricing': '$10/hour',
            'location': 'Location 1',
            'contact': {'phone': '1234567890', 'email': 'court1@example.com'},
            'reviews': '4.5 Stars',
        },
        2: {
            'court_name': 'Court 2',
            'details': ['Detail 3', 'Detail 4'],
            'availability': ['Available 3', 'Available 4'],
            'pricing': '$15/hour',
            'location': 'Location 2',
            'contact': {'phone': '0987654321', 'email': 'court2@example.com'},
            'reviews': '4.0 Stars',
        },
    }
    context = court_data.get(court_id, {})
    return render(request, 'Court_Info.html', context)

def courts_list(request):
    city = request.GET.get('city')
    city_courts = {
        'cairo': [
            {'name': 'Court 1', 'id': 1},
            {'name': 'Court 2', 'id': 2},
        ],
        'alexandria': [
            {'name': 'Court 3', 'id': 3},
            {'name': 'Court 4', 'id': 4},
        ],
    }
    courts = city_courts.get(city, [])
    context = {'city': city, 'courts': courts}
    return render(request, 'Courts_List.html', context)

def court_schedule(request):
    context = {'schedule': schedule}
    return render(request, 'Court_schedule.html', context)

def book_time(request):
    if request.method == 'POST':
        time_slot = request.POST.get('time_slot')
        for slot in schedule:
            if slot['time'] == time_slot and slot['status'] == 'Available':
                slot['status'] = 'Booked'
                messages.success(request, f'Time slot {time_slot} booked successfully!')
                break
        return redirect('court_schedule')
    return redirect('court_schedule')

def main_page(request):
    context = {
        "user_name": request.user.username if request.user.is_authenticated else "Guest",
    }
    return render(request, 'MainPage.html', context)

@login_required
def profile_page(request):
    context = {"profile": sample_user_profile}
    return render(request, 'profile.html', context)

def admin_login_signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        is_signup = request.POST.get("is_signup") == "true"

        if is_signup:
            messages.success(request, "Admin account created successfully.")
        else:
            messages.success(request, "Admin logged in successfully.")
        return redirect('main_page')

    return render(request, 'AdminLoginSignup.html')

def player_login_signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        is_signup = request.POST.get("is_signup") == "true"

        if is_signup:
            messages.success(request, "Player account created successfully.")
        else:
            messages.success(request, "Player logged in successfully.")
        return redirect('main_page')

    return render(request, 'playerLoginSignup.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "testuser" and password == "password123":
            messages.success(request, "Logged in successfully.")
            return redirect('main_page')
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, 'LoginPage.html')

def signup_page(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect('main_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})