from django import forms
from apps.Evento.models import evento

class EventoForm (forms.ModelForm):
    class Meta:
        model = evento
        fields = [
            'Nombre',
            'Lugar',
            'Fecha',
        ]
        labels = {
            'Nombre': 'Nombre',
            'Lugar': 'Lugar',
            'Fecha': 'Fecha',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'Fecha':forms.DateInput(attrs={'class': 'form-control'}),
        }
