# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0042_auto_20170908_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdefinition',
            name='reagent2Slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reagent2', to='tester.ReagentSetup'),
        ),
        migrations.AlterField(
            model_name='testdefinition',
            name='reagent3Slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reagent3', to='tester.ReagentSetup'),
        ),
    ]
