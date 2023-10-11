from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "registrant",
        "product_name",
        "price",
    )
    list_filter = (
        "registrant",
        "price",
    )
