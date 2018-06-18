from django import forms
from apps.Revista.models import revista

class DocumentForm(forms.ModelForm):
    class Meta:
        model= revista
        fields = [
            'Nombre',
            'ISSN',
            'base',
            'Cuartil_Pertenece',
            'Factor_Impacto',
            'Url',
            'user',
        ]
        labels={
            'Nombre': 'Nombre de la Revista',
            'ISSN':'ISSN de la Revista',
            'base':'Base de Datos donde esta Indexada',
            'Cuartil_Pertenece':'Cuartil al que Pertenece',
            'Factor_Impacto':'Factor Impacto',
            'Url':'Url',
            'user': 'Investigador',

        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'ISSN': forms.TextInput(attrs={'class':'form-control'}),
            'base': forms.TextInput(attrs={'class':'form-control'}),
            'Cuartil_Pertenece': forms.TextInput(attrs={'class':'form-control'}),
            'Factor_Impacto': forms.TextInput(attrs={'class':'form-control'}),
            'Url': forms.URLInput(attrs={'class':'form-control'}),
            'user': forms.HiddenInput(attrs={'class': 'form-control','id':'user','name':'user'}),
        }