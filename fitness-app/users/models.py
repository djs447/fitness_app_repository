from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import BaseModel, SoftDeletableBaseModel

UNIT_SYSTEM_CHOICES = [
    ("imperial", "Imperial"),
    ("metric", "Metric")
]

class User(AbstractUser):
    pass

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Goal(SoftDeletableBaseModel):
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE, related_name="goals", blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    target_date = models.DateField()
    completion_date = models.DateField(blank=True, null=True)

class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(blank = True, null=True, max_length=32)
    bio = models.TextField(blank = True, null = True)
    unit_system = models.CharField(max_length=20, choices=UNIT_SYSTEM_CHOICES, default="metric")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.display_name

class Like(models.Model):
    user = models.ForeignKey(
       User,
       on_delete=models.CASCADE,
       related_name="workout_likes"
    )
    workout = models.ForeignKey(
        "workouts.Workout",
        on_delete=models.CASCADE,
        related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'workout'], name='unique_user_workout_like')
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} likes {self.workout}"
