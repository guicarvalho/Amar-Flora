# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_useful_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('subject', models.CharField(choices=[(None, ''), ('C', 'Craft'), ('R', 'Recorde'), ('S', 'Statute')], max_length=1, verbose_name='Subject')),
            ],
            options={
                'verbose_name_plural': 'Documents',
                'verbose_name': 'Document',
            },
        ),
        migrations.CreateModel(
            name='ImageNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='statics/core/image')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='core.News', verbose_name='Id news')),
            ],
            options={
                'verbose_name_plural': 'Images news',
                'verbose_name': 'Image news',
            },
        ),
        migrations.AlterField(
            model_name='useful_phone',
            name='phone2',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Phone'),
        ),
    ]