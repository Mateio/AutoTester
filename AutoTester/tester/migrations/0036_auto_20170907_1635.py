# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 21:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0035_auto_20170907_1225'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestSequenceExternal',
            new_name='TestDefinition',
        ),
    ]
