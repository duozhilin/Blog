from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    test = models.CharField(max_length=200)
