# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 04:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20160611_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='charge',
            field=models.CharField(default=datetime.datetime(2016, 6, 12, 4, 12, 11, 784077, tzinfo=utc), max_length=80, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
