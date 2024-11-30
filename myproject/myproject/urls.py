from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('guest-login/', views.guest_login, name='guest_login'),
    path('', views.entry_page, name='home_page'),
    path('book/', views.book_page, name='book_page'),
    path('court-info/<int:court_id>/', views.court_info, name='court_info'),
    path('courts-list/', views.courts_list, name='courts_list'),
    path('court-schedule/', views.court_schedule, name='court_schedule'),
    path('main/', views.main_page, name='main_page'),
    path('admin-login-signup/', views.admin_login_signup, name='admin_login_signup'),
    path('player-login-signup/', views.player_login_signup, name='player_login_signup'),
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
]