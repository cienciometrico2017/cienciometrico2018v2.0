from django import forms
from apps.baseDatos.models import baseDatos
class baseForm(forms.ModelForm):
    class Meta:
        model = baseDatos
        fields= [
            'BaseDatos',
            'Url',
            'user',
        ]
        labels={
            'BaseDatos':'Nombre de la base de datos',
            'Url':'URL',
            'user':'Autor',

        }
        widgets={
            'BaseDatos':forms.TextInput(attrs={'class':'form-control'}),
            'Url':forms.URLInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control', 'id':'user'}),
        }
