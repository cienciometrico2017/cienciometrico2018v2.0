from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.informacionLaboral.form import infLabForm
from apps.informacionLaboral.models import informacionLaboral
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol

# Create your views here.
class PaisList(ListView):
    model = informacionLaboral
    template_name = 'pais/pais_listar.html'


    def get_context_data(self, **kwargs):
        context = super(PaisList, self).get_context_data(**kwargs)
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

class PaisCreate(CreateView):
    model = informacionLaboral
    form_class = infLabForm
    template_name = 'pais/pais_crear.html'
    success_url = reverse_lazy('pais:pais_listar')
    def get_context_data(self, **kwargs):
        context = super(PaisCreate, self).get_context_data(**kwargs)
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
class PaisUpdate(UpdateView):
    model = informacionLaboral
    form_class = infLabForm
    template_name = 'pais/pais_update.html'
    success_url = reverse_lazy('pais:pais_listar')
    def get_context_data(self, **kwargs):
        context = super(PaisUpdate, self).get_context_data(**kwargs)
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
class PaisDelete(DeleteView):
    model = informacionLaboral
    template_name = 'pais/pais_eliminar.html'
    success_url = reverse_lazy('pais:pais_listar')
    def get_context_data(self, **kwargs):
        context = super(PaisDelete, self).get_context_data(**kwargs)
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