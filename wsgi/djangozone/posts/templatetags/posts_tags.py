from django import template
from posts.models import Post

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
def get_latest_posts(num=10):
    posts = ""
    for post in Post.objects.all()[:num]:
        posts += "<h4><a href=%s>%s</a></h4>" % (post.get_absolute_url(), post)

    return posts

