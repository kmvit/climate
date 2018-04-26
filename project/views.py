from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *
# Create your views here.

class ProjectList(ListView):
    model = Project
    template_name = "projects.html"
    context_name = 'project_list'

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        context['category_list'] = CategoryProject.objects.all()
        return context

class ProjectDetail(DetailView):
    model = Project
