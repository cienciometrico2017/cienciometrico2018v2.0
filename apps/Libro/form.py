from django import forms

from apps.Libro.models import libro


class DocumentForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = [
            'Titulo',
            'ISBN',
            'Anio',
            'Editorial',
            'Resumen',
            'PalabrasClave',
            'Documento',
            'BaseDatos',
            'Url',
            'Doi',
            'UbicacionFisica',
            'capitulo',
            'tipo',
            'autoresLibro',

        ]
        labels = {
            'Titulo': 'Título de portada del libro',
            'ISBN': 'Código normalizado internacional para libros (ISBN)',
            'Anio': 'Año de emisión del libro',
            'Editorial': 'Empresa que editó el libro',
            'Resumen': 'Información del contexto del libro',
            'PalabrasClave': 'Palabras Claves',
            'Documento': 'Archivo digital del libro PDF u otros',
            'BaseDatos': 'Base de datos',
            'Url': 'Ruta online dónde se encuentra el libro (URL)',
            'Doi': 'Identifación Digital del libro (DOI)',
            'UbicacionFisica': 'Ubicación Física del Libro',
            'capitulo': 'Capítulo de libro',
            'tipo': 'Seleccione una opción',
            'autoresLibro':'Autor/es del libro',
        }

        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control','id':'tipo'}),
            'ISBN': forms.TextInput(attrs={'class': 'form-control'}),
            'Anio': forms.TextInput(attrs={'class': 'form-control'}),
            'Editorial': forms.TextInput(attrs={'class': 'form-control'}),
            'Resumen': forms.Textarea(attrs={'class': 'form-control'}),
            'PalabrasClave': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'id': 'tag', 'placeholder': 'Palabras Claves', 'required': False}),
            'Documento': forms.FileInput(attrs={'required': False}),
            'BaseDatos': forms.CheckboxSelectMultiple(attrs={'class': 'form-control input-tags-1', 'multiple':'', 'data-role':'tagsinput', 'id': 'tags', 'placeholder': 'Palabras Claves'}),
            'Url': forms.URLInput(attrs={'class': 'form-control'}),
            'Doi': forms.URLInput(attrs={'class': 'form-control'}),
            'UbicacionFisica': forms.TextInput(attrs={'class': 'form-control'}),
            'capitulo': forms.TextInput(attrs={'class': 'form-control','id':'capitulo'}),
            'autoresLibro': forms.TextInput(attrs={'class': 'form-control', 'id':'autoresLibro'}),
        }
