from common.models import BaseModel, SoftDeletableBaseModel
from django.db import models
from localflavor.us.models import USStateField
from users.models import User
from workouts.constants import WorkoutActivityChoices, WorkoutDifficultyChoices


class Workout(SoftDeletableBaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="workouts", blank=True, null=True
    )
    activity_type = models.CharField(
        choices=WorkoutActivityChoices, blank=True, null=True
    )
    started_at = models.DateTimeField()
    duration = models.DurationField()
    distance = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )  # Meters
    elevation = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )  # Meters

    title = models.CharField(
        max_length=200, blank=True, null=True
    )  # TODO Add default value to "User.name activity_type date"
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    state = USStateField(blank=True, null=True)
    difficulty = models.CharField(
        choices=WorkoutDifficultyChoices, blank=True, null=True
    )

    source_file = models.CharField(max_length=255, blank=True, null=True, unique=True)
    source_file_hash = models.CharField(
        max_length=64, blank=True, null=True, unique=True
    )

    def __str__(self):
        return f"{self.activity_type} - {self.title}"

    @property
    def average_pace(self):
        if not self.distance or not self.duration:
            return 0

        distance = float(self.distance)
        duration_seconds = self.duration.total_seconds()

        if self.activity_type == "running":
            return duration_seconds * 1000 / (distance * 60)  # min / km
        elif self.activity_type == "cycling":
            return distance / 1000 / duration_seconds * 3600  # km/h
        elif self.activity_type == "swimming":
            return duration_seconds * 100 / (distance * 60)  # min / 100m

        return 0

    @property
    def heart_rate(self):
        if not self.samples.exists():
            return None
        return self.samples.aggregate(models.Avg("heart_rate"))["heart_rate__avg"]


class WorkoutSample(BaseModel):
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="samples"
    )
    timestamp = models.DateTimeField()

    heart_rate = models.PositiveSmallIntegerField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    cadence = models.PositiveSmallIntegerField(null=True, blank=True)
    power = models.PositiveSmallIntegerField(null=True, blank=True)
    elevation = models.FloatField(null=True, blank=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["workout", "timestamp"], name="unique_workout_timestamp"
            )
        ]

    def __str__(self):
        return f"{self.workout} - {self.timestamp}"


class Comment(SoftDeletableBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()

    def __str__(self):
        return f"{self.workout} - {self.content[:50]}..."
