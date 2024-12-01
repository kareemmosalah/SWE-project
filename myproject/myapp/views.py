from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

court_schedules = {
    1: [
        {'time': '10:00 AM - 11:00 AM', 'status': 'Available'},
        {'time': '11:00 AM - 12:00 PM', 'status': 'Booked'},
    ],
    2: [
        {'time': '10:00 AM - 11:00 AM', 'status': 'Available'},
        {'time': '11:00 AM - 12:00 PM', 'status': 'Available'},
    ],
}

def guest_login(request):
    """
    Logs in the user as a guest and redirects to the main page.
    """
    messages.success(request, "Logged in as Guest.")
    return redirect('main_page')

def entry_page(request):
    """
    Renders the entry page.
    """
    return render(request, 'EntryPage.html')

def book_page(request):
    """
    Renders the booking page.
    """
    return render(request, 'Book_Page.html')

def court_info(request, court_id):
    """
    Displays information about a specific court based on the court_id.
    """
    if court_id == 1:
        context = {
            'court_id': court_id,
            'court_name': 'Court 1',
            'details': ['Detail 1', 'Detail 2'],
            'availability': ['Available 1', 'Available 2'],
            'pricing': '$10/hour',
            'location': 'Location 1',
            'contact': {'phone': '1234567890', 'email': 'court1@example.com'},
            'reviews': '4.5 Stars'
        }
    elif court_id == 2:
        context = {
            'court_id': court_id,
            'court_name': 'Court 2',
            'details': ['Detail 3', 'Detail 4'],
            'availability': ['Available 3', 'Available 4'],
            'pricing': '$15/hour',
            'location': 'Location 2',
            'contact': {'phone': '0987654321', 'email': 'court2@example.com'},
            'reviews': '4.0 Stars'
        }
    else:
        context = {}

    return render(request, 'Court_Info.Html', context)

def courts_list(request):
    """
    Displays a list of courts based on the selected city.
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
    Displays the schedule for a specific court based on the court_id.
    """
    schedule = court_schedules.get(court_id, [])
    context = {'court_id': court_id, 'schedule': schedule}
    return render(request, 'Court_Schedule.html', context)

def book_time(request, court_id):
    """
    Books a time slot for a specific court based on the court_id.
    """
    if request.method == 'POST':
        time_slot = request.POST.get('time_slot')
        schedule = court_schedules.get(court_id, [])
        for slot in schedule:
            if slot['time'] == time_slot and slot['status'] == 'Available':
                slot['status'] = 'Booked'
                messages.success(request, f'Time slot {time_slot} for Court {court_id} booked successfully!')
                break
        else:
            messages.error(request, f'Time slot {time_slot} is unavailable.')
        return redirect('court_schedule', court_id=court_id)
    return redirect('court_schedule', court_id=court_id)

def main_page(request):
    """
    Renders the main page with the user's name if authenticated, otherwise as Guest.
    """
    context = {
        "user_name": request.user.username if request.user.is_authenticated else "Guest",
    }
    return render(request, 'MainPage.html', context)

@login_required
def profile_page(request):
    """
    Renders the profile page for the logged-in user.
    """
    context = {"profile": sample_user_profile}
    return render(request, 'profile.html', context)

def admin_login_signup(request):
    """
    Handles admin login and signup.
    """
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
    """
    Handles player login and signup.
    """
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
    """
    Handles user login.
    """
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
    """
    Handles user signup.
    """
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            messages.success(request, f"Account created for {full_name}.")
            return redirect('login_page')

    return render(request, 'signup.html')

def add_court(request):
    """
    Handles the addition of a new court by the court owner.
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
    Displays the total profits for the court owner.
    """
    courts = Court.objects.filter(owner=request.user)
    total_profit = sum(booking.amount_paid for booking in Booking.objects.filter(court__in=courts))
    return render(request, 'court_owner/view_profits.html', {'total_profit': total_profit})

def test_view(request):
    """
    A simple test view to check if the court owner page is working.
    """
    return HttpResponse("Court Owner Page is Working!")

def court_owner_page(request):
    """
    Renders the main page for the court owner.
    """
    return render(request, 'owner.html')

def user_profile(request):
    """
    Renders the user profile page.
    """
    return render(request, 'user_profile.html')



def send_notification(registration_ids, message_title, message_desc):
    """
    Sends a notification to the specified registration IDs using the Firebase Cloud Messaging (FCM) service.

    Args:
        registration_ids (list): A list of registration IDs to send the notification to.
        message_title (str): The title of the notification message.
        message_desc (str): The description/body of the notification message.

    Returns:
        dict: The response from the FCM service.

    Raises:
        requests.exceptions.RequestException: If there was an error sending the notification.

    """
    fcm_api = "cQmkGHZZtTc5m__kV8m2QN:APA91bGoDq76gdhk4JgfzqDWvfHYLcRaOfFIwazw4bGSOwawE6o1P0pPpdo00fUgtSwPqEgCwdZflXJkpXK1i440SoGQtjmzKkSVbCWt8-wh8-U5gfUvQ98"  # Replace with your actual FCM server key
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
            "image": "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj"
        }
    }

    result = requests.post(url, data=json.dumps(payload), headers=headers)
    print(result.json())

@login_required
def court_owner_dashboard(request):
    """
    Renders the court owner dashboard, showing options to add courts and view profits.
    """
    courts = Court.objects.filter(owner=request.user)
    total_profit = sum(booking.amount_paid for booking in Booking.objects.filter(court__in=courts))
    context = {
        'courts': courts,
        'total_profit': total_profit,
    }
    return render(request, 'owner.html', context)

# def index(request):
#     """
#     Renders the 'Notification.html' template.

#     Args:
#         request: The HTTP request object.

#     Returns:
#         A rendered HTML response.
#     """
#     return render(request, 'Notification.html')

# def send(request):
#     """
#     Sends a notification to the specified registration tokens.

#     Args:
#         request: The HTTP request object.

#     Returns:
#         An HttpResponse indicating that the notification has been sent.
#     """
#     registration = [  # Add actual registration IDs here
#         "registration_token_1",
#         "registration_token_2"
#     ]
#     send_notification(registration, 'ilovecoding', 'notreely')
#     return HttpResponse("Notification sent")


# def showFirebaseJS(request):
#     data = '''importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");
#               importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js");
#               var firebaseConfig = {
#                   apiKey: "AIzaSyD-Qvpmlec1yGj3Om2fumMRDWrWT_hEZSY",
#                   authDomain: "fir-5a3d4.firebaseapp.com",
#                   projectId: "fir-5a3d4",
#                   storageBucket: "fir-5a3d4.firebasestorage.app",
#                   messagingSenderId: "1096296766719",
#                   appId: "1:1096296766719:web:dea231a92cf3237c6fc0ca",
#                   measurementId: "G-VZNEYLKJ7H"
#               };
#               firebase.initializeApp(firebaseConfig);
#               const messaging = firebase.messaging();
#               messaging.setBackgroundMessageHandler(function(payload) {
#                   console.log(payload);
#                   const notification = JSON.parse(payload);
#                   const notificationOption = {
#                       body: notification.body,
#                       icon: notification.icon
#                   };
#                   return self.registration.showNotification(payload.notification.title, notificationOption);
#               });
#            '''
#     return HttpResponse(data, content_type="text/javascript")
