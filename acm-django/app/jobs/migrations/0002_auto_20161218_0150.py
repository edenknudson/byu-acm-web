# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-18 08:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='updated_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 12, 18, 8, 50, 49, 236905, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='add_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]