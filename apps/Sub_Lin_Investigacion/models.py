from django.db import models
from apps.Linea_Investigacion.models import linea_investigacion
from apps.carrera.models import carrera

# Create your models here.
class sub_lin_investigacion(models.Model):
 Nombre = models.CharField(max_length=200)
 linea_investigacion= models.ForeignKey(linea_investigacion, null=True, blank=True, on_delete=models.CASCADE)
 Carrera = models.ForeignKey(carrera, null=True, blank=True, on_delete=models.CASCADE)

 def __str__(self): return '{}'.format(self.Nombre)