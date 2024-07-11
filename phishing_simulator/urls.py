from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Phishing Awareness Simulator")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('simulator.urls')),
    path('', index),
]
