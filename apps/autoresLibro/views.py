from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from apps.Libro.models import libro
from apps.Proyectos.models import proyecto
from apps.autoresProyecto.models import autoresProyecto
from apps.autoresArticulos.models import autoresArticulos
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
from apps.Articulos_Cientificos.models import articulos_cientificos
from django.contrib import messages

def eliminar (request, idArt ,id):
    articulo = articulos_cientificos.objects.get(id = id)
    art = autoresArticulos.objects.filter(articulo = articulo)
    autor = autoresArticulos.objects.get(id = idArt)
    if art.count() == 1:
        messages.error(request, ('No se puede completar la solicitud, debe contener al menos un autor.'))
        return HttpResponseRedirect('/articulo/UpdateArticulos/%s/' % id)
    else:
        autor.delete()
        messages.success(request, ('El autor fue removido del artículo.'))
        return HttpResponseRedirect('/articulo/UpdateArticulos/%s/' % id)

def eliminarBook (request, idArt ,id):
    book = libro.objects.get(id = id)
    autor = autoresArticulos.objects.get(id = idArt)
    if book.autores.count() == 1:
        messages.error(request, ('No se puede completar la solicitud, debe contener al menos un autor.'), extra_tags='alert')
        return HttpResponseRedirect('/libro/editar/%s/' % id)
    else:
        book.autores.remove(autor)
        book.save()
        messages.success(request, ('El autor fue removido del libro.'), extra_tags='alert')
        return HttpResponseRedirect('/libro/editar/%s/' % id)

def eliminarProj (request, idArt ,id):
    pro = proyecto.objects.get(id = id)
    autor = autoresProyecto.objects.get(id = idArt)
    if pro.integrantes.count() == 1:
        messages.error(request, ('No se puede completar la solicitud, debe contener al menos un autor.'), extra_tags='alert')
        return HttpResponseRedirect('/proyectos/editar/%s/' % id)
    else:
        pro.integrantes.remove(autor)
        pro.save()
        messages.success(request, ('El autor fue removido del libro.'), extra_tags='alert')
        return HttpResponseRedirect('/proyectos/editar/%s/' % id)
