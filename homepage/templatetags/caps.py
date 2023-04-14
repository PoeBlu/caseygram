from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def upper(value):
    return value.split(',')[0].upper() + ' AGO' if ',' in value else value.upper()


upper.is_safe = True
