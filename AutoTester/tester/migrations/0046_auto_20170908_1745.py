# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0045_auto_20170908_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresultsexternal',
            name='results',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
