from django.db import models
from common.models import Common


class UserReview(Common):
    writer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    image = models.ForeignKey(
        "photos.Photo",
        on_delete=models.SET_NULL,
    )
