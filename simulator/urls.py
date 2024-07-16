from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResponseViewSet, send_phishing_email, phishing_tracker, password_test

router = DefaultRouter()
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('send_phishing_email/', send_phishing_email, name='send_phishing_email'),
    path('phishing_tracker/', phishing_tracker, name='phishing_tracker'),
    path('password_test/', password_test, name='password_test'),
]
