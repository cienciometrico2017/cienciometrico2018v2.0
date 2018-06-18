# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from apps.carrera.models import carrera
from apps.carrera.form import CarreraForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from apps.pais.models import pais
from apps.zona.models import zona
from apps.universidad.models import universidad
from apps.campus.models import campus
from apps.facultad.models import facultad
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
# Create your views here.

class CreateCarrera (CreateView):
    model = carrera
    form_class = CarreraForm
    template_name = 'carrera/Createcarrera.html'
    success_url = reverse_lazy('carrera:lista_Carrera')
    def get_context_data(self, **kwargs):
        context = super(CreateCarrera, self).get_context_data(**kwargs)
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
class ListCarrera(ListView):
    model = carrera
    template_name = 'carrera/Listcarrera.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(ListCarrera, self).get_context_data(**kwargs)
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
class UpdateCarrera (UpdateView):
    model = carrera
    form_class = CarreraForm
    template_name = 'carrera/Updatecarrera.html'
    success_url = reverse_lazy ('carrera:lista_Carrera')
    def get_context_data(self, **kwargs):
        context = super(UpdateCarrera, self).get_context_data(**kwargs)
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
class DeleteCarrera (DeleteView):
    model = carrera
    template_name = 'carrera/Deletecarrera.html'
    success_url = reverse_lazy('carrera:lista_Carrera')
    def get_context_data(self, **kwargs):
        context = super(DeleteCarrera, self).get_context_data(**kwargs)
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
def Carreracrear(request):
    Pais = pais.objects.all()
    Zona= zona.objects.all()
    Universidad=universidad.objects.all()
    Campus=campus.objects.all()
    Facultad = facultad.objects.all()
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
        form= CarreraForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('carrera:lista_Carrera')
    else:
        form= CarreraForm()
    return render(request,'carrera/CreateCarrera.html',{'form':form,'Pais': Pais,'Zona': Zona, 'Universidad':Universidad, 'Campus':Campus,'Facultad':Facultad, 'usuario': privilegio})
def Carreradedit(request, id_carrera):
    Pais = pais.objects.all()
    Zona = zona.objects.all()
    Universidad = universidad.objects.all()
    Campus = campus.objects.all()
    Facultad = facultad.objects.all()
    carr = carrera.objects.get(id=id_carrera)
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
        form= CarreraForm(instance=carr)
    else:
        form = CarreraForm(request.POST, instance=carr)
        if form.is_valid():
            form.save()
        return redirect('carrera:lista_Carrera')
    return render(request, 'carrera/UpdateCarrera.html',{'form':form,'Pais': Pais,'Zona': Zona, 'Universidad':Universidad, 'Campus':Campus,'Facultad':Facultad, 'usuario': privilegio})