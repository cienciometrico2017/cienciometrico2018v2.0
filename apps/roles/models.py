from django.db import models
from django.contrib.auth.models import Permission
# Create your models here.
class Rol(models.Model):
    Nombre = models.CharField(max_length=500, blank=True)
    privilegios = models.ManyToManyField(Permission,blank=True)
    def __str__(self):
        return '{}  {}'.format(self.pk,self.Nombre)
    class Meta:
        permissions = (
            ("ver_rol", "ver rol"),
        )