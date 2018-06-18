from django.db import models
from django.db import models
from apps.provincia.models import provincia
# Create your models here.
class ciudad (models.Model):
    Nombre=models.CharField(max_length=155)
    provincia=models.ForeignKey(provincia,null=True ,blank=True ,on_delete=models.CASCADE)

    def __str__(self): return '{}'.format(self.Nombre)
    class Meta:
        permissions = (
            ("ver_ciudad", "ver ciudad"),
        )
