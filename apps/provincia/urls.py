from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.provincia.models import provincia
from apps.provincia.views import ProvinciaCreate,ProvinciaList,ProvinciaDelete,ProvinciaUpdate
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^nuevo',login_required(ProvinciaCreate.as_view()), name='provincia_crear'),
    url(r'^listar',login_required(ProvinciaList.as_view(queryset= provincia.objects.all().order_by('id'))), name='provincia_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(ProvinciaUpdate.as_view()), name='provincia_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(ProvinciaDelete.as_view()), name='provincia_eliminar'),
]