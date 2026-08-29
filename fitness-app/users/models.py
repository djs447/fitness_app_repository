from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(blank = True, null=True, max_length=32)
    bio = models.TextField(blank = True, null = True)

