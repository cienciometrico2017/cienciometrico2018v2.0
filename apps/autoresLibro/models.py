from django.db import models
from django.contrib.auth.models import User
from apps.Articulos_Cientificos.models import articulos_cientificos
from apps.Libro.models import libro
from apps.carrera.models import carrera
class autoresLibro (models.Model):
    gradoAutoria = models.CharField(max_length=150, blank=True, null=True)
    capituloSel = models.BooleanField(blank=True)
    capituloNumero = models.CharField(max_length=200, blank=True, null=True)
    capituloTitulo = models.CharField(max_length=300, blank=True, null=True)
    libro = models.ForeignKey(libro, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.gradoAutoria)

    class Meta:
        permissions = (
            ("ver_autores", "ver autores"),
        )
