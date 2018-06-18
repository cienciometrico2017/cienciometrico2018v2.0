from django import forms
from apps.pais.models import pais
class PaisForm(forms.ModelForm):
    class Meta:
        model=pais
        fields= [
            'Iso',
            'Nombre',
        ]
        labels={
            'Iso':'Iso',
            'Nombre':'Nombre',
        }
        widgets={
            'Iso':forms.TextInput(attrs={'class':'form-control'}),
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
        }