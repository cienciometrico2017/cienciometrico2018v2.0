# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from apps.Investigador.models import Investigador

class privilegios(models.Model):
    Nombre=models.CharField(max_length=40)
    Descripcion=models.TextField(max_length=200)
    investigador=models.ForeignKey(Investigador,null=True ,blank=True,on_delete=models.CASCADE)

    def __str__(self): return '{}'.format(self.Nombres)