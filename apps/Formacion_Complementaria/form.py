from django import forms
from apps.Formacion_Complementaria.models import formacion_complementaria

class FormacionComform (forms.ModelForm):
    class Meta:
        model=formacion_complementaria
        fields=[
            'Nivel_Estudios',
            'NombreTitulo',
            'Fecha_Fin',
            'Nombre_Centro_Estudios',


        ]
        labels={
            'Nivel_Estudios':'Nivel_Estudios' ,
            'NombreTitulo': 'NombreTitulo',
            'Fecha_Fin' :'Fecha_Fin_Estudios',
            'Nombre_Centro_Estudios':'Nombre_Centro_Estudios',

        }

        widgets = {
            'Nivel_Estudios':forms.Select(attrs={'class':'form-control'}),
            'NombreTitulo':forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Fin':forms.DateInput(attrs={'class':'form-control'}),
            'Nombre_Centro_Estudios':forms.TextInput(attrs={'class':'form-control'}),


        }
