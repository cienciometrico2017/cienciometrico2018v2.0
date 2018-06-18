from django import forms

from apps.Proyectos.models import proyecto


class DocumentForm(forms.ModelForm):
    class Meta:
        model = proyecto
        fields = [
            'titulo',
            'financiamiento',
            'montoFinanciado',
            'montorecibido',
            'fechaInicial',
            'fechaFinal',
            'estado',
            'resumen',
            'palabrasClaves',
            'lineaInvestigacion',
            'subLinea',
            'tipoProyecto',
            'documentos',
        ]
        labels = {
            'titulo': 'Título del proyecto',
            'financiamiento': 'Institución que financia el proyecto',
            'montoFinanciado': 'Monto financiado',
            'montorecibido': 'Monto recibido',
            'fechaInicial': 'Fecha en la que inició el proyecto',
            'fechaFinal': 'Fecha en la que finalizó/a el proyecto',
            'estado': 'Estado del proyecto',
            'resumen': 'Resumen / Abstract',
            'palabrasClaves': 'Palabras Clave',
            'lineaInvestigacion': 'Linea de Investigación',
            'subLinea': 'SubLinea de Investigación',
            'tipoProyecto': 'Tipo de Proyecto',
            'documentos': 'Adjuntar Archivo',

        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'financiamiento': forms.Select(attrs={'class': 'form-control'}),
            'montoFinanciado': forms.TextInput(attrs={'class': 'form-control'}),
            'montorecibido': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaInicial': forms.TextInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'fechaFinal': forms.TextInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'integrantes': forms.Select(attrs={'class': 'form-control'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control'}),
            'palabrasClaves': forms.Select(attrs={'class': 'form-control'}),
            'lineaInvestigacion': forms.Select(attrs={'class': 'form-control'}),
            'subLinea': forms.Select(attrs={'class': 'form-control'}),
            'tipoProyecto': forms.Select(attrs={'class': 'form-control'}),
            'documentos': forms.FileInput(attrs={'class': 'form-control'}),
        }
