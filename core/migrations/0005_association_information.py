# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120, verbose_name='Company name')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('email', models.EmailField(max_length=254)),
                ('short_description', models.CharField(max_length=100, verbose_name='Short description')),
                ('long_description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Association information',
                'verbose_name_plural': 'Association information',
            },
        ),
    ]
