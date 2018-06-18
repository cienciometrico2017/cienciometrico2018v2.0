from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.pais.models import pais
from apps.pais.views import PaisCreate, PaisList, PaisUpdate, PaisDelete,listSelectedItems, listPais
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^nuevo',login_required(PaisCreate.as_view()), name='pais_crear'),
    url(r'^sel/$',login_required(listSelectedItems), name='sel'),
    url(r'^selU/$',login_required(listPais), name='selU'),
    url(r'^listar',login_required(PaisList.as_view(queryset= pais.objects.all().order_by('id'))), name='pais_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(PaisUpdate.as_view()), name='pais_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(PaisDelete.as_view()), name='pais_eliminar'),

]