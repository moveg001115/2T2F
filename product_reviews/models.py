from django.db import models
from common.models import Common


class ProductReview(Common):
    writer = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
    )
    objectproduct = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        null=True,
        blank=True,
    )
    description = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.writer} give {self.rating}⭐ on {self.objectproduct}"
