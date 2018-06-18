from django.db import models
from apps.autoresArticulos.models import autoresArticulos
from apps.palabraClave.models import palabraClave
from apps.baseDatos.models import baseDatos

class libro(models.Model):
    TIPO =(
        ('capitulo', 'Capitulo de libro'),
        ('libro', 'Libro completo'),
    )
    Titulo=models.CharField(max_length=200, null=False, blank=False, error_messages={'required': 'Por favor, ingrese un titulo'})
    ISBN = models.CharField(max_length=100, null=True, blank=True)
    Anio = models.CharField(max_length=20, null=True, blank=True)
    Editorial = models.CharField(max_length=100, null=True, blank=True)
    Resumen=models.TextField(null=True)
    PalabrasClave = models.ManyToManyField(palabraClave, blank=True)
    Documento = models.FileField(upload_to='libro/', null=True, blank=True)
    BaseDatos = models.ManyToManyField(baseDatos, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Url = models.URLField(null=True, blank=True)
    Doi = models.Doi = models.URLField(max_length=100, null=True, blank=True)
    UbicacionFisica = models.CharField(max_length=200, null=True, blank=True)

    capitulo = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.CharField(max_length=200, null=True, blank=True, choices=TIPO)
    autoresLibro = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self): return '{}'.format(self.Titulo)

    class Meta:
        permissions = (
            ("ver_libro", "ver libro"),
        )
