# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_page_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
    ]
