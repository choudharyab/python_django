# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-03 05:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pharajinnyserverapi', '0002_auto_20180102_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='comments',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
