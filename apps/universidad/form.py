from django import forms
from .models import pais, universidad ,zona
from apps.provincia.models import provincia

class UniversidadForm(forms.ModelForm):
    class Meta:
        model= universidad
        fields= [
            'Nombre',
            'Rector',
            'pais',
            'zona',
        ]
        labels={
            'Nombre':'Nombre',
            'Rector':'Rector',
            'pais': 'País',
            'zona': 'Zona',
        }
        widgets={
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Rector': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control', 'id':'pais', 'onchange':'myFunction()'}),
            'zona': forms.Select(attrs={'class': 'form-control', 'id':'zona'}),
        }