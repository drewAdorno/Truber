# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_driver_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='lat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='driver',
            name='lng',
            field=models.IntegerField(default=0),
        ),
    ]
