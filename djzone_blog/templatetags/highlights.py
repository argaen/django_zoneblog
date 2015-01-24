from bs4 import BeautifulSoup
from django import template
from django.template.defaultfilters import stringfilter

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

register = template.Library()

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
                formatter = HtmlFormatter()
                code_hl = highlight(code, lexer, formatter)
                pre.contents = [BeautifulSoup(code_hl)]
                pre.name = 'code'

            except:
                raise

    return unicode(soup)
