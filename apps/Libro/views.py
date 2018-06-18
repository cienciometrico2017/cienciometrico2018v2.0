from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.Libro.form import DocumentForm
from django.views.generic import ListView,DeleteView
from apps.Libro.models import libro
from apps.autoresArticulos.models import autoresArticulos
from apps.autoresLibro.models import autoresLibro
from apps.baseDatos.models import baseDatos
from apps.palabraClave.models import palabraClave
from apps.roles.models import Rol
from apps.Investigador.models import Investigador
import unicodedata

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn'))
    return s


class LibroList(ListView):
    model = libro
    template_name = 'libro/ListLibro.html'
    def get_context_data(self, **kwargs):
        context = super(LibroList, self).get_context_data(**kwargs)
        perfil = Investigador.objects.get(user_id=self.request.user.id)
        #book = libro.objects.all()
        us = User.objects.get(id=self.request.user.id)
        aut = autoresLibro.objects.filter(user=us)
        l = []
        for i in aut:
            l.append(i.libro.id)
        book = libro.objects.filter(id__in=l)
        """
        
        var = []
        for art in book:
            for aut in art.autores.all():
                if aut.user == self.request.user:
                    # print(aut.user)
                    var.append(art.id)
        artUser = libro.objects.filter(id__in=var)
        """
        context['perfil'] = perfil
        context['book'] = book
        return context

def Librocrear(request):
    usuario = request.user.id
    perfil = Investigador.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        p = request.POST.getlist('palabras')
        palabras = []
        for i in p:
            palabras.append(elimina_tildes(i.lower()))
        palabras = list(set(palabras))
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            for i in palabras:
                if not palabraClave.objects.filter(Termino__iexact=i):
                    us = User.objects.get(pk=usuario)
                    palabraNew = palabraClave.objects.create(Termino=i, user=us)
                    book.PalabrasClave.add(palabraNew)
                    del palabraNew
                else:
                    palabra = palabraClave.objects.get(Termino__iexact=i)
                    book.PalabrasClave.add(palabra)

            for i in range(20):
                grado = f"grado{i}"
                user = f"user{i}"
                if grado in request.POST:
                    a = request.POST[grado]
                    obj = User.objects.get(pk=int(request.POST[user]))
                    if a != 'Primero':
                        autor = autoresLibro.objects.create(gradoAutoria=a, libro=book, user=obj, capituloSel=False)
                        autor.save()
                    else:
                        autor = autoresLibro.objects.create(gradoAutoria=a, libro=book, user=obj, capituloSel=True)
                        autor.save()
                    del autor
            book.save()
            if request.POST['Aut'] == 'CoAutor':
                autorPos = autoresLibro.objects.get(libro_id = book.id, user_id = request.user.id)
                if "NumeroCap" or "Capitulo" in request.POST:
                    print(request.POST['NumeroCap'], request.POST['Capitulo'])
                    autorPos.capituloNumero = request.POST['NumeroCap']
                    autorPos.capituloTitulo = request.POST['Capitulo']
                    autorPos.capituloSel = False
                    autorPos.save()

            messages.success(request, ('Se ha registrado el libro correctamente'))
            return redirect('Libro:libro_lis')
        else:
            messages.error(request, ('Ah ocurrido un error vuelva a intentarlo'))
            return redirect('libro/libro_crear')

    else:
        form = DocumentForm()
    return render(request,'libro/CreateLibro.html', {
        'form': form, 'base' : baseDatos.objects.all(), 'us': User.objects.all(), 'perfil': perfil
    })



def LibroEdit(request, idLibro):
    usuario = request.user.id
    perfil = Investigador.objects.get(user_id=usuario)
    libros = libro.objects.get(id=idLibro)

    libroAutor = autoresLibro.objects.get(libro=libros, user=usuario)
    print(libroAutor.id)

    basesD = [val.id for val in libros.BaseDatos.all()]
    autores = autoresLibro.objects.filter(libro=libros)
    if not autoresLibro.objects.filter(libro=libros, user = usuario):
        permisos = 'No existe'
    else:
        gr1 = autoresLibro.objects.get(libro=libros, user=usuario)
        permisos = 'existe'
    libObj = libro.objects.get(id=idLibro)
    palabra = [val.id for val in libObj.PalabrasClave.all()]
    p = request.POST.getlist('palabras')
    palabras = []
    for i in p:
        palabras.append(elimina_tildes(i.lower()))
    palabras = list(set(palabras))
    if request.method == 'POST':

        if 'tituloC' in request.POST:
            xyz = request.POST['tituloC']
            libroAutor.capituloTitulo = request.POST['tituloC']
            libroAutor.save()
            print(libroAutor.capituloTitulo, libroAutor.id, libroAutor.user.id, xyz)
        form = DocumentForm(request.POST, request.FILES, instance=libros)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            form.save_m2m()
            for i in palabras:
                if not palabraClave.objects.filter(Termino__iexact=i):
                    us = User.objects.get(pk=usuario)
                    palabraNew = palabraClave.objects.create(Termino=i, user=us)
                    book.PalabrasClave.add(palabraNew)
                    del palabraNew
                else:
                    palabra = palabraClave.objects.get(Termino__iexact=i)
                    book.PalabrasClave.add(palabra)
            au = autoresLibro.objects.filter(libro=book).order_by('id')
            for i in range(len(au)):
                grado = f"grado{i}"
                user = f"user{i}"
                if grado in request.POST:
                    au[i].gradoAutoria = request.POST[grado]
                    au[i].user = User.objects.get(pk=int(request.POST[user]))
                    au[i].save()
            for i in range(len(au),20):
                grado = f"grado{i}"
                user = f"user{i}"
                if grado in request.POST:
                    a = request.POST[grado]
                    obj = User.objects.get(pk=int(request.POST[user]))
                    autor = autoresLibro.objects.create(gradoAutoria=a, libro=book, user=obj, capituloSel=False)
                    autor.save()
                    del autor

            book.save()
            messages.success(request, ('Se ha actualizado la información correctamente'))
            return redirect('Libro:libro_lis')
        else:
            messages.success(request, ('Ah ocurrido un error.'))
            return redirect('Libro:libro_lis')
    else:
        form = DocumentForm(instance=libros)
    if permisos == 'existe':
        return render(request, 'libro/UpdateLibro.html', {
            'form': form,
            'base': baseDatos.objects.all(),
            'Datos': baseDatos.objects.exclude(id__in=basesD),
            'palabra': palabraClave.objects.filter(id__in=palabra),
            'us': User.objects.all(),
            'Autores': autoresLibro.objects.filter(id__in=autores),
            'id': idLibro,
            'perfil': perfil,
            'grad': libroAutor
        })
    else:
        return redirect('Libro:libro_lis')

class LibroDelete(DeleteView):
    model = libro
    template_name = 'libro/DeleteLibro.html'
    success_url = reverse_lazy('Libro:libro_lis')
    def get_context_data(self, **kwargs):
        context = super(LibroDelete, self).get_context_data(**kwargs)
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
