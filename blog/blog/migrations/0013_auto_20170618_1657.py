# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-18 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='vid',
            field=models.URLField(default='http://test.com'),
        ),
    ]