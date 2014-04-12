from django.db import models

from .constants import LANGUAGES


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
