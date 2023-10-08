from django.db import models
from common.models import Common


class Product(Common):
    registrant = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
    )
    image = models.ForeignKey(
        "photos.Photo",
        on_delete=models.SET_NULL,
    )
