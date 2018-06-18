from django.db import models

# Create your models here.
class otrasinvestigaciones(models.Model):

 Titulo = models.CharField(max_length=255)
 Resumen = models.TextField()
 Palabras_Clave = models.TextField()
 Documento = models.FileField(upload_to='otrasinvestigaciones/', null=True, blank=True)
 uploaded_at = models.DateTimeField(auto_now_add=True)
 FechaInicio = models.DateField()
 FechaFin= models.DateField()
 Url = models.URLField(null=True)

 def __str__(self):
  return '{}'.format(self.Titulo)

 class Meta:
  permissions = (
   ("ver_otrasinvestigaciones", "ver otrasinvesitgaciones"),
  )
