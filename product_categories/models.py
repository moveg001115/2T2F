from django.db import models
from common.models import Common


class ProductCategory(Common):
    name = models.CharField(
        max_length=50,
    )

    class Meta:
        verbose_name_plural = "product categories"

    def __str__(self) -> str:
        return self.name
