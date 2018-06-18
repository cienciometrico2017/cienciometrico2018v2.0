from django import forms
from apps.campus.models import campus
class CampusForm(forms.ModelForm):
    class Meta:
        model= campus
        fields= [
            'Nombre',
            'provincia',
            'universidad',
        ]
        labels={
            'Nombre':'Nombre',
            'provincia': 'Provincia',
            'universidad': 'Universidad',
        }
        widgets={
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control','id':'prov'}),
            'universidad': forms.Select(attrs={'class': 'form-control'}),
        }