# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-17 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('meta_description', models.CharField(max_length=350)),
                ('image', models.ImageField(upload_to='news')),
                ('body', djangocms_text_ckeditor.fields.HTMLField()),
            ],
        ),
    ]
