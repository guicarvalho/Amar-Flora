# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_associate_associated_from'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_associates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_type', models.CharField(choices=[(None, ''), ('R', 'Residential'), ('P', 'Plot'), ('C', 'Company'), ('I', 'Individual')], max_length=1, verbose_name='Subject')),
                ('price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Investiment')),
            ],
            options={
                'verbose_name': 'Category Associates',
                'verbose_name_plural': 'Categories Associates',
            },
        ),
        migrations.DeleteModel(
            name='document',
        ),
    ]
