# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-11 18:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170611_1740'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vkladki',
            new_name='Inserts',
        ),
    ]