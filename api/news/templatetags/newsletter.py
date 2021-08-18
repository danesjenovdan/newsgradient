from django import template

register = template.Library()

@register.filter
def base_url(url):
    if not url or not isinstance(url, str):
        return url
    slice_end = url.find('/', url.find('://') + 3)
    return url[0:slice_end]
