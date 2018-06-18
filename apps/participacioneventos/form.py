from django import forms

from apps.participacioneventos.models import participacionevento
class DocuForm(forms.ModelForm):
    class Meta:
        model = participacionevento
        OPTIONS = (
            ("AUT", "Austria"),
            ("DEU", "Germany"),
            ("NLD", "Neitherlands"),
        )
        fields = [
            'Titulo',
            'Nivel_Autoria',
            'Resumen',
            'Palabras_Clave',
            'Documento',
            'Nombre_Evento',
            'Nivel',
            'Lugar_Evento',
            'Fecha_Evento'
        ]
        labels = {
            'Titulo':'Título del Evento',
            'Nivel_Autoria':'Nivel de Autoría',
            'Resumen':'Resumen',
            'Palabras_Clave':'Palabras Claves',
            'Documento':'Adjuntar Documento',
            'Nombre_Evento':'Nombre del Evento',
            'Nivel':'Nivel del Evento',
            'Lugar_Evento':'Lugar del Evento',
            'Fecha_Evento':'Fecha de Evento',
        }
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'Nivel_Autoria':forms.TextInput(attrs={'class': 'form-control'}),
            'Resumne': forms.TextInput(attrs={'class': 'form-control'}),
            'Palabras_Clave':forms.TextInput(attrs={'class':'form-control','id':'tags','placeholder':'Palabras Claves'}),
            'Documento': forms.FileInput(attrs={'class': 'form-control'}),
            'Nombre_Evento': forms.TextInput(attrs={'class': 'form-control'}),
            'Nivel':forms.TextInput(attrs={'class': 'form-control','placeholder':'NACIONAL O INTERNACIONAL'}),
            'Lugar_Evento': forms.TextInput(attrs={'class': 'form-control'}),
            'Fecha_Evento':forms.TextInput(attrs={'class': 'datepicker'}),
        }
