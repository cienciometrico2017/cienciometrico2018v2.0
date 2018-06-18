from django.conf.urls import url
from apps.carrera.models import carrera
from apps.carrera.views import CreateCarrera,ListCarrera,UpdateCarrera,DeleteCarrera,Carreracrear,Carreradedit
from django.contrib.auth.decorators import login_required
urlpatterns = [

    url(r'^CrearCarrera$',login_required(Carreracrear), name="create_Carrera"),
   url(r'^ListarCarrera',login_required(ListCarrera.as_view(queryset=carrera.objects.all().order_by('id'))), name="lista_Carrera"),
   url(r'^UpdateCarrera/(?P<id_carrera>\d+)/$',login_required(Carreradedit), name="update_Carrera"),
   url(r'^DeleteCarrera/(?P<pk>\d+)/$',login_required(DeleteCarrera.as_view()), name="delete_Carrera"),

]