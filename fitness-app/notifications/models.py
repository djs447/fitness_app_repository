from django.db import models
from django.conf import settings

class NotificationPreference(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notification_preferences")

    email_enabled = models.BooleanField(default=True)
    sms_enabled = models.BooleanField(default=False)

    workout_congratulations = models.BooleanField(default=True)
    inactivity_reminders = models.BooleanField(default=True)

    reminder_sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Notification preferences for {self.user}"

class EmailTemplate(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    html_body = models.TextField()
    text_body = models.TextField()

    def __str__(self):
        return self.name
