# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from  apps.campus.models import campus

class facultad (models.Model):
    Nombre=models.CharField(max_length=250)
    Decano =models.CharField(max_length=250)
    campus=models.ForeignKey(campus,null=True ,blank=True ,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Nombre)

    class Meta:
        permissions = (
            ("ver_facultad", "ver facultad"),
        )
