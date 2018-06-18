from django.db import models

# Create your models here.
class investigacion(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fechaInicial=models.DateField()
    fechaFinal = models.DateField()
    estado = models.CharField(max_length=255)
    url = models.URLField()
    gradoAutoria = models.CharField(max_length=255)

    class Meta:
        permissions = (
            ("ver_investigaciones", "ver investigaciones"),

        )
