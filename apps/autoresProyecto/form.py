from django import forms
from apps.autoresProyecto.models import autoresProyecto
class autoresForm(forms.ModelForm):
    class Meta:
        model = autoresProyecto
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
