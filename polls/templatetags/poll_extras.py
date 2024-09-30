import datetime

from django import template
from django.template.defaultfilters import stringfilter, linebreaksbr, urlize
from django.utils.safestring import SafeString
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
@stringfilter
def lower(value):
    return value.lower()


@register.filter(name="cut")
def cut(value, arg):
    return value.replace(arg, "")


@register.filter(is_safe=True)
def myfilter(value):
    return value


@register.filter(is_safe=True)
def add_xx(value):
    return "%sxx" % value


@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = "<strong>%s</strong>%s" % (esc(first), esc(other))
    return mark_safe(result)


@register.filter(needs_autoescape=True)
def urlize_and_linebreaks(text, autoescape=True):
    return linebreaksbr(urlize(text, autoescape=autoescape), autoescape=autoescape)


@register.filter(expects_localtime=True)
def businesshours(value):
    try:
        return 9 <= value.hour < 17
    except AttributeError:
        return ""


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


register.simple_tag(lambda x: x - 1, name="minusone")


@register.simple_tag(name="minustwo")
def some_function(value):
    return value - 2
