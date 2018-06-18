from apps.roles.models import Rol
from django.contrib.auth.models import User, Permission
from django.contrib.auth.forms import UserCreationForm
from django import forms
class Registrorol(forms.ModelForm):
    class Meta:
        model= Rol
        fields = [
            'Nombre',
            'privilegios',

        ]
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'required':'true'}),
            'privilegios': forms.CheckboxSelectMultiple(),

        }
