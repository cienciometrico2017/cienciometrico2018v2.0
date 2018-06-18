# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
class intereses_formativos (models.Model):

    tematicaInteres = models.CharField(max_length=50,blank=False,null=False, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
            message='Solo letras',
            code='SintaxisInvalida'
        ),
    ])
    descripcion = models.TextField(max_length=50)
    palabrasClave = models.CharField(max_length=300)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Tematica_Interes)

    class Meta:
        permissions = (
            ("ver_interes", "ver interes"),
        )