from django.conf.urls import url
from apps.pais.models import pais
from apps.baseDatos.views import listBD, createBD, existe, listDbUp
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^index',login_required(listBD), name='index'),
    url(r'^existe/',login_required(existe), name='existe'),
    url(r'^create/',login_required(createBD), name='createdb'),
    url(r'^selectDb/',login_required(listDbUp), name='selectdb'),
]