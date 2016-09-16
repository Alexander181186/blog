# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-14 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160913_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]