from django.db import models
from django.contrib.auth.models import User
from apps.Sub_Lin_Investigacion.models import sub_lin_investigacion
from apps.Investigador.models import Investigador
from apps.Ambito_Investigativo.models import ambito_investigativo
# Create your models here.
class palabraClave(models.Model):
 Termino=models.CharField(max_length=50)
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 def __str__(self): return '{}'.format(self.Termino)