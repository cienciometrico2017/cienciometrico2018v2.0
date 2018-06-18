from django.shortcuts import render
from apps.datosprofesionales.models import datos_profecionales
from django.core.urlresolvers import reverse_lazy
from apps.datosprofesionales.form import DatosProfeForm
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
# Create your views here.
class DatosProfeList(ListView):
    model = datos_profecionales
    template_name = 'DatosProfesionales/profesionales_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(DatosProfeList, self).get_context_data(**kwargs)
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

class DatosProfeCreate(CreateView):
    model = datos_profecionales
    form_class = DatosProfeForm
    template_name = 'DatosProfesionales/profesionales_crear.html'
    success_url = reverse_lazy('datosprofe:datosprofe_listar')
    def get_context_data(self, **kwargs):
        context = super(DatosProfeCreate, self).get_context_data(**kwargs)
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
        context['perfil'] = perfil
        return context
class DatosProfeUpdate(UpdateView):
    model = datos_profecionales
    form_class = DatosProfeForm
    template_name = 'DatosProfesionales/profesionales_update.html'
    success_url = reverse_lazy('datosprofe:datosprofe_listar')
    def get_context_data(self, **kwargs):
        context = super(DatosProfeUpdate, self).get_context_data(**kwargs)
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
        context['perfil'] = perfil
        return context
class DatosProfeDelete(DeleteView):
    model = datos_profecionales
    template_name = 'DatosProfesionales/profesionales_delete.html'
    success_url = reverse_lazy('datosprofe:datosprofe_listar')
    def get_context_data(self, **kwargs):
        context = super(DatosProfeDelete, self).get_context_data(**kwargs)
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
