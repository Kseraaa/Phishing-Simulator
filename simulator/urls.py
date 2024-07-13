from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResponseViewSet, send_phishing_email, phishing_tracker, get_analysis_data

router = DefaultRouter()
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('send_phishing_email/', send_phishing_email, name='send_phishing_email'),
]
