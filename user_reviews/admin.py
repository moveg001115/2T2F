from django.contrib import admin
from .models import UserReview


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    list_filter = ("writer",)
