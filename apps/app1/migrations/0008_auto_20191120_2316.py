# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 04:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20191118_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='locx',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='locy',
        ),
        migrations.RemoveField(
            model_name='user',
            name='locx',
        ),
        migrations.RemoveField(
            model_name='user',
            name='locy',
        ),
    ]
