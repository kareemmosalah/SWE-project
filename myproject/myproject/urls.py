from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for account management
    path('guest-login/', views.guest_login, name='guest_login'),  # Guest login URL
    path('', views.entry_page, name='home_page'),  # Entry page URL
    path('book/', views.book_page, name='book_page'),  # Booking page URL
    path('court-info/<int:court_id>/', views.court_info, name='court_info'),  # Court info URL with court_id parameter
    path('courts-list/', views.courts_list, name='courts_list'),  # Courts list URL
    path('court-schedule/<int:court_id>/', views.court_schedule, name='court_schedule'),  # Court schedule URL with court_id parameter
    path('main/', views.main_page, name='main_page'),  # Main page URL

    path('login-signup/', views.login_signup_page, name='login_signup_page'),
    path('book-time/<int:court_id>/', views.book_time, name='book_time'),  # Book time URL with court_id parameter
    
    path('user-profile/', views.user_profile, name='user_profile'),
    path('owner', views.court_owner_dashboard, name='court_owner_dashboard'),
    path('Notification/' , views.notification_page , name='notification'),
    # path('send/' , views.send),
    # path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js")  # User profile page URL
    path('change-username/', views.change_username, name='change_username'),
    path('change-password/', views.change_password, name='change_password'),
]