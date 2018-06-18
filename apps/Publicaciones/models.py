from django.db import models


class publicaciones(models.Model):
     Titulo = models.CharField(max_length=500)
     NombrePublica=models.TextField(null=True)
     UbicacionFisica=models.TextField(null=True)
     Url=models.URLField(null=True)

     class Meta:
          permissions = (
               ("ver_Publicaciones", "ver Publicaciones"),
          )