from django.db import models
from apps.pais.models import pais
from apps.zona.models import zona

# Create your models here.
class universidad(models.Model):
    Nombre = models.CharField(max_length=250, null=True, blank=True)
    Rector = models.CharField(max_length=250, null=True, blank=True)
    instituto = models.CharField(max_length=50, null=True, blank=True)
    pais = models.ForeignKey(pais, null=True, blank=True, on_delete=models.CASCADE)
    zona = models.ForeignKey(zona, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Nombre)

    class Meta:
        permissions = (
            ("ver_Universidad", "ver Universidad"),
        )
