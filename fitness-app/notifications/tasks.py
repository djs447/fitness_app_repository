import logging
from datetime import timedelta

from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone
from fitness_app.settings import DEFAULT_INACTIVITY_CADENCE_IN_DAYS
from notifications.models import (
    EmailTemplate,
    InboxMessage,
    InboxMessageTemplate,
    NotificationPreference,
)
from notifications.utils import send_notification_email
from workouts.models import Workout

logger = logging.getLogger(__name__)


@shared_task
def send_workout_congratulations(workout_id, template_name="Workout Congratulations"):

    workout = Workout.objects.select_related("user").get(id=workout_id)

    user = workout.user
    preferences = getattr(user, "notification_preferences", None)
    congratulations_template = EmailTemplate.objects.get(name=template_name)
    context = {
        "username": user.username,
        "workout": workout,
    }

    if not preferences:
        logger.info(
            "User %s has no notification preferences, skipping workout "
            "congratulations notification.",
            user.id,
        )
        return

    if not preferences.workout_congratulations:
        logger.info(
            "User %s has disabled workout congratulations notifications.", user.id
        )
        return

    send_notification_email(
        user=user, template=congratulations_template, context=context
    )


@shared_task
def send_inactivity_reminders(template_name="Inactivity Reminders"):

    cutoff_date = timezone.now() - timedelta(days=DEFAULT_INACTIVITY_CADENCE_IN_DAYS)

    inactivity_template = EmailTemplate.objects.get(name=template_name)

    preferences_list = NotificationPreference.objects.filter(
        inactivity_reminders=True
    ).select_related("user")

    for preferences in preferences_list.iterator():
        user = preferences.user

        last_workout = Workout.objects.filter(user=user).order_by("-started_at").first()

        if not last_workout:
            continue

        if last_workout and last_workout.started_at >= cutoff_date:
            continue

        if preferences.reminder_sent_at and preferences.reminder_sent_at >= cutoff_date:
            continue

        context = {
            "username": user.username,
        }

        email_sent = send_notification_email(
            user=user, template=inactivity_template, context=context
        )

        if email_sent:
            preferences.reminder_sent_at = timezone.now()
            preferences.save()


@shared_task
def send_inbox_message_notification(
    user_id, workout_id, sent_by_id, template_name="Inbox Message Notification"
):

    logger.info(
        "Sending inbox notification for user_id=%s, workout_id=%s, sent_by_id=%s",
        user_id,
        workout_id,
        sent_by_id,
    )

    user = get_user_model().objects.select_related("profile").get(id=user_id)
    workout = Workout.objects.select_related("user").get(id=workout_id)

    inbox_message_template = InboxMessageTemplate.objects.get(name=template_name)

    display_name = user.profile.display_name

    preferences = getattr(user, "notification_preferences", None)
    context = {
        "display_name": display_name,
        "workout": workout,
    }

    if not preferences:
        logger.info(
            "User %s has no notification preferences, skipping inbox notification.",
            user_id,
        )
        return

    sent_by = get_user_model().objects.get(id=sent_by_id)

    inbox_message = InboxMessage.objects.create(
        user=user,
        workout_id=workout_id,
        subject="Sharing a Workout",
        message=inbox_message_template.text_body.format(**context),
        sent_by=sent_by,
    )

    if inbox_message:
        logger.info(
            "Inbox message created for user_id=%s, workout_id=%s, sent_by_id=%s",
            user_id,
            workout_id,
            sent_by_id,
        )
    else:
        logger.error(
            "Failed to add inbox message for user_id=%s, workout_id=%s, sent_by_id=%s",
            user_id,
            workout_id,
            sent_by_id,
        )
