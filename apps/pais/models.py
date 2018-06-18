from django.db import models

# Create your models here.
class pais (models.Model):
    Iso=models.CharField(max_length=2)
    Nombre=models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.Nombre)

    class Meta:
        permissions = (
            ("ver_pais", "ver pais"),
        )
