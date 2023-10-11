from django.db import models
from common.models import Common


class UserReview(Common):
    writer = models.ForeignKey(
        "users.User",
        on_delete=models.SET,
    )
    objectuser = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="objectuser",
    )
    review = models.TextField()
    image = models.ImageField(
        blank=True,
        null=True,
    )
    rating = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.writer} gave {self.rating}⭐ on {self.objectuser}"
