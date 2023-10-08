from django.db import models
from common.models import Common


class Dib(Common):
    owner = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
    )
