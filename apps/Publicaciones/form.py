from django import forms
from apps.Publicaciones.models import publicaciones

class formPublicaciones(forms.ModelForm):
    class Meta:
        model= publicaciones
        fields = [
        'Titulo',
        'NombrePublica',
        'UbicacionFisica',
        'Url',

        ]
        labels={
            'Titulo':'Titulo de la Publicación',
            'NombrePublica':'Nombre de la Publicación',
            'UbicacionFisica':'Ubicación Física Documento',
            'Url':'Url',

        }
        widgets = {

            'Titulo': forms.TextInput(attrs={'class':'form-control'}),
            'NombrePublica':  forms.TextInput(attrs={'class':'form-control'}),
            'UbicacionFisica': forms.TextInput(attrs={'class':'form-control'}),
            'Url':  forms.URLInput(attrs={'class':'form-control'}),
        }