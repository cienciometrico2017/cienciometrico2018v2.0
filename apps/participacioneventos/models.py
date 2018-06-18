from django.db import models

# Create your models here.
class participacionevento(models.Model):

    Titulo = models.CharField(max_length=255)
    Nivel_Autoria=models.CharField(max_length=255)
    Palabras_Clave = models.TextField(max_length=550)
    Resumen= models.TextField(max_length=550)
    Documento = models.FileField(upload_to='eventos/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Nombre_Evento=models.CharField(max_length=255)
    Nivel=models.CharField(max_length=255)
    Lugar_Evento=models.CharField(max_length=255)
    Fecha_Evento=models.DateField()

    class Meta:
        permissions = (
            ("ver_ParticipacionesEventos", "ver ParticipacionesEventos"),
        )