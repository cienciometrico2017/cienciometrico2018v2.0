from django.db import models
from django.contrib.auth.models import User
from apps.roles.models import Rol
from apps.informacionLaboral.models import informacionLaboral
# Create your models here.
class Investigador(models.Model):
    CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    )
    cedula = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='foto/', null=True,blank=True)
    direccion = models.CharField(max_length=500, blank=True, null=True)
    edad = models.DateField(null=True,blank=True)
    coordenadas = models.CharField(max_length=450, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    genero = models.CharField(max_length=100, blank=True, choices=CHOICES, null=True)
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    cambio = models.BooleanField(max_length=100, blank=True)
    roles = models.ManyToManyField(Rol, blank=True)
    documento = models.FileField(upload_to='docSen/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    informacionLaboral = models.OneToOneField(informacionLaboral, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.cedula)

    # Permisos

    class Meta:
        permissions = (
            ("ver_perfil", "ver perfil"),
        )