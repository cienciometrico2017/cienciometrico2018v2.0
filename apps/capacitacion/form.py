from django import forms
from apps.capacitacion.models import capacitacion

class CapacitacionForm (forms.ModelForm):
    class Meta:
        model = capacitacion
        fields = [
            'areaConocimiento',
            'horas',
            'institucion',
            'descripcion',
            'evidencias',
            'tipoCapacitacion',
            'user',
        ]
        labels = {
            'areaConocimiento':' Área de conocimiento',
            'horas': 'Número de horas de duración de la capacitación',
            'institucion': 'Institución, organización o univerdidad dónde recibió la capacitación',
            'descripcion': 'Nombre de la capacitación en la que participó',
            'evidencias': 'PDFs de los diplomas concedidos',
            'tipoCapacitacion': 'tipoCapacitacion',
            'user':'',
        }
        widgets = {
            'areaConocimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'horas': forms.NumberInput(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'evidencias': forms.FileInput(attrs={'class': 'form-control'}),
            'tipoCapacitacion': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(attrs={'class': 'form-control','id':'user','name':'user'}),
        }
