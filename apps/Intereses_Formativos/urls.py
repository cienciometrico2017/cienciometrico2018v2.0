from django.conf.urls import url
from apps.Intereses_Formativos.models import intereses_formativos
from apps.Intereses_Formativos.views import InteresList,InteresCreate,InteresDelete,InteresUpdate
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^nuevo$',login_required(InteresCreate.as_view()), name="create_interes"),
    url(r'^index',login_required(InteresList.as_view(queryset=intereses_formativos.objects.all().order_by('id'))), name="interes_listar"),
    url(r'^Actualizar/(?P<pk>\d+)/$',login_required(InteresUpdate.as_view()), name="update_interes"),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(InteresDelete.as_view()), name="delete_interes"),
]