# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 20:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_associate_associated_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='associate',
            name='associated_from',
            field=models.DateField(default=datetime.datetime(2016, 5, 30, 20, 52, 25, 823119, tzinfo=utc), verbose_name='Associated from'),
            preserve_default=False,
        ),
    ]
