import json, smtplib
from rest_framework import viewsets
from .models import Response, PhishingResult
from .serializers import ResponseSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@csrf_exempt
def send_phishing_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        to_email = data.get('email')
        if not to_email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        subject = 'Phishing Awareness Test'
        body = f'This is a phishing awareness test email. <br><br> <img src="http://127.0.0.1:8000/phishing_tracker/?email={to_email}" width="1" height="1"> <br><br> Click <a href="http://127.0.0.1:8000/phishing_tracker/?email={to_email}&clicked=true">here</a> to verify.'

        from_email = 'thanapat0918618713@gmail.com'
        app_password = 'hunn mgnl jeyh erja'

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

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

@csrf_exempt
def log_phishing_result(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        opened = data.get('opened', False)
        clicked = data.get('clicked', False)

        result = PhishingResult(email=email, opened=opened, clicked=clicked)
        result.save()

        return JsonResponse({'message': 'Result logged successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def phishing_tracker(request):
    email = request.GET.get('email')
    clicked = request.GET.get('clicked', False)

    if email:
        result = PhishingResult.objects.filter(email=email).first()
        if result:
            if clicked:
                result.clicked = True
            else:
                result.opened = True
            result.save()
        else:
            PhishingResult.objects.create(email=email, opened=not clicked, clicked=clicked)

    return JsonResponse({'message': 'Tracking recorded'})

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
