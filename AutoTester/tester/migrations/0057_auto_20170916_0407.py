# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0056_auto_20170914_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorsheetexternal',
            name='itemBeingMeasured',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
