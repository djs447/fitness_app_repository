from common.models import SoftDeletableBaseModel
from django.conf import settings
from django.db import models


class NotificationPreference(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notification_preferences",
    )

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


class InboxMessage(SoftDeletableBaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inbox_messages",
    )
    workout_id = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_inbox_messages",
    )

    def __str__(self):
        return f"Inbox message for {self.user} about workout {self.workout_id}"


class InboxMessageTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    text_body = models.TextField()

    def __str__(self):
        return self.name
