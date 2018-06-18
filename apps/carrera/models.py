# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from apps.facultad.models import facultad

class carrera (models.Model):
    Nombre=models.CharField(max_length=350)
    Director=models.CharField(max_length=250)
    facultad=models.ForeignKey(facultad,null=True ,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Nombre)

    class Meta:
        permissions = (
            ("ver_carrera", "ver carrera"),
        )

