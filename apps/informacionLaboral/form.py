from django import forms
from apps.informacionLaboral.models import informacionLaboral
class infLabForm(forms.ModelForm):
    class Meta:
        model=informacionLaboral
        fields= [
            'tipoContrato',
            'facultad',
            'carrera',
            'university',

        ]
        labels={
            'tipoContrato':'Tipo de contrato',
            'facultad':'Facultad',
            'carrera':'Carrera',
            'university':'Universidad',
        }
        widgets={
            'tipoContrato':forms.TextInput(attrs={'class':'form-control'}),
            'facultad':forms.Select(attrs={'class':'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'university': forms.Select(attrs={'class': 'form-control'}),
        }