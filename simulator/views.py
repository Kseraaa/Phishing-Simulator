import json, smtplib, re
from rest_framework import viewsets
from .models import Response, PhishingResult
from .serializers import ResponseSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from .models import PhishingAttempt, SocialEngineerAttempt

@csrf_exempt
def send_phishing_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        to_email = data.get('email')
        if not to_email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        subject = 'Gift Voucher Reward'
        body = f'ยินดีด้วยคุณได้รับรางวัล.<br><br> ถึงผู้ใช้บัญชี {to_email} คุณได้รับรางวัลเป็น Gift Voucher สำหรับใช้จ่ายทุกห้างสรรพสินค้า เช่น Cetral, Lotus เป็นต้น <br> กรุณากรอกข้อมูลภายใน 3 วัน หลังจากได้รับอีเมลเพื่อเป็นการยืนยันสิทธิ เนื่องจากของรางวัลมีจำนวนจำกัด<br> หากท่านไม่ยืนยันสิทธิในเวลา ทางบริษัทขอสงวนสิทธิให้ผู้โชคดีท่านถัดไปทุกกรณี<br><br>  <a href="http://127.0.0.1:8000/phishing_tracker/?email={to_email}&clicked=true">ยืนยันสิทธิ</a>.'
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

def password_strength(password):
    if len(password) < 8:
        return 'Very Weak'
    
    # Check for presence of digits
    if not re.search(r"\d", password):
        return 'Weak'

    # Check for presence of uppercase letters
    if not re.search(r"[A-Z]", password):
        return 'Weak'

    # Check for presence of lowercase letters
    if not re.search(r"[a-z]", password):
        return 'Weak'

    # Check for presence of special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return 'Moderate'

    if len(password) >= 12:
        return 'Strong'

    return 'Moderate'

@csrf_exempt
def password_test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        password = data.get('password')
        if not password:
            return JsonResponse({'error': 'Password is required'}, status=400)
        
        strength = password_strength(password)
        return JsonResponse({'strength': strength})

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def send_social_engineering(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        to_email = data.get('email')
        if not to_email:
            return JsonResponse({'error': 'Email is required'}, status=400)

        subject = 'Gift Voucher Reward'
        body = f'ยินดีด้วยคุณได้รับรางวัล.<br><br> ถึงผู้ใช้บัญชี {to_email} คุณได้รับรางวัลเป็น Gift Voucher สำหรับใช้จ่ายทุกห้างสรรพสินค้า เช่น Cetral, Lotus เป็นต้น <br> กรุณากรอกข้อมูลภายใน 3 วัน หลังจากได้รับอีเมลเพื่อเป็นการยืนยันสิทธิ เนื่องจากของรางวัลมีจำนวนจำกัด<br> หากท่านไม่ยืนยันสิทธิในเวลา ทางบริษัทขอสงวนสิทธิให้ผู้โชคดีท่านถัดไปทุกกรณี<br><br>  <a href="http://127.0.0.1:8000/social_engineer_tracker/?email={to_email}&clicked=true">ยืนยันสิทธิ</a>.'
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
            attempt = SocialEngineerAttempt(email=to_email, clicked=False)
            attempt.save()

            return JsonResponse({'message': 'Email sent successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def social_engineering_tracker(request):
    email = request.GET.get('email')
    clicked = request.GET.get('clicked')
    if email and clicked:
        attempts = SocialEngineerAttempt.objects.filter(email=email)
        if attempts.exists():
            attempts.update(clicked=True)
            return JsonResponse({'email': email, 'clicked': 'true'})
        else:
            return JsonResponse({'error': 'Email not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
