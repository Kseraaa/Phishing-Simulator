from rest_framework import viewsets
from .models import Response
from .serializers import ResponseSerializer

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

@csrf_exempt
def send_phishing_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        to_email = data.get('email')
        if not to_email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        subject = 'Phishing Awareness Test'
        body = 'ไอพวกโง่เตรียมโดนกูหลอก.'
        from_email = 'thanapat0918618713@gmail.com'
        app_password = 'hunn mgnl jeyh erja'  # รหัสผ่านสำหรับแอปหลังจาก2factor

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, app_password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            return JsonResponse({'message': 'Email sent successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
