from django import template
from cms.models.pagemodel import Page
from project.models import Project

register = template.Library()

def cms_page_list():
    cms_pages = Page.objects.filter(published = True)
    return {'cms_pages': cms_pages}
    register.inclusion_tag('includes/our-service-block.html')(cms_page_list)

@register.inclusion_tag('includes/project_list.html', takes_context=True)
def project_list_tags(context):
    project_list = Project.objects.all()
    context_dict = {'project_list':project_list}
    return context_dict
