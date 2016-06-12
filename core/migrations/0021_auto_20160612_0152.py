# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20160612_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryassociates',
            name='category_type',
            field=models.CharField(choices=[(None, ''), ('R', 'Residential'), ('G', 'Ground'), ('C', 'Company'), ('I', 'Individual')], max_length=1, verbose_name='Subject'),
        ),
    ]
