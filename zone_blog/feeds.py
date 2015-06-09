from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from taggit.models import Tag

from models import Post


class LatestPosts(Feed):
    title = "Django Zone latests posts"
    link = "/"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    # If models don't have get_absolute_url method, override item_link
    # def item_link(self, item):
        # return reverse('post-item', args=[item.pk])


class Category(Feed):

    def get_object(self, request, tag):
        return get_object_or_404(Tag, name=tag)

    def title(self, obj):
        return "Django Zone: %s posts" % obj.name

    def link(self, obj):
        return reverse('post-list-tag', args=[obj.name])

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def items(self, obj):
        return Post.objects.filter(is_published=True, tags__name=obj)
