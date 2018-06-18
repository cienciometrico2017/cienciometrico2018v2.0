# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from apps.Evento.models import evento
from apps.Evento.form import EventoForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
# Create your views here.

class CreateEvento (CreateView):
    model = evento
    form_class = EventoForm
    template_name = 'Evento/CreateEvento.html'
    success_url = reverse_lazy('evento:lista_Evento')
    def get_context_data(self, **kwargs):
        context = super(CreateEvento, self).get_context_data(**kwargs)
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


class ListEvento(ListView):
    model = evento
    template_name = 'Evento/ListEvento.html'
    def get_context_data(self, **kwargs):
        context = super(ListEvento, self).get_context_data(**kwargs)
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
class UpdateEvento (UpdateView):
    model = evento
    form_class = EventoForm
    template_name = 'Evento/UpdateEvento.html'
    success_url = reverse_lazy ('evento:lista_Evento')
    def get_context_data(self, **kwargs):
        context = super(UpdateEvento, self).get_context_data(**kwargs)
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

class DeleteEvento (DeleteView):
    model = evento
    template_name = 'Evento/DeleteEvento.html'
    success_url = reverse_lazy('evento:lista_Evento')
    def get_context_data(self, **kwargs):
        context = super(DeleteEvento, self).get_context_data(**kwargs)
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