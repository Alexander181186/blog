# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-13 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160913_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='add_tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='Тэги'),
        ),
    ]
