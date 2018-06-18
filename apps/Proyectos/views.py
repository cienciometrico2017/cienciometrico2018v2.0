from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.autoresProyecto.models import autoresProyecto
from apps.Linea_Investigacion.models import linea_investigacion
from apps.Proyectos.form import DocumentForm
from apps.Proyectos.models import proyecto
from django.views.generic import ListView,DeleteView
from apps.Investigador.models import Investigador
from apps.Sub_Lin_Investigacion.models import sub_lin_investigacion
from apps.autoresArticulos.models import autoresArticulos
from apps.palabraClave.models import palabraClave
from apps.roles.models import Rol
import unicodedata

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn'))
    return s

def Proyectocrear(request):

    if request.method == 'POST':
        usuario = request.user.id
        form = DocumentForm(request.POST, request.FILES)
        p = request.POST.getlist('palabraC')
        palabras = []
        for i in p:
            palabras.append(elimina_tildes(i.lower()))
        palabras = list(set(palabras))
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.save()
            form.save_m2m()
            for i in range(50):
                grado = f"grado{i}"
                user = f"user{i}"
                if grado in request.POST:
                    a = request.POST[grado]
                    obj = User.objects.get(pk=int(request.POST[user]))
                    autor = autoresProyecto.objects.create(gradoAutoria=a, proyecto=proyecto, user=obj)
                    autor.save()
                    del autor
            for i in palabras:
                if not palabraClave.objects.filter(Termino__iexact=i):
                    us = User.objects.get(pk=usuario)
                    palabraNew = palabraClave.objects.create(Termino=i, user=us)
                    proyecto.palabrasClaves.add(palabraNew)
                    del palabraNew
                else:
                    palabra = palabraClave.objects.get(Termino__iexact=i)
                    proyecto.palabrasClaves.add(palabra)
            proyecto.save()
            messages.success(request, ('Se ha registrado la información correctamente'))
            return redirect('proyecto:proyectos_lis')
    else:
        form = DocumentForm()
    return render(request, 'proyecto/proyectos_crear.html', {
        'form': form, 'us': User.objects.all(), 'linea': linea_investigacion.objects.all(),'subLinea': sub_lin_investigacion.objects.all(), 'perfil': Investigador.objects.get(user_id=request.user.id)
    })

class ProyectoList(ListView):
    model = proyecto
    template_name = 'proyecto/proyectos_listar.html'
    #paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(ProyectoList, self).get_context_data(**kwargs)
        #articulo = proyecto.objects.all()
        us = User.objects.get(id=self.request.user.id)
        aut = autoresProyecto.objects.filter(user=us)
        l = []
        for i in aut:
            l.append(i.proyecto.id)
        p = proyecto.objects.filter(id__in=l)
        perfil = Investigador.objects.get(user_id=self.request.user.id)
        context['perfil'] = perfil
        context['proyecto'] = p
        return context

def ProyectoEdit(request, id_proyecto):
    proy = proyecto.objects.get(id=id_proyecto)
    usuario = request.user.id
    pro = proyecto.objects.get(id=id_proyecto)
    autores = autoresProyecto.objects.filter(proyecto=proy).order_by('id')
    palabra = [val.id for val in pro.palabrasClaves.all()]
    perfil = Investigador.objects.get(user_id=usuario)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=proy)
        p = request.POST.getlist('palabraC')
        palabras = []
        for i in p:
            palabras.append(elimina_tildes(i.lower()))
        palabras = list(set(palabras))
        print("aqui")
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            form.save_m2m()
            for i in palabras:
                if not palabraClave.objects.filter(Termino__iexact=i):
                    us = User.objects.get(pk=usuario)
                    palabraNew = palabraClave.objects.create(Termino=i, user=us)
                    project.palabrasClaves.add(palabraNew)
                    del palabraNew
                    print(i)
                else:
                    print(i)
                    palabra = palabraClave.objects.get(Termino__iexact=i)
                    project.palabrasClaves.add(palabra)
            au = autoresProyecto.objects.filter(proyecto=project)
            for i in au:
                i.delete()
            for i in range(50):
                grado = f"grado{i}"
                user = f"user{i}"
                if grado in request.POST:
                    a = request.POST[grado]
                    obj = User.objects.get(pk=int(request.POST[user]))
                    autor = autoresProyecto.objects.create(gradoAutoria=a, proyecto=project, user=obj)
                    autor.save()
                    del autor
            project.save()
            messages.success(request, ('Se ha actualizado la información correctamente'))
            return redirect('proyecto:proyectos_lis')
    else:
        form = DocumentForm(instance=proy)
    return render(request, 'proyecto/proyectos_update.html', {
        'form': form,
        'linea': linea_investigacion.objects.all(),
        'subLinea': sub_lin_investigacion.objects.all(),
        'palabra': palabraClave.objects.filter(id__in=palabra),
        'us': User.objects.all(),
        'Autores': autores,
        'id': id_proyecto,
        'perfil': perfil
    })

class ProyectoDelete(DeleteView):
    model = proyecto
    template_name = 'proyecto/proyectos_delete.html'
    success_url = reverse_lazy('proyecto:proyectos_lis')
    def get_context_data(self, **kwargs):
        context = super(ProyectoDelete, self).get_context_data(**kwargs)
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

