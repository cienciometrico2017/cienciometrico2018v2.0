from django import forms
from apps.ciudad.models import ciudad
class CiudadForm(forms.ModelForm):
    class Meta:
        model= ciudad
        fields= [
            'Nombre',
            'provincia',
        ]
        labels={
            'Nombre':'Nombre',
            'provincia': 'Provincias',
        }
        widgets={
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control'}),
        }