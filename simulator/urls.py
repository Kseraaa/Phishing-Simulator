from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResponseViewSet, send_phishing_email, phishing_tracker, password_test, social_engineering_tracker, send_social_engineering

router = DefaultRouter()
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('send_phishing_email/', send_phishing_email, name='send_phishing_email'),
    path('phishing_tracker/', phishing_tracker, name='phishing_tracker'),

    path('password_test/', password_test, name='password_test'),

    path('send_social_engineering/', send_social_engineering, name='send_social_engineering'),
    path('social_engineering_tracker/', social_engineering_tracker, name='social_engineering_tracker'),

]
