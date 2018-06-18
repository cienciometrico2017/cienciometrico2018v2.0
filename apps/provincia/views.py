from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.provincia.form import ProvinciaForm
from apps.provincia.models import provincia
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
from apps.pais.models import pais
from apps.zona.models import zona
# Create your views here.
class ProvinciaList(ListView):
    model = provincia
    template_name = 'provincia/provincia_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(ProvinciaList, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Investigador.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio= []
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
class ProvinciaCreate(CreateView):
    model = provincia
    form_class = ProvinciaForm
    template_name = 'provincia/provincia_crear.html'
    success_url = reverse_lazy('provincia:provincia_listar')
    def get_context_data(self, **kwargs):
        context = super(ProvinciaCreate, self).get_context_data(**kwargs)
        Pais = pais.objects.all()
        Zona = zona.objects.all()

        usuario = self.request.user.id
        perfil = Investigador.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio= []
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
        context['Pais'] = Pais
        context['Zona'] = Zona
        return context
class ProvinciaUpdate(UpdateView):
    model = provincia
    form_class = ProvinciaForm
    template_name = 'provincia/provincia_update.html'
    success_url = reverse_lazy('provincia:provincia_listar')
    def get_context_data(self, **kwargs):
        context = super(ProvinciaUpdate, self).get_context_data(**kwargs)
        Pais = pais.objects.all()
        Zona = zona.objects.all()
        usuario = self.request.user.id
        perfil = Investigador.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio= []
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
        context['Pais'] = Pais
        context['Zona'] = Zona
        return context
class ProvinciaDelete(DeleteView):
    model = provincia
    template_name = 'provincia/provincia_delete.html'
    success_url = reverse_lazy('provincia:provincia_listar')
    def get_context_data(self, **kwargs):
        context = super(ProvinciaDelete, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Investigador.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio= []
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
