from django import forms
from apps.carrera.models import carrera

class CarreraForm (forms.ModelForm):
    class Meta:
        model = carrera
        fields = [
            'Nombre',
            'Director',
            'facultad',
        ]
        labels = {
            'Nombre': 'Nombre',
            'Director': 'Director',
            'facultad': 'facultad',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Director': forms.TextInput(attrs={'class': 'form-control'}),
            'facultad':forms.Select(attrs={'class': 'form-control','id':'facultad'}),
        }
