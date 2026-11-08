from django.contrib import admin

from .models import (
    EmailTemplate,
    InboxMessage,
    InboxMessageTemplate,
    NotificationPreference,
)


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "subject")


class NotificationPreferenceAdmin(admin.ModelAdmin):
    list_display = ("user", "email_enabled", "sms_enabled", "inactivity_reminders")


class InboxMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "subject", "created", "modified")

    ordering = ("-created",)


class InboxMessageTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(NotificationPreference, NotificationPreferenceAdmin)
admin.site.register(InboxMessage, InboxMessageAdmin)
admin.site.register(InboxMessageTemplate, InboxMessageTemplateAdmin)
