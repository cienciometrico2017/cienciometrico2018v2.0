from django.db import models
from django.contrib.auth.models import User
from apps.universidad.models import universidad
from apps.pais.models import pais


# Create your models here.

class formacion_academica(models.Model):
    TipoTitulo = (
        ('Título de tercer nivel', 'Título de tercer nivel'),
        ('Título de cuarto nivel', 'Título de cuarto nivel'),
    )
    descripcion = models.CharField(max_length=300, null=True)
    anio = models.CharField(max_length=50, null=True)
    titulo = models.CharField(max_length=250, null=True)
    tipoTitulo = models.CharField(max_length=250, null=True, choices=TipoTitulo)
    nombreCentroEstudios = models.ForeignKey(universidad, null=True, blank=True)
    pais = models.ForeignKey(pais, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.titulo)

    class Meta:
        permissions = (
            ("ver_formacionAcademica", "ver formacionAcademica"),
        )
