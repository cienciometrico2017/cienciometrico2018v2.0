# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.Intereses_Formativos.form import InteresForm
from apps.Intereses_Formativos.models import intereses_formativos
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol

# Create your views here.
class InteresList(ListView):
    model = intereses_formativos
    template_name = 'interes/interes_listar.html'
    def get_context_data(self, **kwargs):
        context = super(InteresList, self).get_context_data(**kwargs)
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

class InteresCreate(CreateView):
    model = intereses_formativos
    form_class = InteresForm
    template_name = 'interes/interes_crear.html'
    success_url = reverse_lazy('interes:interes_listar')
    def get_context_data(self, **kwargs):
        context = super(InteresCreate, self).get_context_data(**kwargs)
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
class InteresUpdate(UpdateView):
    model = intereses_formativos
    form_class = InteresForm
    template_name = 'interes/interes_update.html'
    success_url = reverse_lazy('interes:interes_listar')
    def get_context_data(self, **kwargs):
        context = super(InteresUpdate, self).get_context_data(**kwargs)
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
class InteresDelete(DeleteView):
    model = intereses_formativos
    template_name = 'interes/interes_eliminar.html'
    success_url = reverse_lazy('interes:interes_listar')
    def get_context_data(self, **kwargs):
        context = super(InteresDelete, self).get_context_data(**kwargs)
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