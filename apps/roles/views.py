from django.shortcuts import render
from django.views.generic import CreateView
from apps.roles.models import Rol
from apps.roles.form import Registrorol
from django.core.urlresolvers import reverse_lazy
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
# Create your views here.
class RegistroRol(CreateView):
    model = Rol
    template_name = "roles/rol_crear.html"
    form_class = Registrorol
    success_url = reverse_lazy('roles:crear_rol')

    def get_context_data(self, **kwargs):
        persona = Investigador.objects.all()  # Esto si retorna un QuerySet
        exi = persona.exists()

        context = super(RegistroRol, self).get_context_data(**kwargs)
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
