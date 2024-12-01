from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomUserLoginForm

from django.contrib.auth import get_user_model, load_backend

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
from django.shortcuts import render, redirect
from django.contrib import messages

# Existing imports...

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
        is_signup = request.POST.get("is_signup") == "true"

        if is_signup:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_admin = True  # Set admin flag
                user.is_player = False  # Ensure player flag is False
                user.is_staff = True  # Admins should have staff privileges
                user.is_superuser = True  # Admins should have superuser privileges
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, "Admin account created successfully!")
                return redirect('main_page')
            else:
                for field, errors in form.errors.items():
                    messages.error(request, f"{field}: {', '.join(errors)}")
        else:
            form = CustomUserLoginForm(request, data=request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
                if user is not None and user.is_admin:
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    messages.success(request, f"Welcome back, Admin {user.username}!")
                    return redirect('main_page')
                elif user is not None:
                    messages.error(request, "You do not have admin privileges.")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                for field, errors in form.errors.items():
                    messages.error(request, f"{field}: {', '.join(errors)}")
    else:
        form = CustomUserCreationForm() if request.GET.get("is_signup") == "true" else CustomUserLoginForm()
    return render(request, 'adminLoginSignup.html', {'form': form})

# views.py

def player_login_signup(request):
    if request.method == "POST":
        is_signup = request.POST.get("is_signup") == "true"

        if is_signup:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_player = True  # Set player flag
                user.is_admin = False  # Ensure admin flag is False
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, "Player account created successfully!")
                return redirect('main_page')
            else:
                for field, errors in form.errors.items():
                    messages.error(request, f"{field}: {', '.join(errors)}")
        else:
            form = CustomUserLoginForm(request, data=request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
                if user is not None and user.is_player:
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    messages.success(request, f"Welcome back, Player {user.username}!")
                    return redirect('main_page')
                elif user is not None:
                    messages.error(request, "You do not have player privileges.")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                for field, errors in form.errors.items():
                    messages.error(request, f"{field}: {', '.join(errors)}")
    else:
        form = CustomUserCreationForm() if request.GET.get("is_signup") == "true" else CustomUserLoginForm()
    return render(request, 'playerLoginSignup.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('main_page')
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

# views.py
def signup_page(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, f"Account created successfully, {user.username}. Please explore our features!")
            return redirect('main_page')
        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})