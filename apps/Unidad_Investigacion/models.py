from django.db import models
from apps.universidad.models import universidad
# Create your models here.
class unidad_investigacion (models.Model):
    Nombre=models.CharField(max_length=50)
    Director=models.CharField(max_length=100)
    universidad=models.ForeignKey(universidad,null=True ,blank=True ,on_delete=models.CASCADE)

    def __str__(self): return '{}'.format(self.Nombre)