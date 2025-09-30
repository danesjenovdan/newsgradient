from django import template

register = template.Library()

@register.filter
def base_url(url):
    if not url or not isinstance(url, str):
        return url
    slice_end = url.find('/', url.find('://') + 3)
    return url[0:slice_end]

@register.filter
def favicon_url(url):
    if not url or not isinstance(url, str):
        return 'https://www.google.com/s2/favicons?sz=32&domain_url=https://does.not.exist.newsgradient-pwa.lb.djnd.si'
    return f'https://www.google.com/s2/favicons?sz=32&domain_url={base_url(url)}'
