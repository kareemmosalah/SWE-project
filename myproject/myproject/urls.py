from django.shortcuts import render
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return render(request, 'index.html')  # React app's entry point

urlpatterns = [
    # API routes go here, e.g., path('api/', include('api.urls'))
    path('', index),  # Serve React app for root URL
    re_path(r'^(?!api/).*$', index),  # Serve React app for all other routes except API
    path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)