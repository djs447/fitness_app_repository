from workouts.models import Workout
from notifications.models import EmailTemplate
from celery import shared_task
from notifications.utils import send_notification_email

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
        return

    if not preferences.workout_congratulations:
        return

    send_notification_email(
        user=user,
        template=congratulations_template,
        context=context
    )