from django.db import models
from django.contrib.auth.models import User

import datetime

from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=200)
    published_on = models.DateField(default=datetime.date.today)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    content = models.TextField()

    tags = TaggableManager()

    commit = models.CharField(max_length=30, blank=True, null=True)
    branch = models.URLField(max_length=150, blank=True, null=True)

    def __unicode__(self):    #Print object's title when printing the object
        return self.title

    def get_absolute_url(self):     #Return the url of the object
        return "/posts/%d" % self.id

    class Meta:     #Order by published_on field (newest first)
        ordering = ["-published_on", ]
