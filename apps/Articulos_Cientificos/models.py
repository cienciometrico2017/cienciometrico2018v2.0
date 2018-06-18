# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.Linea_Investigacion.models import linea_investigacion
from apps.Sub_Lin_Investigacion.models import sub_lin_investigacion
from apps.baseDatos.models import baseDatos
from apps.Revista.models import revista
from apps.palabraClave.models import palabraClave
from apps.ciudad.models import ciudad
from apps.pais.models import pais
from django.contrib.auth.models import User


# Create your models here.
class articulos_cientificos(models.Model):
    Estado = (
        ('Receptado', 'Receptado'),
        ('En revisión', 'En revisión'),
        ('Aceptado', 'Aceptado'),
        ('Publicado', 'Publicado'),
    )
    Tipo = (
        ('Científico', 'Científico'),
        ('De revisión', 'De revisión'),
        ('Ensayo', 'Ensayo'),
        ('Reflexión', 'Reflexión'),
    )

    titulo = models.CharField(max_length=300, null=True, blank=True, unique=True)
    estado = models.CharField(max_length=30, blank=True, null=True, choices=Estado)
    iSSN = models.CharField(max_length=60, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    doi = models.CharField(max_length=300, blank=True, null=True)
    fechaPublicacion = models.DateField(blank=True, null=True)
    pais = models.ForeignKey(pais, blank=True, null=True)
    ciudad = models.ForeignKey(ciudad, blank=True, null=True)
    baseDatos = models.ManyToManyField(baseDatos, blank=True)
    revista = models.ForeignKey(revista, blank=True)
    volumen = models.CharField(max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=150, blank=True, null=True)
    lineaInves = models.ForeignKey(linea_investigacion, max_length=150, blank=True, null=True)
    SubLinea = models.ForeignKey(sub_lin_investigacion, max_length=150, blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    palabraClave = models.ManyToManyField(palabraClave, blank=True)
    documento = models.FileField(upload_to='articulo/', blank=True, null=True)
    tipoArticulo = models.CharField(max_length=150, blank=True, null=True, choices=Tipo)
    aprobado = models.CharField(max_length=150, blank=True, null=True)

    comiteEditorial = models.CharField(max_length=150, blank=True, null=True)
    estPub = models.BooleanField(blank=True)
    desEstado = models.TextField(null=True, blank=True)

    class Meta:
        permissions = (
            ("ver_articulo", "ver articulo"),
        )
