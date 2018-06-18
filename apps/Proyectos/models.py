from django.db import models

from apps.autoresArticulos.models import autoresArticulos
from apps.palabraClave.models import palabraClave
from apps.Linea_Investigacion.models import linea_investigacion
from apps.Sub_Lin_Investigacion.models import sub_lin_investigacion
from apps.universidad.models import universidad


class proyecto(models.Model):
    Tipo = (
        ('Formativo', 'Formativo'),
        ('Generativo', 'Generativo'),
    )
    Estado = (
        ('En espera de Presupuesto', 'En espera de Presupuesto'),
        ('En Ejecución', 'En Ejecución'),
        ('Finalizado', 'Finalizado'),
    )

    titulo = models.CharField(max_length=255, blank=True, null=True)
    financiamiento = models.ForeignKey(universidad, blank=True, null=True)
    montoFinanciado = models.CharField(max_length=200, blank=True, null=True)
    montorecibido = models.CharField(max_length=200, blank=True, null=True)
    fechaInicial = models.DateField()
    fechaFinal = models.DateField()
    estado = models.CharField(max_length=200, choices=Estado, blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    palabrasClaves = models.ManyToManyField(palabraClave, blank=True)
    lineaInvestigacion = models.ForeignKey(linea_investigacion, blank=True, null=True)
    subLinea = models.ForeignKey(sub_lin_investigacion, blank=True, null=True)
    tipoProyecto = models.CharField(max_length=255, choices=Tipo, blank=True, null=True)
    documentos = models.FileField(upload_to='proyecto/', null=True, blank=True)

    class Meta:
        permissions = (
            ("ver_Proyectos", "ver Proyectos"),
        )
