from django.db import models
import datetime
from djangocms_text_ckeditor.fields import HTMLField
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created = models.DateField(auto_now_add=True)
    meta_description = models.CharField(max_length=350)
    image = models.ImageField(upload_to='news')
    body = HTMLField()
