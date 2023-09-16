from django import template

register = template.Library()


@register.filter(name='has_logo')
def has_logo(logo):
    try:
        return bool(logo.url)
    except ValueError:
        return False

@register.simple_tag
def set_xs(val=None):
    return val

@register.simple_tag
def set_sm(val=None):
    return val

@register.simple_tag
def set_md(val=None):
    return val

@register.simple_tag
def set_lg(val=None):
    return val
