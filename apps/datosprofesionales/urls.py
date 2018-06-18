from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.datosprofesionales.models import datos_profecionales
from apps.datosprofesionales.views import DatosProfeList, DatosProfeCreate, DatosProfeUpdate, DatosProfeDelete
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^nuevo',login_required(DatosProfeCreate.as_view()), name='datosprofe_crear'),
    url(r'^listar',login_required(DatosProfeList.as_view(queryset= datos_profecionales.objects.all().order_by('id'))), name='datosprofe_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(DatosProfeUpdate.as_view()), name='datosprofe_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(DatosProfeDelete.as_view()), name='datosprofe_eliminar'),
]