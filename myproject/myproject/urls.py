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
    path('admin-login-signup/', views.admin_login_signup, name='admin_login_signup'),  # Admin login/signup URL
    path('player-login-signup/', views.player_login_signup, name='player_login_signup'),  # Player login/signup URL
    path('login/', views.login_page, name='login_page'),  # Login page URL
    path('book-time/<int:court_id>/', views.book_time, name='book_time'),  # Book time URL with court_id parameter
    path('signup/', views.signup_page, name='signup_page'),  # Signup page URL
    path('owner', views.court_owner_page, name='court_owner_page'),  # Court owner page URL
    path('user-profile/', views.user_profile, name='user_profile'),
    path('owner', views.court_owner_dashboard, name='court_owner_dashboard'),
    # path('Notification/' , views.index , name='Notify'),
    # path('send/' , views.send),
    # path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js")  # User profile page URL
]