from django.conf.urls import url
from apps.participacioneventos.models import participacionevento
from apps.participacioneventos.views import participacioneventoscrear,participacioneventosDelete,participacioneventosEdit,participacioneventosList
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^uploads/form/$', login_required(participacioneventoscrear), name='partevento_crear'),
    url(r'^listar', login_required(participacioneventosList.as_view(queryset= participacionevento.objects.all().order_by('id'))), name='partevento_lis'),
    url(r'^editar/(?P<id_participacioneventos>\d+)/$',login_required(participacioneventosEdit), name='partevento_update'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(participacioneventosDelete.as_view()), name='partevento_eliminar'),
]
