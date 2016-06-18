# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-16 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20160612_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='members'),
        ),
        migrations.AlterField(
            model_name='categoryassociates',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='gallery_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.Gallery', verbose_name='Gallery'),
        ),
    ]