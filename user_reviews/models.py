from django.db import models
from common.models import Common


class UserReview(Common):
    writer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        blank=True,
    )
