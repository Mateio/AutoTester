# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0025_jobentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobentry',
            name='jobIndex',
            field=models.IntegerField(default=0),
        ),
    ]
