from django.db import models
from apps.Unidad_Investigacion.models import unidad_investigacion
# Create your models here.
class ambito_investigativo(models.Model):
    Nombre=models.CharField(max_length=40)
    unidad_investigacion = models.ForeignKey(unidad_investigacion, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self): return '{}'.format(self.Nombre)
