from rest_framework import viewsets
from .models import Response
from .serializers import ResponseSerializer

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def send_phishing_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        recipient_email = data.get('email')
        
        if recipient_email:
            subject = 'ตรวจสอบบัญชีของคุณ'
            message = 'มีการเปลี่ยนแปลงในบัญชีของคุณ โปรดคลิกที่ลิงก์ด้านล่างเพื่อเข้าสู่ระบบและตรวจสอบ'
            from_email = 'your_email@example.com'
            recipient_list = [recipient_email]
            
            send_mail(subject, message, from_email, recipient_list)
            return JsonResponse({'message': 'Email sent successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Email is required'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)



class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
