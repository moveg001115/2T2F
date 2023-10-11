from django.db import models
from common.models import Common


class Dib(Common):
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="dibowner",
    )
    favorites = models.ManyToManyField(
        "users.User",
        related_name="dibfavorites",
    )

    def __str__(self) -> str:
        return f"{self.owner}'s Dib"
