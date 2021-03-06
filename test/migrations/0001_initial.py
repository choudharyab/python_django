# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pharjinny_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=20)),
                ('confirm_password', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], default=b'M', max_length=1)),
                ('contact_no', models.CharField(max_length=13)),
            ],
        ),
    ]
