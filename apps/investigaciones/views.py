from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.investigaciones.form import DocumentForm
from apps.investigaciones.models import investigacion
from django.views.generic import ListView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
# Create your views here.
def Investigacioncrear(request):
    usuario = request.user.id
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
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('investigacion:investigaciones_lis')
    else:
        form = DocumentForm()
    return render(request, 'investigaciones/investigaciones_crear.html', {
        'form': form, 'usuario': privilegio
    })
class InvestigacionList(ListView):
    model = investigacion
    template_name = 'investigaciones/investigaciones_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(InvestigacionList, self).get_context_data(**kwargs)
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
def InvestigacionEdit(request, id_investigacion):
    usuario = request.user.id
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
    inves = investigacion.objects.get(id=id_investigacion)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=inves)
        if form.is_valid():
            form.save()
            return redirect('investigacion:investigaciones_lis')
    else:
        form = DocumentForm(instance=inves)
    return render(request, 'investigaciones/investigaciones_update.html', {'form': form, 'usuario':privilegio})

class InvestigacionDelete(DeleteView):
    model = investigacion
    template_name = 'investigaciones/investigaciones_delete.html'
    success_url = reverse_lazy('investigacion:investigaciones_lis')
    def get_context_data(self, **kwargs):
        context = super(InvestigacionDelete, self).get_context_data(**kwargs)
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

