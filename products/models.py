from django.db import models
from common.models import Common


class Product(Common):
    registrant = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        blank=True,
    )
