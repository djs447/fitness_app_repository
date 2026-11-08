from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template

from .models import EmailTemplate


def send_notification_email(user, template: EmailTemplate, context=None):

    if not user.email:
        return False

    preferences = getattr(user, "notification_preferences", None)

    if not preferences or not preferences.email_enabled:
        return False

    if not template:
        return False

    html_content = Template(template.html_body).render(Context(context))
    text_content = Template(template.text_body).render(Context(context))

    email = EmailMultiAlternatives(
        subject=template.subject,
        body=text_content,
        from_email=None,
        to=[user.email],
    )
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)

    return True
