# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-03 22:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='formacion_academica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=300, null=True)),
                ('anio', models.CharField(max_length=50, null=True)),
                ('nombreCentroEstudios', models.CharField(max_length=250, null=True)),
                ('titulo', models.CharField(max_length=250, null=True)),
                ('tipoTitulo', models.CharField(choices=[('Título de tercer nivel', 'Título de tercer nivel'), ('Título de cuarto nivel', 'Título de cuarto nivel')], max_length=250, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('ver_formacionAcademica', 'ver formacionAcademica'),),
            },
        ),
    ]
