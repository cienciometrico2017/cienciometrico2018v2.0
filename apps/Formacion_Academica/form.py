from django import forms
from apps.Formacion_Academica.models import formacion_academica

class FormacionAform (forms.ModelForm):
    class Meta:
        model=formacion_academica
        fields=[
            'descripcion',
            'anio',
            'pais',
            'nombreCentroEstudios',
            'titulo',
            'tipoTitulo',
            'user',
        ]
        labels={
            'descripcion':'Título obtenido',
            'anio':'Año de graduación',
            'pais':'Pais',
            'nombreCentroEstudios':'Universidad donde se graduó',
            'titulo':'Título de la tesis con la que se graduó',
            'tipoTitulo':'Tipo de título',
            'user':'',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombreCentroEstudios':forms.Select(attrs={'class':'form-control', 'id':'nombreCentroEstudios','name':'nombreCentroEstudios'}),
            'pais': forms.Select(attrs={'class': 'form-control', 'id':'pais','name':'pais'}),
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'tipoTitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'user'}),
        }
