# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0011_auto_20170904_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresultsexternal',
            name='datePerformed',
            field=models.DateTimeField(),
        ),
    ]
