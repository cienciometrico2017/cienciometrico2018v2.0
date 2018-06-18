# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from apps.Formacion_Academica.models import formacion_academica
from apps.Formacion_Academica.form import FormacionAform
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from apps.roles.models import Rol
from apps.Investigador.models import Investigador
# Create your views here.

class CreateFormacion_Academica (CreateView):
    model = formacion_academica
    form_class = FormacionAform
    template_name = 'FormacionAcademica/CreateFormacionAcademica.html'
    success_url = reverse_lazy('FormacionAcademica:lista_Formacion_Academica')
    def get_context_data(self, **kwargs):
        context = super(CreateFormacion_Academica, self).get_context_data(**kwargs)
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

class ListFormacion_Academica(ListView):
    model = formacion_academica
    template_name = 'FormacionAcademica/ListFormacionAcademica.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(ListFormacion_Academica, self).get_context_data(**kwargs)
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

class UpdateFormacion_Academica (UpdateView):
    model = formacion_academica
    form_class = FormacionAform
    template_name = 'FormacionAcademica/UpdateFormacionAcademica.html'
    success_url = reverse_lazy ('inicio:logeo')
    def get_context_data(self, **kwargs):
        context = super(UpdateFormacion_Academica, self).get_context_data(**kwargs)
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

class DeleteFormacion_Academica (DeleteView):
    model = formacion_academica
    template_name = 'FormacionAcademica/DeleteFormacionAcademica.html'
    success_url = reverse_lazy('inicio:logeo')
    def get_context_data(self, **kwargs):
        context = super(DeleteFormacion_Academica, self).get_context_data(**kwargs)
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