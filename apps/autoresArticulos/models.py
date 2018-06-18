from django.db import models
from django.contrib.auth.models import User
from apps.Articulos_Cientificos.models import articulos_cientificos
from apps.carrera.models import carrera
class autoresArticulos (models.Model):
    gradoAutoria = models.CharField(max_length=150, blank=False, null=False)
    articulo = models.ForeignKey(articulos_cientificos, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.gradoAutoria)

    class Meta:
        permissions = (
            ("ver_autores", "ver autores"),
        )
