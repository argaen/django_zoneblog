from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import datetime

from taggit.managers import TaggableManager


class Content(models.Model):
    title = models.CharField(_("Title"), max_length=200, unique=True)
    slug = models.SlugField(_("Slug"), max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Author"))
    content = models.TextField(_("Content"))

    published_on = models.DateField(_("Published on"), default=datetime.date.today)
    is_published = models.BooleanField(_("Is published"), default=False)

    keywords = models.CharField(_("Meta keywords"), max_length=1000, help_text="A comma-separated list of keywords")
    tags = TaggableManager(blank=True)

    views = models.IntegerField(_("Views"), editable=False, default=0)

    def __str__(self):
        return self.title

    def get_classname(self):
        return self.__class__.__name__.lower() + 's'

    class Meta:
        ordering = ["-published_on", ]
        abstract = True


class Post(Content):
    def get_absolute_url(self):
        return "/posts/%s" % self.slug


class NewsItem(Content):
    def get_absolute_url(self):
        return "/news/%s" % self.slug


class Project(Content):
    template = models.CharField(_("Template"), max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return "/projects/%s" % self.slug
