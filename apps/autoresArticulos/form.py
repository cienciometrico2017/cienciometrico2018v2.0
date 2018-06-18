from django import forms
from apps.autoresArticulos.models import autoresArticulos
class autoresForm(forms.ModelForm):
    class Meta:
        model = autoresArticulos
        fields= [
            'gradoAutoria',
            'user',
        ]
        labels={
            'gradoAutoria':'Grado de autoria',
            'user':'Autor',

        }
        widgets={
            'gradoAutoria':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
        }
