# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160303_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 3, 15, 18, 23, 637534, tzinfo=utc)),
        ),
    ]
