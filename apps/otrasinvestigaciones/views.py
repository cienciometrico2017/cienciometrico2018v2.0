from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.otrasinvestigaciones.models import otrasinvestigaciones
from django.views.generic import ListView,DeleteView
from apps.otrasinvestigaciones.form import DocumentForm
from apps.roles.models import Rol
from apps.Investigador.models import Investigador
# Create your views here.
def Otrainvestigacioncrear(request):
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
            return redirect('otrainvestigacion:otrasinvestigaciones_lis')
    else:
        form = DocumentForm()
    return render(request, 'otrasinvestigaciones/otrasinvestigaciones_crear.html', {
        'form': form, 'usuario': privilegio
    })
class OtrainvestigacionList(ListView):
    model = otrasinvestigaciones
    template_name = 'otrasinvestigaciones/otrasinvestigaciones_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(OtrainvestigacionList, self).get_context_data(**kwargs)
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
def OtrainvestigacionEdit(request, id_otrainvestigacion):
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
    oinves = otrasinvestigaciones.objects.get(id=id_otrainvestigacion)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=oinves)
        if form.is_valid():
            form.save()
            return redirect('otrainvestigacion:otrasinvestigaciones_lis')
    else:
        form = DocumentForm(instance=oinves)
    return render(request, 'otrasinvestigaciones/otrasinvestigaciones_update.html', {'form': form,'usuario': privilegio})
class OtrainvestigacionDelete(DeleteView):
    model = otrasinvestigaciones
    template_name = 'otrasinvestigaciones/otrasinvestigaciones_delete.html'
    success_url = reverse_lazy('otrainvestigacion:otrasinvestigaciones_lis')
    def get_context_data(self, **kwargs):
        context = super(OtrainvestigacionDelete, self).get_context_data(**kwargs)
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

