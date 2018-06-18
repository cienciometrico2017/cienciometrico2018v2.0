from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.Proyectos.models import proyecto
from apps.Proyectos.views import Proyectocrear,ProyectoDelete,ProyectoEdit,ProyectoList
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^uploads/form/$', login_required(Proyectocrear), name='proyectos_crear'),
    url(r'^listar', login_required(ProyectoList.as_view(queryset= proyecto.objects.all().order_by('id'))), name='proyectos_lis'),
    url(r'^editar/(?P<id_proyecto>\d+)/$',login_required(ProyectoEdit), name='proyectos_update'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(ProyectoDelete.as_view()), name='proyectos_eliminar'),
]
