from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect

from apps.Ponencia.form import PonenciaForm
from apps.Ponencia.models import ponencia
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.Investigador.models import Investigador
from apps.autoresPonencia.models import autoresPonencia
from apps.palabraClave.models import palabraClave
from apps.roles.models import Rol
from apps.Articulos_Cientificos.models import articulos_cientificos
# Create your views here.
import unicodedata

from apps.universidad.models import universidad


def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn'))
    return s

class PonenciaList(ListView):
    model = ponencia
    template_name = 'Ponencia/ponencia_listar.html'
    def get_context_data(self, **kwargs):
        context = super(PonenciaList, self).get_context_data(**kwargs)
        us = User.objects.get(id=self.request.user.id)
        aut = autoresPonencia.objects.filter(user=us)
        l = []
        for i in aut:
            l.append(i.ponencia.id)
        pon = ponencia.objects.filter(id__in=l)
        context['perfil'] = Investigador.objects.get(user_id=self.request.user.id)
        context['Pon'] = pon
        return context

class PonenciaCreate(CreateView):
    model = ponencia
    form_class = PonenciaForm
    template_name = 'ponencia/ponencia_crear.html'
    success_url = reverse_lazy('Ponencia:ponencia_listar')
    def get_context_data(self, **kwargs):
        context = super(PonenciaCreate, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        context['uni'] = universidad.objects.all()
        context['us'] = User.objects.all()
        context['articulos'] = articulos_cientificos.objects.all()
        context['perfil'] = Investigador.objects.get(user_id=self.request.user.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        usuario = self.request.user.id
        form = self.form_class(request.POST, request.FILES)
        p = request.POST.getlist('palabras')
        palabras = []
        for i in p:
            palabras.append(elimina_tildes(i.lower()))
        palabras = list(set(palabras))

        if form.is_valid():
            print("hola")
            pon = form.save(commit=False)
            pon.save()
            form.save_m2m()
            for i in palabras:
                if not palabraClave.objects.filter(Termino__iexact=i):
                    us = User.objects.get(pk=usuario)
                    palabraNew = palabraClave.objects.create(Termino=i, user=us)
                    pon.palabrasClave.add(palabraNew)
                    del palabraNew
                else:
                    palabra = palabraClave.objects.get(Termino__iexact=i)
                    pon.palabrasClave.add(palabra)
            for i in range(5):
                grado = f"grado{i}"
                user = f"user{i}"
                print(user)
                if grado in request.POST:
                    a = request.POST[grado]
                    obj = User.objects.get(pk=int(request.POST[user]))
                    autor = autoresPonencia.objects.create(gradoAutoria=a, ponencia=pon, user=obj)
                    autor.save()
                    del autor
            pon.save()
            messages.success(request, ('Se ha registrado la ponencia correctamente'))
            return HttpResponseRedirect(reverse_lazy('Ponencia:ponencia_listar'))
        else:
            messages.error(request, ('Por favor registrese nuevamente'))
            return self.render_to_response(self.get_context_data(form=form))


class PonenciaUpdate(UpdateView):
    model = ponencia
    form_class = PonenciaForm
    template_name = 'ponencia/ponencia_update.html'
    success_url = reverse_lazy('Ponencia:ponencia_listar')
    def get_context_data(self, **kwargs):
        context = super(PonenciaUpdate, self).get_context_data(**kwargs)
        ponenciaId = self.object.id
        pon = ponencia.objects.get(id=ponenciaId)
        palabra = [val.id for val in pon.palabrasClave.all()]
        articulo = [val.id for val in pon.articuloCientifico.all()]
        autores = autoresPonencia.objects.filter(ponencia=pon)
        context['us'] = User.objects.all()
        context['Autores'] = autores
        context['palabra'] = palabraClave.objects.filter(id__in=palabra)
        context['articulo'] =  articulos_cientificos.objects.exclude(id__in=articulo)
        context['articuloAll'] = articulos_cientificos.objects.all()
        context['uni'] = universidad.objects.all()
        context['perfil'] = Investigador.objects.get(user_id=self.request.user.id)

        return context
    def post(self, request, *args, **kwargs):
        usuario = self.request.user.id
        ponId = kwargs['pk']
        ponencia = self.model.objects.get(id=ponId)
        form = self.form_class(request.POST, request.FILES, instance=ponencia)
        p = request.POST.getlist('palabras')
        palabras = []
        for i in p:
            palabras.append(elimina_tildes(i.lower()))
        palabras = list(set(palabras))
        if form.is_valid():
            pon = form.save(commit=False)
            pon.save()
            form.save_m2m()
            for i in palabras:
                if not palabraClave.objects.filter(Termino__iexact=i):
                    us = User.objects.get(pk=usuario)
                    palabraNew = palabraClave.objects.create(Termino=i, user=us)
                    pon.palabrasClave.add(palabraNew)
                    del palabraNew
                    print(i)
                else:
                    print(i)
                    palabra = palabraClave.objects.get(Termino__iexact=i)
                    pon.palabrasClave.add(palabra)
                    pon.save()
            au = autoresPonencia.objects.filter(ponencia=pon)
            for i in au:
                i.delete()
            for i in range(6):
                grado = f"grado{i}"
                user = f"user{i}"
                if grado in request.POST:
                    a = request.POST[grado]
                    obj = User.objects.get(pk=int(request.POST[user]))

                    autor = autoresPonencia.objects.create(gradoAutoria=a, ponencia=pon, user=obj)
                    autor.save()
                    del autor

            messages.success(request, ('Se ha actualizado información correctamente'))
            return HttpResponseRedirect(reverse_lazy('Ponencia:ponencia_listar'))
        else:
            messages.error(request, ('Por favor revise la información del formulario'))
            return self.render_to_response(self.get_context_data(form=form))



class PonenciaDelete(DeleteView):
    model = ponencia
    template_name = 'ponencia/ponencia_eliminar.html'
    success_url = reverse_lazy('Ponencia:ponencia_listar')
    def get_context_data(self, **kwargs):
        context = super(PonenciaDelete, self).get_context_data(**kwargs)
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

