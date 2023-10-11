from django.contrib import admin
from .models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("owner",)
    list_filter = ("owner",)
