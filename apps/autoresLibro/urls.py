from django.conf.urls import url
from apps.pais.models import pais
from apps.autoresArticulos.views import eliminar,eliminarBook,eliminarProj
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^del/(?P<idArt>\d+)_(?P<id>\d+)/$',login_required(eliminar), name='eliminar'),
    url(r'^delB/(?P<idArt>\d+)_(?P<id>\d+)/$',login_required(eliminarBook), name='eliminarBook'),
    url(r'^delP/(?P<idArt>\d+)_(?P<id>\d+)/$',login_required(eliminarProj), name='eliminarProj'),
]