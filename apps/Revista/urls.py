from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.Revista.models import revista
from apps.Revista.views import listRev,RevistaList,RevistaDelete,RevistaEdit, revCreate, listRevUp, listSelectedItems
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^new/$', login_required(revCreate), name='create_Revista'),
    url(r'^select/$', login_required(listRev), name='select'),
    url(r'^sel/$', login_required(listSelectedItems), name='select'),
    url(r'^selectUp/$', login_required(listRevUp), name='selectUp'),
    url(r'^list', login_required(RevistaList.as_view(queryset= revista.objects.all().order_by('id'))), name='lista_Revista'),
    url(r'^edit/(?P<id_revista>\d+)/$', login_required(RevistaEdit), name='update_Revista'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(RevistaDelete.as_view()), name='delete_Revista'),
    
]