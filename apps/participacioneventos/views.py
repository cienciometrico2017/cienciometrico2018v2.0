from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.participacioneventos.models import participacionevento
from django.views.generic import ListView,DeleteView
from apps.participacioneventos.form import DocuForm
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
# Create your views here.
def participacioneventoscrear(request):
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
        form = DocuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('partevento:partevento_lis')
    else:
        form = DocuForm()
    return render(request, 'participacioneventos/participacioneventos_crear.html', {
        'form': form, 'usuario': privilegio
    })
class participacioneventosList(ListView):
    model = participacionevento
    template_name = 'participacioneventos/participacioneventos_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(participacioneventosList, self).get_context_data(**kwargs)
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
def participacioneventosEdit(request, id_participacioneventos):
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
    pevento = participacionevento.objects.get(id=id_participacioneventos)
    if request.method == 'POST':
        form = DocuForm(request.POST, request.FILES,instance=pevento)
        if form.is_valid():
            form.save()
            return redirect('partevento:partevento_lis')
    else:
        form = DocuForm(instance=pevento)
    return render(request, 'participacioneventos/participacioneventos_update.html', {'form': form, 'usuario': privilegio})
class participacioneventosDelete(DeleteView):
    model = participacionevento
    template_name = 'participacioneventos/participacioneventos_delete.html'
    success_url = reverse_lazy('partevento:partevento_lis')
    def get_context_data(self, **kwargs):
        context = super(participacioneventosDelete, self).get_context_data(**kwargs)
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

