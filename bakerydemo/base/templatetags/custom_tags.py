from django import template

register = template.Library()


@register.filter(name='has_logo')
def has_logo(logo):
    try:
        return bool(logo.url)
    except ValueError:
        return False
