from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from simulator.views import get_analysis_Phishing, send_social_engineering, phishing_tracker, send_phishing_email, get_analysis_social_engineering, social_engineering_tracker

def index(request):
    return HttpResponse("Welcome to the Phishing Awareness Simulator")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('simulator.urls')),

    path('send_phishing_email/', send_phishing_email, name='send_phishing_email'),
    path('phishing_tracker/', phishing_tracker, name='phishing_tracker'),
    path('api/analysis_Phishing/', get_analysis_Phishing),


    path('send_social_engineering/', send_social_engineering, name='send_social_engineering'),
    path('social_engineering_tracker/', social_engineering_tracker, name='social_engineering_tracker'),
    path('api/analysis_social_engineering/', get_analysis_social_engineering),

    path('', index),
]
