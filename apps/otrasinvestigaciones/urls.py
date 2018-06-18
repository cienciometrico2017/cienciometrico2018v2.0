from django.conf.urls import url
from apps.otrasinvestigaciones.models import otrasinvestigaciones
from apps.otrasinvestigaciones.views import Otrainvestigacioncrear,OtrainvestigacionDelete,OtrainvestigacionEdit,OtrainvestigacionList
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^uploads/form/$', login_required(Otrainvestigacioncrear), name='otrasinvestigaciones_crear'),
    url(r'^listar', login_required(OtrainvestigacionList.as_view(queryset= otrasinvestigaciones.objects.all().order_by('id'))), name='otrasinvestigaciones_lis'),
    url(r'^editar/(?P<id_otrainvestigacion>\d+)/$',login_required(OtrainvestigacionEdit), name='otrasinvestigaciones_update'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(OtrainvestigacionDelete.as_view()), name='otrasinvestigaciones_eliminar'),
]
