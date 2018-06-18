from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.ciudad.form import CiudadForm
from apps.ciudad.models import ciudad
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
# Create your views here.
"""
class CantonList(ListView):
    model = canton
    template_name = 'ciudad/canton_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(CantonList, self).get_context_data(**kwargs)
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
class CantonCreate(CreateView):
    model = canton
    form_class = CantonForm
    template_name = 'ciudad/canton_crear.html'
    success_url = reverse_lazy('ciudad:canton_listar')
    def get_context_data(self, **kwargs):
        context = super(CantonCreate, self).get_context_data(**kwargs)
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
class CantonUpdate(UpdateView):
    model = canton
    form_class =CantonForm
    template_name = 'ciudad/canton_update.html'
    success_url = reverse_lazy('ciudad:canton_listar')
    def get_context_data(self, **kwargs):
        context = super(CantonUpdate, self).get_context_data(**kwargs)
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
class CantonDelete(DeleteView):
    model = canton
    template_name = 'ciudad/canton_delete.html'
    success_url = reverse_lazy('ciudad:canton_listar')
    def get_context_data(self, **kwargs):
        context = super(CantonDelete, self).get_context_data(**kwargs)
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
"""