from django.db import models
from common.models import Common


class Photo(Common):
    file = models.FileField()
