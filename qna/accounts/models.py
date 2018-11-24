from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    QnA User Model

    Fields:
    - Default User fields
    - handle
    """

    handle = models.CharField(max_length=100, null=True, blank=True)
