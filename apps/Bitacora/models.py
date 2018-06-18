# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from apps.Investigador.models import Investigador
class bitacora (models.Model):
    investigador=models.ForeignKey(Investigador,null=True ,blank=True ,on_delete=models.CASCADE)
    Hora=models.DateTimeField()
    Fecha=models.DateField()
    Actividades=models.TextField(max_length=100)


