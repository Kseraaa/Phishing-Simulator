from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from simulator.views import phishing_tracker, get_analysis_data

def index(request):
    return HttpResponse("Welcome to the Phishing Awareness Simulator")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('simulator.urls')),
    path('phishing_tracker/', phishing_tracker, name='phishing_tracker'),
    path('api/analysis/', get_analysis_data),
    path('', index),
]
