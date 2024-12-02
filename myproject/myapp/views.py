from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth import get_user_model, load_backend
import requests
import json

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

# Define schedules for each court by ID
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
    # Add more courts as needed
}

# Views


def guest_login(request):
    """
    Logs in the user as a guest and redirects to the main page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponseRedirect: Redirects to the main page.
    """
    messages.success(request, "Logged in as Guest.")
    return redirect('main_page')

def entry_page(request):
    """
    Renders the entry page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: Renders the EntryPage.html template.
    """
    return render(request, 'EntryPage.html')

def book_page(request):
    """
    Renders the booking page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: Renders the Book_Page.html template.
    """
    return render(request, 'Book_Page.html')

def court_info(request, court_id):
    """
    Provides information about a specific court based on the court_id.
    
    Args:
        request: The HTTP request object.
        court_id: The ID of the court to retrieve information for.
    
    Returns:
        HttpResponse: Renders a template with court information.
    """
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
    court_id = int(court_id)  # Ensure court_id is an integer
    context = court_data.get(court_id, {})
    context['court_id'] = court_id  # Include court_id in the context
    return render(request, 'Court_Info.html', context)

def courts_list(request):
    """
    View function that retrieves a list of courts based on the specified city.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response containing the list of courts.

    """
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



def court_schedule(request, court_id):
    """
    View function to display the schedule for a specific court.

    Args:
        request (HttpRequest): The HTTP request object.
        court_id (int): The ID of the court.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.

    """
    # court_schedules = {
    #     1: [
    #         {'time': '08:00 AM - 09:00 AM', 'status': 'Available'},
    #         {'time': '09:00 AM - 10:00 AM', 'status': 'Booked'},
    #         # Add more time slots as needed
    #     ],
    #     2: [
    #         {'time': '08:00 AM - 09:00 AM', 'status': 'Booked'},
    #         {'time': '09:00 AM - 10:00 AM', 'status': 'Available'},
    #         # Add more time slots as needed
    #     ],
    # }
    schedule = court_schedules.get(court_id, [])
    context = {'schedule': schedule, 'court_id': court_id}
    return render(request, 'Court_schedule.html', context)


# Assuming court_schedules is a global variable or can be fetched from a database


def book_time(request, court_id):
    """
    View function to book a time slot for a court.

    Args:
        request (HttpRequest): The HTTP request object.
        court_id (int): The ID of the court.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        None

    """
    if request.method == 'POST':
        time_slot = request.POST.get('time_slot')

        if not time_slot:
            messages.error(request, 'No time slot selected.')
            return redirect('court_schedule', court_id=court_id)

        schedule = court_schedules.get(court_id, [])

        for slot in schedule:
            if slot['time'] == time_slot:
                if slot['status'] == 'Available':
                    slot['status'] = 'Booked'
                    messages.success(request, f'Time slot "{time_slot}" booked successfully!')
                else:
                    messages.error(request, f'Time slot "{time_slot}" is already booked.')
                break
        else:
            messages.error(request, f'Time slot "{time_slot}" not found.')

        # Pass updated schedule back to the template
        return render(request, 'court_schedule.html', {'schedule': schedule, 'court_id': court_id})

    return redirect('court_schedule', court_id=court_id)



def main_page(request):
    """
    Renders the main page with the user's name if authenticated, otherwise as 'Guest'.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered main page with the context containing the user's name.
    """
    context = {
        "user_name": request.user.username if request.user.is_authenticated else "Guest",
    }
    return render(request, 'MainPage.html', context)

@login_required
def user_profile(request):
    """
    Renders the user profile page for authenticated users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered user profile page with the context containing the sample user profile.
    """
    context = {"profile": sample_user_profile}
    return render(request, 'user_profile.html', context)

def login_signup_page(request):
    """
    Handles the login and signup functionality for users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered login/signup page with the appropriate context.

    The function determines whether the user is attempting to log in or sign up based on the POST data.
    It validates the form data and either logs the user in or creates a new user account.
    """
    user_type = request.GET.get('user_type', 'player')  # Default to 'player'

    if request.method == "POST":
        action = request.POST.get('action')  # Determine login or signup
        user_type = request.POST.get('user_type')  # Get user type
        
        if action == "Login":
            form = CustomUserLoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                # Authenticate user
                user = authenticate(username=username, password=password)
                if user and ((user.is_player and user_type == 'player') or (user.is_admin and user_type == 'admin')):
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    messages.success(request, f"Welcome back, {user.username}!")
                    return redirect('main_page')
                else:
                    messages.error(request, "Invalid credentials or incorrect user type.")
            else:
                messages.error(request, "Login failed. Please check your input.")
                
        elif action == "signup":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_player = user_type == 'player'
                user.is_admin = user_type == 'admin'
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, "Account created successfully!")
                return redirect('main_page')
            else:
                messages.error(request, "Signup failed. Please check your input.")

    else:
        form = CustomUserLoginForm()

    return render(request, 'login_signup.html', {'user_type': user_type})

@login_required
def court_owner_dashboard(request):
    """
    Renders the dashboard for court owners with their courts and total profit.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered owner dashboard page with the context containing the courts and total profit.

    The function retrieves all courts owned by the logged-in user and calculates the total profit from bookings.
    """
    courts = Court.objects.filter(owner=request.user)
    total_profit = sum(booking.amount_paid for booking in Booking.objects.filter(court__in=courts))
    context = {
        'courts': courts,
        'total_profit': total_profit,
    }
    return render(request, 'owner.html', context)

def add_court(request):
    """
    Handles the addition of a new court by the court owner.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the court owner dashboard if the court is successfully added,
                      otherwise renders the add court page.

    The function processes the POST request to create a new court with the provided name, location, and price.
    """
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        price = request.POST['price']
        Court.objects.create(owner=request.user, name=name, location=location, price_per_hour=price)
        return redirect('court_owner_dashboard')
    return render(request, 'court_owner/add_court.html')

def view_profits(request):
    """
    Displays the total profit for the court owner from all their courts.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered view profits page with the context containing the total profit.

    The function calculates the total profit from all bookings for the courts owned by the logged-in user.
    """
    courts = Court.objects.filter(owner=request.user)
    total_profit = sum(booking.amount_paid for booking in Booking.objects.filter(court__in=courts))
    return render(request, 'court_owner/view_profits.html', {'total_profit': total_profit})

def send_notification(registration_ids, message_title, message_desc):
    """
    Sends a notification to the specified registration IDs using Firebase Cloud Messaging (FCM).

    Args:
        registration_ids (list): List of registration IDs to send the notification to.
        message_title (str): The title of the notification message.
        message_desc (str): The body of the notification message.

    Returns:
        None

    The function constructs the payload with the provided message title and description,
    and sends a POST request to the FCM API endpoint with the necessary headers.
    """
    fcm_api = "YOUR_SERVER_KEY"  # Replace with your actual FCM server key
    url = "https://fcm.googleapis.com/fcm/send"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f'key={fcm_api}'
    }

    payload = {
        "registration_ids": registration_ids,
        "priority": "high",
        "notification": {
            "body": message_desc,
            "title": message_title,
        }
    }

    result = requests.post(url, data=json.dumps(payload), headers=headers)
    print(result.json())

def notification_page(request):
    """
    Renders the notification page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered notification page.

    The function simply renders the 'Notification.html' template.
    """
    return render(request, 'Notification.html')