# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-18 22:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20191118_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='pickup',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='pickup',
            name='item',
        ),
        migrations.RemoveField(
            model_name='pickup',
            name='user',
        ),
        migrations.RemoveField(
            model_name='truck',
            name='driver',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Pickup',
        ),
        migrations.DeleteModel(
            name='Truck',
        ),
    ]
