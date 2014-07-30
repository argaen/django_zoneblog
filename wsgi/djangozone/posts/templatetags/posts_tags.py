from django import template

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
