from django.db import models

class Response(models.Model):
    user_info = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_info
    
#ใช้ติดตามผล เช่น ใครเปิดอีเมล 
class PhishingResult(models.Model):
    email = models.EmailField()
    opened = models.BooleanField(default=False)
    clicked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class PhishingAttempt(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    clicked = models.BooleanField(default=False)

    def __str__(self):
        return self.email
