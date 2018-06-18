from django.conf.urls import url
from apps.HomePrincipal.views import inde,producc,similar
from django.contrib.auth.decorators import login_required
from .views import BusquedaView, BusquedaAjaxView,BusquedaFacuView, BusquedaCampusView,BusquedaCarreraView,BusquedaFiltroView, ReportePersonasPDF
urlpatterns = [
    url(r'^$',inde, name="HomePrincipal"),
    url(r'^cientifica$',producc, name="produccion"),
    url(r'^similares$',similar, name="similar"),
    url(r'^Home/graficas$', BusquedaView.as_view(), name="grafic"),
    url(r'^Home/busqueda_ajax/$',BusquedaAjaxView.as_view()),
    url(r'^Home/busqueda_campus/$',BusquedaCampusView.as_view()),
    url(r'^Home/busqueda_facultad/$',BusquedaFacuView.as_view()),
    url(r'^Home/busqueda_carrera/$',BusquedaCarreraView.as_view()),
    url(r'^Home/busqueda_filtros/$',BusquedaFiltroView.as_view()),
    url(r'^Home/reporte_personas_pdf/$',ReportePersonasPDF.as_view(), name="reporte_personas_pdf"),

   ]
