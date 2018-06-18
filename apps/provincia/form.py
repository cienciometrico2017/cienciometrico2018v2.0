from django import forms
from apps.provincia.models import provincia
class ProvinciaForm(forms.ModelForm):
    class Meta:
        model= provincia
        fields= [
            'Nombre',
            'zona',
            'pais',
        ]
        labels={
            'Nombre':'Nombre',
            'zona':'Zona',
            'pais': 'País',
        }
        widgets={
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'zona': forms.Select(attrs={'class': 'form-control','id':'zona'}),
            'pais': forms.Select(attrs={'class': 'form-control','id':'pais'}),
        }