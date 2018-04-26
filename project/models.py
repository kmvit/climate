from django.db import models
import datetime
from djangocms_text_ckeditor.fields import HTMLField
# Create your models here.

class CategoryProject(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    class Meta:
        verbose_name='Категория проекта'
        verbose_name_plural = 'Категории Проекта'

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(CategoryProject, verbose_name='Категория')
    image = models.ImageField(upload_to='project', verbose_name='Изображение')
    created = models.DateField(auto_now_add=True)
    meta_description = models.CharField(max_length=350)
    content = HTMLField()

    class Meta:
        verbose_name='Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title
