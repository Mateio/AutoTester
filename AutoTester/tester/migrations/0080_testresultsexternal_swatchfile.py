# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0079_auto_20171006_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresultsexternal',
            name='swatchFile',
            field=models.CharField(blank=True, default=None, help_text='This was the test that was run', max_length=200, null=True),
        ),
    ]
