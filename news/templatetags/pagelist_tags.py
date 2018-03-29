from django import template
from cms.models.pagemodel import Page

register = template.Library()

def cms_page_list():
    cms_pages = Page.objects.filter(published = True)
    return {'cms_pages': cms_pages}

register.inclusion_tag('includes/our-service-block.html')(cms_page_list)
