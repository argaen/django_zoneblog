from django import template
from contents.models import Post, NewsItem

import os

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
def get_latest_posts(num=5):
    posts = ""
    for post in Post.objects.all()[:num]:
        posts += "<h4><span class='glyphicon glyphicon-book'></span> <a href=%s>%s</a></h4>" % (post.get_absolute_url(), post)

    return posts


@register.simple_tag
def get_latest_news(num=5):
    news = ""
    for n in NewsItem.objects.all()[:num]:
        news += "<h4><span class='glyphicon glyphicon-info-sign'></span> <a href=%s>%s</a></h4>" % (n.get_absolute_url(), n)

    return news
