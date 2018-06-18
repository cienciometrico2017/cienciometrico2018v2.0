from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.pais.form import PaisForm
from apps.pais.models import pais
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
from django.http import HttpResponse
from apps.pais.models import pais
from apps.provincia.models import provincia
from apps.ciudad.models import ciudad
from apps.universidad.models import universidad
import json

# Create your views here.
def listSelectedItems(request):
    if request.method == 'POST':
        data = request.POST.get('datos')
        if data:
            country = pais.objects.get(id = data)
            state = provincia.objects.filter(pais = country)
            results = []
            doctor_json = {}
            doctor_json['text'] = '----------'
            doctor_json['value'] = ''
            results.append(doctor_json)
            for i in state:
                city = ciudad.objects.filter(provincia_id = i.id)
                for i in city:
                    doctor_json = {}
                    doctor_json['text'] = i.Nombre
                    doctor_json['value'] = i.id
                    results.append(doctor_json)
                    print(city)
            data_json = json.dumps(results)
        else:
            results = []
            doctor_json = {}
            doctor_json['text'] = '----------'
            doctor_json['value'] = ''
            results.append(doctor_json)
            data_json = json.dumps(results)

    else:
        data_json='fail'
    mimetype="application/json"
    return HttpResponse(data_json,mimetype)

# Create your views here.
def listPais(request):
    if request.method == 'POST':
        data = request.POST.get('datos')
        if data:
            country = pais.objects.get(id = data)
            university = universidad.objects.filter(pais = country).order_by('Nombre')
            results = []
            doctor_json = {}
            doctor_json['text'] = '----------'
            doctor_json['value'] = ''
            results.append(doctor_json)
            for i in university:
                doctor_json = {}
                doctor_json['text'] = i.Nombre
                doctor_json['value'] = i.id
                results.append(doctor_json)
            data_json = json.dumps(results)
        else:
            results = []
            doctor_json = {}
            doctor_json['text'] = '----------'
            doctor_json['value'] = ''
            results.append(doctor_json)
            data_json = json.dumps(results)

    else:
        data_json='fail'
    mimetype="application/json"
    return HttpResponse(data_json,mimetype)

class PaisList(ListView):
    model = pais
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
    model = pais
    form_class = PaisForm
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
    model = pais
    form_class = PaisForm
    template_name = 'pais/pais_update.html'

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
    model = pais
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