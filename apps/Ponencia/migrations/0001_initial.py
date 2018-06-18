# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-04 05:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autoresArticulos', '0001_initial'),
        ('Articulos_Cientificos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('palabraClave', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ponencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePonencia', models.CharField(blank=True, max_length=150, null=True)),
                ('lugarPonencia', models.CharField(blank=True, max_length=150, null=True)),
                ('tituloPonencia', models.CharField(blank=True, max_length=70, null=True)),
                ('fechaPonencia', models.DateField(blank=True, null=True)),
                ('anio', models.IntegerField(blank=True, null=True)),
                ('resumen', models.TextField(blank=True, null=True)),
                ('certificado', models.FileField(blank=True, null=True, upload_to='certificados/')),
                ('urlPonencia', models.URLField(blank=True, null=True)),
                ('financiamiento', models.CharField(blank=True, choices=[('Sí', 'Sí'), ('No', 'No')], max_length=2, null=True)),
                ('financia', models.CharField(blank=True, max_length=200, null=True)),
                ('informe', models.FileField(blank=True, null=True, upload_to='informes/')),
                ('articuloCientifico', models.ManyToManyField(blank=True, to='Articulos_Cientificos.articulos_cientificos')),
                ('autores', models.ManyToManyField(to='autoresArticulos.autoresArticulos')),
                ('palabrasClave', models.ManyToManyField(blank=True, to='palabraClave.palabraClave')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
