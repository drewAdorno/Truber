# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-18 14:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20191113_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]
