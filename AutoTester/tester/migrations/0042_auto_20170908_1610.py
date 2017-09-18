# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0041_testresultsexternal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdefinition',
            name='daysToRun',
            field=models.CharField(choices=[('Everyday', 'Everyday'), ('Even', 'Even Days'), ('Odd', 'Odd Days'), ('Sunday', 'Every Sunday'), ('Monday', 'Every Monday'), ('Tuesday', 'Every Tuesday'), ('Wednesday', 'Every Wednesday'), ('Thursday', 'Every Thursday'), ('Friday', 'Every Friday'), ('Saturday', 'Every Saturday'), ('2day', 'Every 2 days'), ('3day', 'Every 3 days'), ('4day', 'Every 4 days'), ('1stday', '1st day of month'), ('115day', '1st and 15th day of month'), ('Never', 'Never')], default='Never', max_length=10, null=True),
        ),
    ]
