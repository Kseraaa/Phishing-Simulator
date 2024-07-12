import json, smtplib
from rest_framework import viewsets
from .models import Response, PhishingResult
from .serializers import ResponseSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from .models import PhishingAttempt

@csrf_exempt
def send_phishing_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        to_email = data.get('email')
        if not to_email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        subject = 'Phishing Simulator Test'
        body = f'This is a phishing awareness test email. <br><br> <img src="http://127.0.0.1:8000/phishing_tracker/?email={to_email}" width="1" height="1"> <br><br> Click <a href="http://127.0.0.1:8000/phishing_tracker/?email={to_email}&clicked=true">here</a> to verify.'

        from_email = 'service.rewards.Inc@gmail.com'
        app_password = 'fdpc xfze entn ygbp'

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
            
            # Save email to database
            attempt = PhishingAttempt(email=to_email, clicked=False)
            attempt.save()

            return JsonResponse({'message': 'Email sent successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def phishing_tracker(request):
    email = request.GET.get('email')
    clicked = request.GET.get('clicked')
    if email and clicked:
        attempts = PhishingAttempt.objects.filter(email=email)
        if attempts.exists():
            attempts.update(clicked=True)
            return JsonResponse({'email': email, 'clicked': 'true'})
        else:
            return JsonResponse({'error': 'Email not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_analysis_data(request):
    total_emails_sent = PhishingAttempt.objects.count()
    emails_clicked = PhishingAttempt.objects.filter(clicked=True).count()
    response_data = {
        'total_emails_sent': total_emails_sent,
        'emails_clicked': emails_clicked,
        'click_rate': emails_clicked / total_emails_sent * 100 if total_emails_sent > 0 else 0
    }
    return JsonResponse(response_data)

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
