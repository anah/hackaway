from django.db import models

from hackaway.tag.constants import LANGUAGES


class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    text = models.TextField()
    published = models.DateTimeField()
    image_url = models.URLField(null=True, blank=True)

    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    tag = models.ManyToManyField("self")
