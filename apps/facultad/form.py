from django import forms
from apps.facultad.models import facultad

class FacultadForm (forms.ModelForm):
    class Meta:
        model = facultad
        fields = [
            'Nombre',
            'Decano',
            'campus',
        ]
        labels = {
            'Nombre': 'Nombre',
            'Decano': 'Decano',
            'campus': 'Campus',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Decano': forms.TextInput(attrs={'class': 'form-control'}),
            'campus':forms.Select(attrs={'class': 'form-control','id':'campus'}),
        }
