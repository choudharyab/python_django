# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-04 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pharajinnyserverapi', '0005_mass_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=b'upload'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mass_post',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=b'upload'),
            preserve_default=False,
        ),
    ]