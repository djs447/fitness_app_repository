from django.db import models
from common.models import BaseModel, SoftDeletableBaseModel
from workouts.constants import WorkoutActivityChoices
from users.models import User

class Workout(SoftDeletableBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts", blank=True, null=True)
    activity_type = models.CharField(choices=WorkoutActivityChoices, blank=True, null=True)
    started_at = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return f"{self.user.full_name} - {self.activity_type}"

class WorkoutSample(BaseModel):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="samples")
    timestamp = models.DateTimeField()

    heart_rate = models.PositiveSmallIntegerField()
    speed = models.FloatField()
    cadence = models.PositiveSmallIntegerField()
    power = models.PositiveSmallIntegerField()
    elevation = models.FloatField()

    def __str__(self):
        return f"{self.workout} - {self.timestamp}"