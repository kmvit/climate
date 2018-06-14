from django.contrib import admin
from .models import *
# Register your models here.
class CategoryProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(CategoryProject, CategoryProjectAdmin)
admin.site.register(Project)
