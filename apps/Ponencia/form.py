from django import forms
from apps.Ponencia.models import ponencia

class PonenciaForm (forms.ModelForm):
    class Meta:
        model = ponencia
        fields = [
            'nombrePonencia',
            'lugarPonencia',
            'tituloPonencia',
            'fechaPonencia',
            'anio',
            'palabrasClave',
            'resumen',
            'certificado',
            'urlPonencia',
            'financiamiento',
            'financia',
            'informe',
            'articuloCientifico',
            'user',
        ]
        labels = {
            'nombrePonencia':'Nombre del evento',
            'lugarPonencia':'Lugar del evento',
            'tituloPonencia':'Titulo de ponencia',
            'fechaPonencia':'Fecha de la ponencia',
            'anio':'Año',
            'palabrasClave':'Palabras clave',
            'resumen':'Resumen',
            'certificado':'Certificado',
            'urlPonencia':'URL',
            'financiamiento': 'Financiamiento',
            'financia': 'Universidad la cual financia costos de la disertación',
            'informe':'Informe de actividades',
            'articuloCientifico':'La disertación pertenece a algún artículo cientifico.',

            'user': '',

        }
        widgets = {
            'nombrePonencia':forms.TextInput(attrs={'class': 'form-control'}),
            'lugarPonencia':forms.TextInput(attrs={'class': 'form-control'}),
            'tituloPonencia': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaPonencia':forms.TextInput(attrs={'class':'form-control datepicker','type':'date'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'palabrasClave':forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'resumen':forms.Textarea(attrs={'class': 'form-control'}),
            'certificado':forms.FileInput(attrs={'class': 'form-control'}),
            'urlPonencia':forms.URLInput(attrs={'class': 'form-control'}),
            'financiamiento':forms.Select(attrs={'class': 'form-control', 'id':'financiamiento'}),
            'financia': forms.Select(attrs={'class': 'form-control'}),
            'informe': forms.FileInput(attrs={'class': 'form-control'}),
            'articuloCientifico': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'user'}),
        }
