# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from apps.Publicaciones.models import publicaciones
from apps.Publicaciones.form import formPublicaciones
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from apps.roles.models import Rol
from apps.Investigador.models import Investigador
# Create your views here.

def CreatePublicaciones(request):
    usuario = request.user.id
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
    if request.method == 'POST':
        form = formPublicaciones(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publicaciones:lista_Publicaciones')
    else:
        form = formPublicaciones()
    return render(request, 'Publicaciones/CreatePublicaciones.html', {
        'form': form, 'usuario': privilegio
    })

class ListPublicaciones(ListView):
    model = publicaciones
    template_name = 'Publicaciones/ListPublicaciones.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(ListPublicaciones, self).get_context_data(**kwargs)
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

def UpdatePublicaciones(request, id_publicaciones):
    usuario = request.user.id
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
    proy = publicaciones.objects.get(id=id_publicaciones)
    if request.method == 'POST':
        form = formPublicaciones(request.POST, request.FILES,instance=proy)
        if form.is_valid():
            form.save()
            return redirect('publicaciones:lista_Publicaciones')
    else:
        form = formPublicaciones(instance=proy)
    return render(request, 'Publicaciones/UpdatePublicaciones.html', {'form': form, 'usuario': privilegio})

class DeletePublicaciones (DeleteView):
    model = publicaciones
    template_name = 'Publicaciones/DeletePublicaciones.html'
    success_url = reverse_lazy('publicaciones:lista_Publicaciones')
    def get_context_data(self, **kwargs):
        context = super(DeletePublicaciones, self).get_context_data(**kwargs)
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