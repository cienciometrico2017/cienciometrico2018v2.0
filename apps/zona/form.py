from django import forms
from apps.zona.models import zona
class ZonaForm(forms.ModelForm):
    class Meta:
        model= zona
        fields= [
            'Nombre',
            'Descripcion',
            'pais',

        ]
        labels={
            'Nombre':'Nombre',
            'Descripcion':'Descripcion',
            'pais':'Paises',

        }
        widgets={
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
        }