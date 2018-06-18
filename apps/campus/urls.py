from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.campus.models import campus
from apps.campus.views import CampusCreate, CampusList,Campus_edit, CampusDelete
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^nuevo',login_required(CampusCreate), name='campus_crear'),
    url(r'^listar',login_required(CampusList.as_view(queryset= campus.objects.all().order_by('id'))), name='campus_listar'),
    url(r'^update/(?P<id_campus>\d+)/$',login_required(Campus_edit), name='campus_update'),
    url(r'^delete/(?P<pk>\d+)/$',login_required(CampusDelete.as_view()), name='campus_delete'),
]