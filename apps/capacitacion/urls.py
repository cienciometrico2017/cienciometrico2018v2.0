from django.conf.urls import url
from apps.capacitacion.models import capacitacion
from apps.capacitacion.views import CapacitacionList,CapacitacionCreate,CapacitacionUpdate,CapacitacionDelete
from django.contrib.auth.decorators import login_required
urlpatterns = [

   url(r'^nuevo',login_required(CapacitacionCreate.as_view()), name="capacitacionCrear"),
   url(r'^index',login_required(CapacitacionList.as_view(queryset=capacitacion.objects.all().order_by('id'))), name="capacitacion_listar"),
   url(r'^Actualizar/(?P<pk>\d+)/$',login_required(CapacitacionUpdate.as_view()), name="capacitacionActualizar"),
   url(r'^eliminar/(?P<pk>\d+)/$',login_required(CapacitacionDelete.as_view()), name="capacitacionEliminar"),

]