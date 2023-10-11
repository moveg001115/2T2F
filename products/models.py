from django.db import models
from common.models import Common


class Product(Common):
    registrant = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    product_kind = models.ForeignKey(
        "product_categories.ProductCategory",
        null=True,
        on_delete=models.SET_NULL,
    )
    image = models.ImageField(
        blank=True,
    )
    product_name = models.CharField(
        max_length=150,
    )
    title = models.CharField(
        max_length=300,
    )
    content = models.TextField(
        default="",
    )
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.registrant}'s outsourcing : {self.product_name}({self.product_kind})"
