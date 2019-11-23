# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-22 04:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0012_auto_20191121_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('distanceTraveled', models.IntegerField(default=0)),
                ('driverAccepted', models.BooleanField(default=0)),
                ('completed', models.BooleanField(default=0)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Driver')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User')),
            ],
        ),
    ]
