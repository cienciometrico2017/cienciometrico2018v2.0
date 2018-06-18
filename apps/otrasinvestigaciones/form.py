from django import forms

from apps.otrasinvestigaciones.models import otrasinvestigaciones
class DocumentForm(forms.ModelForm):
    class Meta:
        model = otrasinvestigaciones
        fields = [
            
            'Titulo',
            'Resumen',
            'Palabras_Clave',
            'Documento',
            'FechaInicio',
            'FechaFin',
            'Url',
        ]
        labels = {
            'Titulo':'Título Proyecto',
            'Resumen':'Resumen del Proyecto',
            'Palabras_Clave':'Palabras Clave',
            'Documento':'Adjuntar Documento',
            'FechaInicio':'Fecha de Inicio',
            'FechaFin':'Fecha de Culminación',
            'Url':'Link',
        }
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'Resumen':  forms.TextInput(attrs={'class': 'form-control'}),
            'Palabras_Clave':forms.TextInput(attrs={'class':'form-control','id':'tags','placeholder':'Palabras Claves'}),
            'Documento': forms.FileInput(attrs={'class': 'form-control'}),
            'FechaInicio':forms.TextInput(attrs={'class': 'datepicker'}),
            'FechaFin': forms.TextInput(attrs={'class': 'datepicker'}),
            'Url': forms.URLInput(attrs={'class': 'form-control'}),
        }
