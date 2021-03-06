from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse


import datetime

from taggit.managers import TaggableManager
from versatileimagefield.fields import VersatileImageField


class Content(models.Model):
    title = models.CharField(_("Title"), max_length=200, unique=True)
    slug = models.SlugField(_("Slug"), max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Author"))
    content = models.TextField(_("Content"))
    photo = VersatileImageField(_("Picture"), upload_to="img/posts/", blank=True, null=True)

    published_on = models.DateField(_("Published on"), default=datetime.date.today)
    last_update = models.DateField(_("Last update"), blank=True, null=True)
    is_published = models.BooleanField(_("Is published"), default=False)

    keywords = models.CharField(_("Meta keywords"), max_length=1000, help_text="A comma-separated list of keywords. Used for Google indexing.", blank=True, null=True)
    tags = TaggableManager(blank=True)

    views = models.IntegerField(_("Views"), editable=False, default=0)

    def __unicode__(self):
        return self.title

    def get_classname(self):
        return self.__class__.__name__.lower() + 's'

    class Meta:
        ordering = ["-published_on", ]
        abstract = True


class Post(Content):
    def get_absolute_url(self):
        return reverse('post-detail', args=[self.slug])


class Project(Content):
    project_url = models.URLField(_("Project url"))
    code_url = models.URLField(_("Code url"), null=True, blank=True)

    def get_absolute_url(self):
        return reverse('project-detail', args=[self.slug])
