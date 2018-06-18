from django.db import models
from apps.zona.models import zona
from apps.pais.models import pais
class provincia (models.Model):
    Nombre=models.CharField(max_length=155)
    zona=models.ForeignKey(zona, null=True ,blank=True ,on_delete=models.CASCADE)
    pais=models.ForeignKey(pais, null=True ,blank=True ,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Nombre)

    class Meta:
        permissions = (
            ("ver_provincia", "ver provincia"),
        )