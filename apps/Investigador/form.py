from apps.Investigador.models import Investigador
from django.contrib.auth.models import User
from apps.informacionLaboral.models import informacionLaboral
from django import forms

class RegistroForm(forms.ModelForm):
    class Meta:
        model= Investigador
        fields = [
            'cedula',
            'photo',
            'coordenadas',
            'telefono',
            'genero',
            'nacionalidad',
            'direccion',
            'edad',
        ]
        labels = {
            'cedula': 'Cedula',
            'photo':'Fotografía',
            'direccion': 'Dirección, (para obtener la dirección automaticamente mueva el pin ',
            'edad':'Fecha de nacimiento',
            'coordenadas': 'Coordenadas',
            'telefono': 'Teléfono',
            'genero': 'Genero',
            'nacionalidad': 'Nacionalidad',

        }
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control','required':False}),
            'photo':forms.FileInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','id':'address1'}),
            'edad': forms.TextInput(attrs={'class': 'form-control datepicker', 'type':'date'}),
            'coordenadas': forms.TextInput(attrs={'class': 'form-control','style':'display:none','id':'latlng', 'value':'-0.917476, -78.632573'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),

        }


class UserForm (forms.ModelForm):
    class Meta:
        model = User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels={
            'username':'Username',
            'first_name':'Nombres',
            'last_name':'Apellidos',
            'email':'Correo electrónico',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','required':False, 'readonly':True}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','required':False, 'readonly':True}),
        }


class InformacionForm (forms.ModelForm):
    class Meta:
        model = informacionLaboral
        fields = [
            'tipoContrato',
            'facultad',
            'carrera',
            'university',
        ]
        labels = {
            'tipoContrato': 'Tipo de contrato',
            'facultad': 'Facultad',
            'carrera': 'Carrera',
            'university': '',
        }
        widgets = {
            'tipoContrato': forms.Select(attrs={'class': 'form-control'}),
            'facultad': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'university': forms.Select(attrs={'class': 'form-control'}),
        }

class PasswordForm (forms.ModelForm):
    class Meta:
        model = User
        fields=[
            'password',
        ]
        labels={
            'password':'Ingrese una nueva contraseña',
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class cambioForm (forms.ModelForm):
    class Meta:
        model = Investigador
        fields = [
            'cambio',
        ]
        labels={
            'cambio': 'Cambiar estado',
        }
        widgets = {
            'cambio': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class document (forms.ModelForm):
    class Meta:
        model = Investigador
        fields = [
            'documento',
        ]
        labels={
            'documento': 'Adjuntar archivo',
        }
        widgets = {
            'documento': forms.FileInput(),
        }