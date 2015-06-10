from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from taggit.models import Tag
import datetime

from models import Post


class LatestPostsFeed(Feed):
    title = "Django Zone latests posts"
    link = "/"
    description_template = 'content_description.html'
    item_enclosure_mime_type = "image/jpeg"

    def items(self):
        return Post.objects.filter(is_published=True)

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return datetime.datetime.combine(item.published_on, datetime.time())

    def item_enclosure_url(self, item):
        return "http://django.zone/" + item.photo.url if item.photo else ''

    # If models don't have get_absolute_url method, override item_link
    # def item_link(self, item):
        # return reverse('post-item', args=[item.pk])


class TagFeed(Feed):
    description_template = 'content_description.html'
    item_enclosure_mime_type = "image/jpeg"

    def get_object(self, request, tag):
        return get_object_or_404(Tag, name=tag)

    def title(self, obj):
        return "Django Zone: %s posts" % obj.name

    def link(self, obj):
        return reverse('post-list-tag', args=[obj.name])

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return datetime.datetime.combine(item.published_on, datetime.time())

    def items(self, obj):
        return Post.objects.filter(is_published=True, tags__name=obj)

    def item_enclosure_url(self, item):
        return "http://django.zone/" + item.photo.url if item.photo else ''
