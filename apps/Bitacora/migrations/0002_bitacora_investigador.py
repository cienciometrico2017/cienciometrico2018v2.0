# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-03 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Investigador', '0001_initial'),
        ('Bitacora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitacora',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.Investigador'),
        ),
    ]
