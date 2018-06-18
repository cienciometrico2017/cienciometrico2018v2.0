from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.investigaciones.models import investigacion
from apps.investigaciones.views import InvestigacionList,Investigacioncrear,InvestigacionEdit,InvestigacionDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^nuevo/$', login_required(Investigacioncrear), name='investigaciones_crear'),
    url(r'^listar', login_required(InvestigacionList.as_view(queryset= investigacion.objects.all().order_by('id'))), name='investigaciones_lis'),
    url(r'^editar/(?P<id_investigacion>\d+)/$',login_required(InvestigacionEdit), name='investigaciones_update'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(InvestigacionDelete.as_view()), name='investigaciones_eliminar'),
]
