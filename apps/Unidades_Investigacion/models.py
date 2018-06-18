from django.db import models

# Create your models here.
class unidades_investigacion (models.Model):
    Nombre = models.CharField(max_length=150)