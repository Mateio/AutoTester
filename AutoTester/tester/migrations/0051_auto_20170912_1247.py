# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0050_auto_20170912_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testschedule',
            name='testToSchedule',
            field=models.CharField(max_length=40),
        ),
    ]
