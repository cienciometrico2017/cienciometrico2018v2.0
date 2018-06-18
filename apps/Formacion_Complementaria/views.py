# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from apps.Formacion_Complementaria.models import formacion_complementaria
from apps.Formacion_Complementaria.form import FormacionComform
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
# Create your views here.

class CreateFormacion_Complementaria (CreateView):
    model = formacion_complementaria
    form_class = FormacionComform
    template_name = 'FormacionComplementaria/CreateFormacionComplementaria.html'
    success_url = reverse_lazy('FormacionComplementaria:lista_Formacion_Complementaria')
    def get_context_data(self, **kwargs):
        context = super(CreateFormacion_Complementaria, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Investigador.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context

class ListFormacion_Complementaria(ListView):
    model = formacion_complementaria
    template_name = 'FormacionComplementaria/ListFormacionComplementaria.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(ListFormacion_Complementaria, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Investigador.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context

class UpdateFormacion_Complementaria (UpdateView):
    model = formacion_complementaria
    form_class = FormacionComform
    template_name = 'FormacionComplementaria/UpdateFormacionComplementaria.html'
    success_url = reverse_lazy ('FormacionComplementaria:lista_Formacion_Complementaria')
    def get_context_data(self, **kwargs):
        context = super(UpdateFormacion_Complementaria, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Investigador.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context

class DeleteFormacion_Complementaria (DeleteView):
    model = formacion_complementaria
    template_name = 'FormacionComplementaria/DeleteFormacionComplementaria.html'
    success_url = reverse_lazy('FormacionComplementaria:lista_Formacion_Complementaria')
    def get_context_data(self, **kwargs):
        context = super(DeleteFormacion_Complementaria, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Investigador.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context