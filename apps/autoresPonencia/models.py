from django.db import models
from django.contrib.auth.models import User
from apps.Ponencia.models import ponencia
class autoresPonencia (models.Model):
    gradoAutoria = models.CharField(max_length=150, blank=False, null=False)
    ponencia = models.ForeignKey(ponencia, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.gradoAutoria)

    class Meta:
        permissions = (
            ("ver_autores", "ver autores"),
        )
