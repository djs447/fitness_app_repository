from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import BaseModel


class User(AbstractUser):
    pass

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(blank = True, null=True, max_length=32)
    bio = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.display_name
