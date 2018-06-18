from django.db import models
from apps.carrera.models import carrera
# Create your models here.
class linea_investigacion(models.Model):
 Nombre = models.CharField(max_length=200)
 Carrera = models.ForeignKey(carrera, null=True, blank=True, on_delete=models.CASCADE)

 def __str__(self): return '{}'.format(self.Nombre)