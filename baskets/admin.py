from django.contrib import admin
from .models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass
