# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-03 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Unidad_Investigacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ambito_investigativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('unidad_investigacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Unidad_Investigacion.unidad_investigacion')),
            ],
        ),
    ]
