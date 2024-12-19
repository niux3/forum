from django import template
from django.utils.safestring import mark_safe
from markdown import markdown


register = template.Library()

@register.filter(name="markdown")
def markdown_format(txt):
    return mark_safe(markdown(txt, extensions=['extra']))
