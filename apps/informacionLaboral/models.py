from django.db import models
from django.contrib.auth.models import User
from apps.facultad.models import facultad
from apps.carrera.models import carrera
from apps.universidad.models import universidad
class informacionLaboral (models.Model):
    Tipo = (
        ('Servicios Ocasionales', 'Servicios Ocasionales'),
        ('Nombramiento Titular Auxiliar 1','Nombramiento Titular Auxiliar 1'),
        ('Nombramiento Titular Auxiliar 2', 'Nombramiento Titular Auxiliar 2'),
        ('Nombramiento Titular Agregado 1', 'Nombramiento Titular Agregado 1'),
        ('Nombramiento Titular Agregado 2', 'Nombramiento Titular Agregado 2'),
        ('Nombramiento Principal 1', 'Nombramiento Principal 1'),
        ('Nombramiento Principal 2', 'Nombramiento Principal 2'),
    )
    tipoContrato=models.CharField(max_length=200,choices=Tipo, blank=True, null=True)
    facultad=models.ForeignKey(facultad, blank=True, null=True)
    carrera = models.ForeignKey(carrera, blank=True, null=True)
    university = models.ForeignKey(universidad, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.tipoContrato)

    class Meta:
        permissions = (
            ("ver_pais", "ver pais"),
        )
