# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-04 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos_Cientificos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos_cientificos',
            name='doi',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='articulos_cientificos',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]