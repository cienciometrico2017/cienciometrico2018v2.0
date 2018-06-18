from django.db import models

# Create your models here.
from apps.universidad.models import universidad
from apps.provincia.models import provincia
class campus (models.Model):
 Nombre=models.CharField(max_length=250)
 provincia=models.ForeignKey(provincia,null=True ,blank=True ,on_delete=models.CASCADE)
 universidad=models.ForeignKey(universidad,null=True ,blank=True ,on_delete=models.CASCADE)
 def __str__(self):
        return '{}'.format(self.Nombre)

 class Meta:
     permissions = (
         ("ver_campus", "ver campus"),
     )
