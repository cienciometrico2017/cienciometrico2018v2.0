from django.conf.urls import url
from apps.Formacion_Complementaria.models import formacion_complementaria
from apps.Formacion_Complementaria.views import CreateFormacion_Complementaria,ListFormacion_Complementaria,UpdateFormacion_Complementaria,DeleteFormacion_Complementaria
from django.contrib.auth.decorators import login_required
urlpatterns = [

    url(r'^CrearFormacion_Complementaria$',login_required(CreateFormacion_Complementaria.as_view()), name="create_Formacion_Complementaria"),
   url(r'^ListarFormacion_Complementaria',login_required(ListFormacion_Complementaria.as_view(queryset=formacion_complementaria.objects.all().order_by('id'))), name="lista_Formacion_Complementaria"),
   url(r'^UpdateFormacion_Complementaria/(?P<pk>\d+)/$',login_required(UpdateFormacion_Complementaria.as_view()), name="update_Formacion_Complementaria"),
   url(r'^DeleteFormacion_Complementaria/(?P<pk>\d+)/$',login_required(DeleteFormacion_Complementaria.as_view()), name="delete_Formacion_Complementaria"),

]