# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unicodedata
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.shortcuts import render
from pip._vendor.appdirs import unicode
from django.template.loader import render_to_string
from apps.Articulos_Cientificos.models import articulos_cientificos
from apps.Articulos_Cientificos.form import articuloform
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.roles.models import Rol
from apps.Investigador.models import Investigador
from apps.autoresArticulos.models import autoresArticulos
from apps.autoresArticulos.form import autoresForm
from django.contrib.auth.models import User
from apps.palabraClave.models import palabraClave
from apps.Linea_Investigacion.models import linea_investigacion
from apps.Sub_Lin_Investigacion.models import sub_lin_investigacion
from apps.Revista.models import revista
from apps.baseDatos.models import baseDatos

from django.http import JsonResponse, HttpResponse


# Create your views here.

def index(request):
    objs = palabraClave.objects.all().values('Termino')
    onjsList = list(objs)
    return JsonResponse(onjsList, safe=False)


def deleteArt(request, idArt):
    articulo = articulos_cientificos.objects.get(id = idArt)
    autoresArticulos.objects.filter(articulo = articulo).delete()
    articulo.delete()
    messages.success(request, ('Artículo eliminado.'))
    return HttpResponseRedirect(reverse_lazy('articulosCientificos:ListaArticulo'))



def listarArticulo(request):
    return render(request, 'ArticuloCientifico/ListarArticulos.html')


def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn'))
    return s


class articulocreate(CreateView):
    model = articulos_cientificos
    model_second = autoresArticulos
    form_class = articuloform
    template_name = 'ArticuloCientifico/ArticulosCientificos.html'
    success_url = reverse_lazy('articulosCientificos:ListaArticulo')
    def get_context_data(self, **kwargs):
        context = super(articulocreate, self).get_context_data(**kwargs)
        perfil = Investigador.objects.get(user_id=self.request.user.id)
        US = []
        for i in User.objects.all():
            US.append(i)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['us'] = User.objects.all()
        context['linea'] = linea_investigacion.objects.all()
        context['subLinea'] = sub_lin_investigacion.objects.all()
        context['base'] = baseDatos.objects.all()
        context['revista'] = revista.objects.all()
        context['perfil'] = perfil
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        usuario = self.request.user.id
        form = self.form_class(request.POST, request.FILES)
        p = request.POST.getlist('palabraC')
        palabras = []
        for i in p:
            palabras.append(elimina_tildes(i.lower()))
        palabras = list(set(palabras))
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.save()
            form.save_m2m()
            for i in range(5):
                grado = f"grado{i}"
                user = f"user{i}"
                print(user)
                if grado in request.POST:
                    a = request.POST[grado]
                    obj = User.objects.get(pk=int(request.POST[user]))
                    autor = autoresArticulos.objects.create(gradoAutoria=a, articulo=articulo, user=obj)
                    autor.save()
                    del autor
            for i in palabras:
                if not palabraClave.objects.filter(Termino__iexact=i):
                    us = User.objects.get(pk=usuario)
                    palabraNew = palabraClave.objects.create(Termino=i, user=us)
                    articulo.palabraClave.add(palabraNew)
                    del palabraNew
                else:
                    palabra = palabraClave.objects.get(Termino__iexact=i)
                    articulo.palabraClave.add(palabra)
            articulo.save()
            messages.success(request, ('Se ha registrado el articulo correctamente'))
            return HttpResponseRedirect(reverse_lazy('articulosCientificos:ListaArticulo'))
        else:
            messages.error(request, ('AH ocurrido un error, revise la informacion del formulario.'))
            return self.render_to_response(self.get_context_data(form=form))


class articuloUpdate(UpdateView):
    model = articulos_cientificos
    form_class = articuloform
    template_name = 'ArticuloCientifico/UpdateArticulo.html'
    success_url = reverse_lazy('articulosCientificos:ListaArticulo')
    def get_context_data(self, **kwargs):
        context = super(articuloUpdate, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        ArticuloID = self.object.id
        articulo = articulos_cientificos.objects.get(id=ArticuloID)
        basesD = [val.id for val in articulo.baseDatos.all()]
        autores =  autoresArticulos.objects.filter(articulo = articulo)
        if not  autoresArticulos.objects.filter(articulo = articulo, user_id = self.request.user.id):
            context['permisos'] = 'invalido'

        perfil = Investigador.objects.get(user_id=self.request.user.id)
        palabra = [val.id for val in articulo.palabraClave.all()]
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        context['us'] = User.objects.all()
        context['Autores'] = autoresArticulos.objects.filter(id__in=autores)
        context['Datos'] = baseDatos.objects.exclude(id__in=basesD)
        # context['revEx'] = revista.objects.exclude(id__in=rev)
        context['palabra'] = palabraClave.objects.filter(id__in=palabra)
        context['linea'] = linea_investigacion.objects.all()
        context['subLinea'] = sub_lin_investigacion.objects.all()
        context['base'] = baseDatos.objects.all()
        context['revista'] = revista.objects.all()
        context['id'] = ArticuloID
        context['perfil'] = perfil
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        usuario = self.request.user.id
        id_art = kwargs['pk']
        art = self.model.objects.get(id=id_art)
        form = self.form_class(request.POST, request.FILES, instance=art)
        p = request.POST.getlist('palabras')
        palabras = []
        for i in p:
            palabras.append(elimina_tildes(i.lower()))
        palabras = list(set(palabras))
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.save()
            form.save_m2m()
            for i in palabras:
                if not palabraClave.objects.filter(Termino__iexact=i):
                    us = User.objects.get(pk=usuario)
                    palabraNew = palabraClave.objects.create(Termino=i, user=us)
                    articulo.palabraClave.add(palabraNew)
                    del palabraNew
                else:
                    palabra = palabraClave.objects.get(Termino__iexact=i)
                    articulo.palabraClave.add(palabra)
            au = autoresArticulos.objects.filter(articulo = art)
            for i in au:
                i.delete()
            for i in range(6):
                grado = f"grado{i}"
                user = f"user{i}"
                if grado in request.POST:
                    a = request.POST[grado]
                    obj = User.objects.get(pk=int(request.POST[user]))

                    autor = autoresArticulos.objects.create(gradoAutoria=a, articulo=articulo, user=obj)
                    autor.save()
                    del autor
            articulo.save()
            messages.success(request, ('Se ha actualizado la información del articulo correctamente'))
            return HttpResponseRedirect(reverse_lazy('articulosCientificos:ListaArticulo'))
        else:
            messages.error(request, ('Ah ocurrido un error, revise la informacion del formulario.'))
            return self.render_to_response(self.get_context_data(form=form))


class articuloDelete(DeleteView):
    model = articulos_cientificos
    template_name = 'ArticuloCientifico/DeleteArticulo.html'
    success_url = reverse_lazy('articulosCientificos:ListaArticulo')
    def get_context_data(self, **kwargs):
        context = super(articuloDelete, self).get_context_data(**kwargs)
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


class articuloList(ListView):
    model = articulos_cientificos
    template_name = 'ArticuloCientifico/ListarArticulos.html'
    # paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(articuloList, self).get_context_data(**kwargs)
        perfil = Investigador.objects.get(user_id=self.request.user.id)
        us = User.objects.get(id = self.request.user.id)
        aut = autoresArticulos.objects.filter(user = us)
        l = []
        for i in aut:
            l.append(i.articulo.id)
        articulo = articulos_cientificos.objects.filter(id__in = l)
        context['articulo'] = articulo
        context['perfil'] = perfil
        return context
