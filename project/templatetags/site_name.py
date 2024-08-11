from django import template
from django.contrib.sites.models import Site

register = template.Library()

@register.simple_tag
def get_site_name():
    # return Site.objects.get_current().name
    return "WebTank"
