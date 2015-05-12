from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count

from taggit.models import Tag
from bs4 import BeautifulSoup
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

import markdown

from zone_blog.models import Post, Project

register = template.Library()


@register.assignment_tag
def get_tags(model=None):
    if model:
        tags = list(Tag.objects.all())
        for t in tags:
            t.num_items = t.taggit_taggeditem_items.filter(content_type__model=model).count()
            if t.num_items != 0:
                yield t
    else:
        for x in Tag.objects.annotate(num_items=Count('taggit_taggeditem_items__content_type__model')):
            yield x


@register.filter
def markdownify(text):
    return markdown.markdown(text)


@register.assignment_tag
def get_latest_posts():
    return Post.objects.filter(is_published=True)[:3]


@register.assignment_tag
def get_latest_projects():
    return Project.objects.filter(is_published=True)[:3]


@register.filter    # Register the function as a filter
@stringfilter       # Filter expects a string as input
def highlight_code(html):

    soup = BeautifulSoup(unicode(html))     # Create beautiful soup object to access html objects
    preblocks = soup.findAll('pre')

    for pre in preblocks:

        if pre.has_key('class'):    # Check if the pre tag has the class attribute

            try:
                code = ''.join([unicode(item) for item in pre.contents])
                lexer = get_lexer_by_name(pre['class'][0])  # Get the class attribute value to identify the language
                formatter = HtmlFormatter(cssclass="sourcecode")
                code_hl = highlight(code, lexer, formatter)
                pre.contents = [BeautifulSoup(code_hl)]
                pre.name = 'precode'

            except:
                raise

    return unicode(soup)
