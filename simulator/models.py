from django.db import models

class Response(models.Model):
    user_info = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_info
