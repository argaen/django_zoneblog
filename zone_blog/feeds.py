from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from taggit.models import Tag

from models import Post


class LatestPosts(Feed):
    title = "Django Zone latests posts"
    link = "/"
    description_template = 'content_description.html'

    def items(self):
        return Post.objects.filter(is_published=True)

    def item_title(self, item):
        return item.title

    # If models don't have get_absolute_url method, override item_link
    # def item_link(self, item):
        # return reverse('post-item', args=[item.pk])


class Category(Feed):
    description_template = 'content_description.html'

    def get_object(self, request, tag):
        return get_object_or_404(Tag, name=tag)

    def title(self, obj):
        return "Django Zone: %s posts" % obj.name

    def link(self, obj):
        return reverse('post-list-tag', args=[obj.name])

    def item_title(self, item):
        return item.title

    def items(self, obj):
        return Post.objects.filter(is_published=True, tags__name=obj)
