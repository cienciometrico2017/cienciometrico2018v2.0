from django.conf.urls import url
from apps.Publicaciones.models import publicaciones
from apps.Publicaciones.views import CreatePublicaciones,ListPublicaciones,UpdatePublicaciones,DeletePublicaciones
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^CrearPublicaciones$', login_required(CreatePublicaciones), name="create_Publicaciones"),
    url(r'^ListarPublicaciones', login_required(ListPublicaciones.as_view(queryset=publicaciones.objects.all().order_by('id'))),name="lista_Publicaciones"),
    url(r'^UpdatePublicaciones/(?P<id_publicaciones>\d+)/$', login_required(UpdatePublicaciones),name="update_Publicaciones"),
    url(r'^DeletePublicaciones/(?P<pk>\d+)/$', login_required(DeletePublicaciones.as_view()),name="delete_Publicaciones"),

]