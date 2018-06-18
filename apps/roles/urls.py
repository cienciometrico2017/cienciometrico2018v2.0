from django.conf.urls import url,include
from apps.roles.views import RegistroRol
urlpatterns = [
    url(r'^nuevo$',RegistroRol.as_view(),name="crear_rol"),


]