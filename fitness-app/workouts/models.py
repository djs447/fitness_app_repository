from django.db import models
from workouts.constants import WorkoutActivityChoices
from users.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts", blank=True, null=True)
    activity_type = models.CharField(choices=WorkoutActivityChoices, blank=True, null=True)
    started_at = models.DateTimeField()
    duration = models.DurationField()

class WorkoutSample(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="samples")
    timestamp = models.DateTimeField()

    heart_rate = models.PositiveSmallIntegerField()
    speed = models.FloatField()
    cadence = models.PositiveSmallIntegerField()
    power = models.PositiveSmallIntegerField()
    elevation = models.FloatField()