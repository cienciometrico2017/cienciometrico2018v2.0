from django.conf.urls import url
from apps.Evento.models import evento
from apps.Evento.views import CreateEvento,ListEvento,UpdateEvento,DeleteEvento
from django.contrib.auth.decorators import login_required
urlpatterns = [

    url(r'^CrearEvento$',login_required(CreateEvento.as_view()), name="create_Evento"),
   url(r'^ListarEvento',login_required(ListEvento.as_view(queryset=evento.objects.all().order_by('id'))), name="lista_Evento"),
   url(r'^UpdateEvento/(?P<pk>\d+)/$',login_required(UpdateEvento.as_view()), name="update_Evento"),
   url(r'^DeleteEvento/(?P<pk>\d+)/$',login_required(DeleteEvento.as_view()), name="delete_Evento"),

]