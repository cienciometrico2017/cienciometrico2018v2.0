from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from apps.capacitacion.form import CapacitacionForm
from apps.capacitacion.models import capacitacion
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol

# Create your views here.
class CapacitacionList(ListView):
    model = capacitacion
    template_name = 'capacitacion/capacitacion_listar.html'
    def get_context_data(self, **kwargs):
        usuario = self.request.user.id
        context = super(CapacitacionList, self).get_context_data(**kwargs)
        try:
            capa = capacitacion.objects.filter(user_id=usuario)
        except capacitacion.DoesNotExist:
            capa = None
        usuario = self.request.user.id
        context['perfil'] = Investigador.objects.get(user_id=self.request.user.id)
        context['capa'] = capa
        return context

class CapacitacionCreate(CreateView):
    model = capacitacion
    form_class = CapacitacionForm
    template_name = 'capacitacion/capacitacion_crear.html'
    success_url = reverse_lazy('capacitacion:capacitacion_listar')
    #
    def get_context_data(self, **kwargs):
        context = super(CapacitacionCreate, self).get_context_data(**kwargs)
        usuario = self.request.user.id

        context['perfil'] = Investigador.objects.get(user_id=self.request.user.id)

        return context


class CapacitacionUpdate(UpdateView):
    model = capacitacion
    form_class = CapacitacionForm
    template_name = 'capacitacion/capacitacion_update.html'
    success_url = reverse_lazy('capacitacion:capacitacion_listar')
    def get_context_data(self, **kwargs):
        context = super(CapacitacionUpdate, self).get_context_data(**kwargs)
        usuario = self.request.user.id

        context['perfil'] = Investigador.objects.get(user_id=self.request.user.id)
        return context

class CapacitacionDelete(DeleteView):
    model = capacitacion
    template_name = 'capacitacion/capacitacion_eliminar.html'
    success_url = reverse_lazy('capacitacion:capacitacion_listar')
    def get_context_data(self, **kwargs):
        context = super(CapacitacionDelete, self).get_context_data(**kwargs)
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