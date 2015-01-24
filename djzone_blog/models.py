from django.db import models
from django.contrib.auth.models import User

import datetime

from taggit.managers import TaggableManager

class Content(models.Model):
    title = models.CharField(max_length=200, unique=True)
    published_on = models.DateField(default=datetime.date.today)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    content = models.TextField()

    slug = models.SlugField(max_length=200,blank=True)

    keywords = models.CharField("Meta keywords", max_length=1000, help_text="A comma-separated list of keywords")
    tags = TaggableManager(blank=True)

    def __unicode__(self):    #Print object's title when printing the object
        return self.title

    def get_classname(self):
        return self.__class__.__name__.lower()+'s'

    class Meta:     #Order by published_on field (newest first)
        ordering = ["-published_on", ]
        abstract = True


class Post(Content):
    commit = models.CharField(max_length=30, blank=True, null=True)
    branch = models.URLField(max_length=150, blank=True, null=True)

    def get_absolute_url(self):
        return "/contents/posts/%s" % self.slug


class NewsItem(Content):
    def get_absolute_url(self):
        return "/contents/news/%s" % self.slug


class Project(Content):
    template = models.CharField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return "/projects/%s" % self.slug
