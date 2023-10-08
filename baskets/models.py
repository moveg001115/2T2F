from django.db import models
from common.models import Common


class Basket(Common):
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    products = models.ManyToManyField(
        "products.Product",
    )
