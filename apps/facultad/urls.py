from django.conf.urls import url
from apps.facultad.models import facultad
from apps.facultad.views import CreateFacultad,ListFacultad,UpdateFacultad,DeleteFacultad,Facultadcrear,Facultadedit
from django.contrib.auth.decorators import login_required
urlpatterns = [

    url(r'^CrearFacultad$',login_required(Facultadcrear), name="create_Facultad"),
   url(r'^ListarFacultad',login_required(ListFacultad.as_view(queryset=facultad.objects.all().order_by('id'))), name="lista_Facultad"),
   url(r'^UpdateFacultad/(?P<id_facultad>\d+)/$',login_required(Facultadedit), name="update_Facultad"),
   url(r'^DeleteFacultad/(?P<pk>\d+)/$',login_required(DeleteFacultad.as_view()), name="delete_Facultad"),

]