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
    path('login-signup/', views.login_signup_page, name='login_signup_page'),
 
    path('book-time/', views.book_time, name='book_time'),

]