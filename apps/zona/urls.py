from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.zona.models import zona
from apps.zona.views import ZonaCreate,ZonaList,ZonaDelete,ZonaUpdate
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^nuevo',login_required(ZonaCreate.as_view()), name='zona_crear'),
    url(r'^listar',login_required(ZonaList.as_view(queryset= zona.objects.all().order_by('id'))), name='zona_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(ZonaUpdate.as_view()), name='zona_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(ZonaDelete.as_view()), name='zona_eliminar'),
]