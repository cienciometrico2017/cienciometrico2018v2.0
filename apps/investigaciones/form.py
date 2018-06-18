from django import forms

from apps.investigaciones.models import investigacion


class DocumentForm(forms.ModelForm):
    class Meta:
        model = investigacion
        fields = [
            'titulo',
            'descripcion',
            'fechaInicial',
            'fechaFinal',
            'estado',
            'url',
            'gradoAutoria',
        ]
        labels = {
            'titulo':'Título',
            'descripcion':'Descripción',
            'fechaInicial':'Fecha inicial',
            'fechaFinal':'Fecha Final',
            'estado':'Estado',
            'url':'URL',
            'gradoAutoria':'Grado de autoría',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fechaInicial': forms.DateInput(attrs={'class': 'form-control'}),
            'fechaFinal': forms.DateInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'gradoAutoria': forms.TextInput(attrs={'class': 'form-control'}),
        }
