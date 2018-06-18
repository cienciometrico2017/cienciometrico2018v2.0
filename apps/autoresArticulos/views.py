from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from apps.Libro.models import libro
from apps.Proyectos.models import proyecto
from apps.autoresLibro.models import autoresLibro
from apps.autoresArticulos.models import autoresArticulos
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.autoresProyecto.models import autoresProyecto
from apps.roles.models import Rol
from apps.Articulos_Cientificos.models import articulos_cientificos
from django.contrib import messages
import json

def eliminar (request, idArt ,id):
    us = []
    articulo = articulos_cientificos.objects.get(id = id)
    art = autoresArticulos.objects.filter(articulo = articulo).all()
    for i in art:
        us.append(i.gradoAutoria)
    us = us[:-1]
    t = len(us)
    if art.count() == 1:
        messages.error(request, ('No se puede completar la solicitud, debe contener al menos un autor.'))
        return HttpResponseRedirect('/articulo/UpdateArticulos/%s/' % id)
    else:
        autor = autoresArticulos.objects.get(id=idArt)
        autor.delete()
        art2 = autoresArticulos.objects.filter(articulo = articulo).all()
        for i in art2:
            print(i)
        for i in range(t):
            art2[i].gradoAutoria = us[i]
            art2[i].save()
        messages.success(request, ('El autor fue removido del artículo.'))
        return HttpResponseRedirect('/articulo/UpdateArticulos/%s/' % id)

def eliminarBook (request, idArt ,id):
    us = []
    book = libro.objects.get(id=id)
    art = autoresLibro.objects.filter(libro=book).all()
    for i in art:
        us.append(i.gradoAutoria)
    us = us[:-1]
    for i in us:
        print(i)
    t = len(us)

    if art.count() == 1:
        messages.error(request, ('No se puede completar la solicitud, debe contener al menos un autor.'))
        return HttpResponseRedirect('/articulo/UpdateArticulos/%s/' % id)
    else:
        autor = autoresLibro.objects.get(id=idArt)
        autor.delete()
        art2 = autoresLibro.objects.filter(libro=book).all()
        for i in art2:
            print(i)
        for i in range(t):
            art2[i].gradoAutoria = us[i]
            art2[i].save()
        messages.success(request, ('El autor fue removido del artículo.'))
        return HttpResponseRedirect('/libro/editar/%s/' % id)


def eliminarProj (request, idArt ,id):
    us = []
    pro = proyecto.objects.get(id=id)
    art = autoresProyecto.objects.filter(proyecto=pro).all()
    if art.count() == 1:
        messages.error(request, ('No se puede completar la solicitud, debe contener al menos un autor.'))
        return HttpResponseRedirect('/proyectos/editar/%s/' % id)
    else:
        art2 = autoresProyecto.objects.get(proyecto=pro, id=idArt)
        art2.delete()
        messages.success(request, ('El autor fue removido del libro.'))
        return HttpResponseRedirect('/proyectos/editar/%s/' % id)

def selAA (request):

    if request.is_ajax:
        bd = User.objects.all()
        results = []
        doctor_json = {}
        doctor_json['text'] = '----------'
        doctor_json['value'] = ''
        results.append(doctor_json)
        for i in bd:
            doctor_json = {}
            doctor_json['text'] = i.first_name + ' ' + i.last_name
            doctor_json['value'] = i.id
            results.append(doctor_json)
        data_json = json.dumps(results)
    else:
        data_json = 'fail'
    mimetype = "application/json"
    return HttpResponse(data_json, mimetype)
