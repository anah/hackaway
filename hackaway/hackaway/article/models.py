from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=225)
    category = models.CharField(max_length=225)
    author = models.CharField(max_length=50)
    text = models.TextField()
    published = models.DateTimeField()

