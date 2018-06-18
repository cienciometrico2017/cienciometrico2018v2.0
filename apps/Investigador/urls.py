from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.Investigador.models import User
from apps.Investigador.views import RegistroUsuario,ActualizarUsuario,ActualizarPassword, new, autor
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registrar$', RegistroUsuario.as_view(), name="registrar"),
    url(r'^registrarAut/', login_required(autor), name="registrarAut"),
    url(r'^editar/(?P<pk>\d+)/$', ActualizarUsuario.as_view(), name="editar"),
    url(r'^editarPass/(?P<pk>\d+)/$', ActualizarPassword.as_view(), name="editarPass"),
    url(r'^new$', new, name="new"),

]
