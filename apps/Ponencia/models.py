# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from apps.universidad.models import universidad
from apps.autoresArticulos.models import autoresArticulos
from apps.palabraClave.models import palabraClave
from apps.Articulos_Cientificos.models import articulos_cientificos

class ponencia (models.Model):
  CHOICES = (
    ('Sí', 'Sí'),
    ('No', 'No'),
  )
  nombrePonencia = models.CharField(max_length=150, null=True, blank=True)
  lugarPonencia = models.CharField(max_length=150, null=True, blank=True)
  tituloPonencia = models.CharField(max_length=70, null=True, blank=True)
  fechaPonencia = models.DateField(null=True, blank=True)
  anio = models.IntegerField(null=True, blank=True)
  palabrasClave = models.ManyToManyField(palabraClave, blank=True)
  resumen = models.TextField(null=True, blank=True)
  certificado = models.FileField(upload_to='certificados/', null=True, blank=True)
  urlPonencia = models.URLField(null=True, blank=True)
  financiamiento = models.CharField(max_length=2, null=True, blank=True,choices=CHOICES)
  financia = models.ForeignKey(universidad, null=True, blank=True)
  informe = models.FileField(upload_to='informes/', null=True, blank=True)
  articuloCientifico = models.ManyToManyField(articulos_cientificos, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  autores = models.ManyToManyField(autoresArticulos)
  def __str__(self): return '{}'.format(self.nombrePonencia)



