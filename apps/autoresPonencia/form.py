from django import forms
from apps.autoresPonencia.models import autoresPonencia
class autoresForm(forms.ModelForm):
    class Meta:
        model = autoresPonencia
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
