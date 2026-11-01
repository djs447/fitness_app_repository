from django.contrib import admin

from .models import EmailTemplate, NotificationPreference

class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "subject")

class NotificationPreferenceAdmin(admin.ModelAdmin):
    list_display = ("user", "email_enabled", "sms_enabled", "inactivity_reminders", "inactivity_cadence")

admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(NotificationPreference, NotificationPreferenceAdmin)
