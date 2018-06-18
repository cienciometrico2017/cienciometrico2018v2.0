# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from apps.facultad.models import facultad
from apps.facultad.form import FacultadForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from apps.pais.models import pais
from apps.zona.models import zona
from apps.universidad.models import universidad
from apps.campus.models import campus
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from apps.roles.models import Rol
from apps.Investigador.models import Investigador
# Create your views here.

class CreateFacultad (CreateView):
    model = facultad
    form_class = FacultadForm
    template_name = 'Facultad/CreateFacultad.html'
    success_url = reverse_lazy('Facultad:lista_Facultad')
    def get_context_data(self, **kwargs):
        context = super(CreateFacultad, self).get_context_data(**kwargs)
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
    @method_decorator(permission_required('facultad.add_facultad', reverse_lazy('Facultad:lista_Facultad')))
    def dispatch(self, *args, **kwargs):
        return super(CreateFacultad, self).dispatch(*args, **kwargs)

class ListFacultad(ListView):
    model = facultad
    template_name = 'Facultad/ListFacultad.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(ListFacultad, self).get_context_data(**kwargs)
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
    @method_decorator(permission_required('facultad.ver_facultad', reverse_lazy('inicio:logeo')))
    def dispatch(self, *args, **kwargs):
        return super(ListFacultad, self).dispatch(*args, **kwargs)
class UpdateFacultad (UpdateView):
    model = facultad
    form_class = FacultadForm
    template_name = 'Facultad/UpdateFacultad.html'
    success_url = reverse_lazy ('Facultad:lista_Facultad')

    def get_context_data(self, **kwargs):
        context = super(UpdateFacultad, self).get_context_data(**kwargs)
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
    @method_decorator(permission_required('facultad.change_facultad', reverse_lazy('Facultad:lista_Facultad')))
    def dispatch(self, *args, **kwargs):
        return super(UpdateFacultad, self).dispatch(*args, **kwargs)

class DeleteFacultad (DeleteView):
    model = facultad
    template_name = 'Facultad/DeleteFacultad.html'
    success_url = reverse_lazy('Facultad:lista_Facultad')

    def get_context_data(self, **kwargs):
        context = super(DeleteFacultad, self).get_context_data(**kwargs)
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
def Facultadcrear(request):
    Pais = pais.objects.all()
    Zona= zona.objects.all()
    Universidad=universidad.objects.all()
    Campus=campus.objects.all()
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
        form= FacultadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Facultad:lista_Facultad')
    else:
        form= FacultadForm()
    return render(request,'Facultad/CreateFacultad.html',{'form':form,'Pais': Pais,'Zona': Zona, 'Universidad':Universidad, 'Campus':Campus, 'usuario': privilegio})
def Facultadedit(request, id_facultad):
    Pa = pais.objects.all()
    Zo = zona.objects.all()
    Uni = universidad.objects.all()
    Cam = campus.objects.all()
    fac = facultad.objects.get(id=id_facultad)
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
    if request.method == 'GET':
        form= FacultadForm(instance=fac)
    else:
        form = FacultadForm(request.POST, instance=fac)
        if form.is_valid():
            form.save()
        return redirect('Facultad:lista_Facultad')
    return render(request, 'Facultad/UpdateFacultad.html',{'form':form,'Pa': Pa,'Zo': Zo, 'Uni':Uni, 'Cam':Cam, 'usuario': privilegio})