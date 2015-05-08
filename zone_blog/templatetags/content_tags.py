from django import template

from taggit.models import Tag

import markdown

register = template.Library()


@register.assignment_tag
def get_tags():
    return Tag.objects.all()


@register.filter
def markdownify(text):
    return markdown.markdown(text)
