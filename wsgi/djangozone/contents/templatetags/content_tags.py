from django import template
from contents.models import Content, Post, NewsItem, Project

from operator import attrgetter
from itertools import chain

import os
import markdown

register = template.Library()

@register.simple_tag
def get_tags(tags, url=None):
    ret_tags = []
    for tag in tags:
        head = "<a href=%s>#" % os.path.join(url, tag) if url else ''
        tail = "</a>" if url else ''
        ret_tags.append(head+str(tag)+tail)
    return ', '.join(ret_tags)


@register.simple_tag
def get_latest_contents(num=5):
    contents_list = sorted(
            chain(Post.objects.filter(published=True),
                NewsItem.objects.filter(published=True),
                Project.objects.filter(published=True)),
            key=attrgetter('published_on'), reverse=True)
    contents = ""
    for c in contents_list[:num]:
        contents += "<li><i class='fa-li fa fa-angle-right'></i> <a href=%s>%s</a></li>" % (c.get_absolute_url(), c)

    return contents
