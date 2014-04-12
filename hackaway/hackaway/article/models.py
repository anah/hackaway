from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from hackaway.tag.constants import LANGUAGES, DEFAULT_LANGUAGE
from hackaway.tag.models import Tag


class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=50)
    text = models.TextField()
    published = models.DateTimeField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    omni_id = models.CharField(max_length=50)

    language = models.CharField(max_length=2, choices=LANGUAGES,
                                default=DEFAULT_LANGUAGE)
    tag = models.ManyToManyField(Tag)

    def add_tags(self, tag_names):
        for tag_name in tag_names:
            try:
                tag = Tag.objects.get(name=tag_name,
                                      language=DEFAULT_LANGUAGE)
            except ObjectDoesNotExist:
                tag = Tag()
                tag.name = tag_name
                tag.language = DEFAULT_LANGUAGE
                tag.save()
            self.tag.add(tag)
            self.save()
