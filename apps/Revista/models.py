from django.db import models
from django.contrib.auth.models import User
from apps.baseDatos.models import baseDatos

# Create your models here.
class revista(models.Model):
 Val = (
  ('Ingresada', 'Ingresada'),
  ('A revisar', 'A revisar'),
  ('Corregida', 'Corregida'),
  ('validada', 'validada'),
 )

 Nombre = models.CharField(max_length=500,unique=True)
 ISSN=models.CharField(max_length=250,null=True,blank=True)
 base=models.ManyToManyField(baseDatos, blank=True)
 Cuartil_Pertenece=models.CharField(max_length=500,null=True,blank=True)
 Factor_Impacto=models.CharField(max_length=500,null=True,blank=True)
 Url=models.URLField(null=True,blank=True)
 validar  = models.CharField(max_length=500, blank=True,null=True, choices=Val)
 user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

 def __str__(self): return '{}'.format(self.Nombre)
 class Meta:
  permissions = (
   ("ver_Revista", "ver Revista"),
  )
