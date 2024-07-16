from django.contrib import admin
from .models import PhishingAttempt, SocialEngineerAttempt

class PhishingAttemptAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp', 'clicked')

admin.site.register(PhishingAttempt, PhishingAttemptAdmin)

class SocialEngineerAttemptAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp', 'clicked')

admin.site.register(SocialEngineerAttempt, SocialEngineerAttemptAdmin)
