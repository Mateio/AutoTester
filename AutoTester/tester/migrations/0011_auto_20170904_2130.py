# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0010_auto_20170904_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsequenceexternal',
            name='reagent1AgitateSecs',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='testsequenceexternal',
            name='reagent1DropCount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='testsequenceexternal',
            name='reagent1Slot',
            field=models.CharField(default='A', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='testsequenceexternal',
            name='reagent2AgitateSecs',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='testsequenceexternal',
            name='reagent2DropCount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='testsequenceexternal',
            name='reagent2Slot',
            field=models.CharField(default='A', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='testsequenceexternal',
            name='reagent3AgitateSecs',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='testsequenceexternal',
            name='reagent3DropCount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='testsequenceexternal',
            name='reagent3Slot',
            field=models.CharField(default='A', max_length=1, null=True),
        ),
    ]
