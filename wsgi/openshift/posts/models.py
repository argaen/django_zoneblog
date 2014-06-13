from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    published_on = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    tags = models.CharField(max_length=500)
    content = models.TextField()

    commit = models.URLField(max_length=300, blank=True, null=True)
    branch = models.URLField(max_length=150, blank=True, null=True)
    tag = models.URLField(max_length=150, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/posts/%d" % self.id

    class Meta:
        ordering = ["published_on", ]

