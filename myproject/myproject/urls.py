from django.contrib import admin
from django.urls import path, include
from myapp import views

# Add imports for media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for account management
    path('guest-login/', views.guest_login, name='guest_login'),
    path('', views.entry_page, name='home_page'),
    path('book/', views.book_page, name='book_page'),
    path('court-info/<int:court_id>/', views.court_info, name='court_info'),
    path('courts-list/', views.courts_list, name='courts_list'),
    path('court-schedule/<int:court_id>/', views.court_schedule, name='court_schedule'),
    path('main/', views.main_page, name='main_page'),
    path('login-signup/', views.login_signup_page, name='login_signup_page'),
    path('book-time/<int:court_id>/', views.book_time, name='book_time'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('owner', views.court_owner_dashboard, name='court_owner_dashboard'),
    path('Notification/', views.notification_page, name='notification'),
    path('change-username/', views.change_username, name='change_username'),
    path('change-password/', views.change_password, name='change_password'),
    path('owner', views.court_owner_dashboard, name='court_owner_dashboard'),
    path('add-court/', views.add_court, name='add_court'),
    path('view-courts/', views.view_courts, name='view_courts'),
    path('settings/', views.settings_page, name='settings_page'),
    # path('owner/', views.court_owner_dashboard, name='court_owner_dashboard'),
    # path('change-profile-photo/', views.change_profile_photo, name='change_profile_photo'),  # New URL
]

