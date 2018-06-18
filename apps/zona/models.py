from django.db import models
from apps.pais.models import pais
# Create your models here.
class zona (models.Model):
    Nombre=models.CharField(max_length=150)
    Descripcion=models.TextField()
    pais = models.ForeignKey(pais, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.Nombre)

    class Meta:
        permissions = (
            ("ver_zona", "ver zona"),
        )
