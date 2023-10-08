from django.contrib import admin
from .models import UserReview


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    pass
