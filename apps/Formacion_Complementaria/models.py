# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class formacion_complementaria(models.Model):
    Nivel_Estudios=models.CharField(max_length=50,null=True)
    NombreTitulo=models.CharField(max_length=550,null=True)
    Fecha_Fin=models.DateField(null=True)
    Nombre_Centro_Estudios=models.CharField(max_length=250,null=True)

    class Meta:
        permissions = (
            ("ver_FormacionComplementaria", "ver FormacionComplementaria"),
        )