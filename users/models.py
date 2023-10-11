from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User Model Definition"""

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class UserKindChoices(models.TextChoices):
        CLIENT = ("client", "Client")
        PRODUCER = ("producer", "Producer")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    avatar = models.ImageField(
        blank=True,
        null=True,
    )
    password = models.CharField(
        max_length=200,
    )
    email = models.CharField(
        max_length=150,
    )
    birth = models.CharField(
        max_length=8,
    )
    nickname = models.CharField(
        max_length=100,
    )
    gender = models.CharField(
        max_length=6,
        choices=GenderChoices.choices,
    )
    phone_num = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    user_kind = models.CharField(
        max_length=8,
        choices=UserKindChoices.choices,
    )
    location = models.CharField(
        max_length=100,
    )
