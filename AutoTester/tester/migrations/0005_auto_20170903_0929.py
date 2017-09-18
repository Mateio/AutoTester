# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0004_auto_20170818_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesterProcessingParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cameraChannel', models.CharField(default='0', max_length=100)),
                ('cameraIllumSource', models.CharField(default='LED', max_length=100)),
                ('framesPerSecond', models.IntegerField(default=10)),
                ('defaultReferenceCenterRow', models.FloatField(default=256.5)),
                ('defaultReferenceCenterCol', models.FloatField(default=245)),
                ('defaultAvgDotDistance', models.FloatField(default=95)),
            ],
        ),
        migrations.AddField(
            model_name='testerexternal',
            name='measurementUnits',
            field=models.CharField(default='US Imperial', max_length=40),
        ),
    ]
