from django import forms
from apps.Intereses_Formativos.models import intereses_formativos

class InteresForm (forms.ModelForm):
    class Meta:
        model = intereses_formativos
        fields = [
            'tematicaInteres',
            'descripcion',
            'palabrasClave',
            'user',
        ]
        labels = {
            'tematicaInteres':'Temática de interés',
            'descripcion':'Descripción',
            'palabrasClave':'Palabras clave',
            'user':'',
        }
        widgets = {
            'tematicaInteres': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'palabrasClave': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(attrs={'class': 'form-control','id':'user','name':'user'}),
        }
