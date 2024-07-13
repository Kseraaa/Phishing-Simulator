from django.contrib import admin
from .models import PhishingAttempt

class PhishingAttemptAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp', 'clicked')

admin.site.register(PhishingAttempt, PhishingAttemptAdmin)
