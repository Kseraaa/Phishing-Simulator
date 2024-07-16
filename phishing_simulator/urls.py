from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from simulator.views import get_analysis_data, send_social_engineering, phishing_tracker, send_phishing_email

def index(request):
    return HttpResponse("Welcome to the Phishing Awareness Simulator")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('simulator.urls')),
    path('api/analysis/', get_analysis_data),

    path('send_phishing_email/', send_phishing_email, name='send_phishing_email'),
    path('phishing_tracker/', phishing_tracker, name='phishing_tracker'),

    path('send_social_engineering/', send_social_engineering, name='send_social_engineering'),
    path('social_engineering_tracker/', send_social_engineering, name='social_engineering_tracker'),

    path('', index),
]
