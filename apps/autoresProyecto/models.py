from django.db import models
from django.contrib.auth.models import User
from apps.Proyectos.models import proyecto
class autoresProyecto (models.Model):
    gradoAutoria = models.CharField(max_length=150, blank=False, null=False)
    proyecto = models.ForeignKey(proyecto, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.gradoAutoria)

    class Meta:
        permissions = (
            ("ver_autores", "ver autores"),
        )
