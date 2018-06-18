"""Cienciometrico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login,password_reset,password_reset_done,password_reset_confirm,password_reset_complete
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.HomePrincipal.urls', namespace="indexHome")),
    url(r'^pais/', include('apps.pais.urls', namespace="pais")),
    url(r'^zona/', include('apps.zona.urls', namespace="zona")),
    url(r'^provincia/', include('apps.provincia.urls', namespace="provincia")),
    url(r'^ciudad/', include('apps.ciudad.urls', namespace="ciudad")),
    #url(r'^universidad/', include('apps.universidad.urls', namespace="universidad")),
    url(r'^Carrera/', include('apps.carrera.urls', namespace="carrera")),
    url(r'^Facultad/', include('apps.facultad.urls', namespace="Facultad")),
    url(r'^campus/', include('apps.campus.urls', namespace="campus")),
    url(r'^investigador/', include('apps.Investigador.urls', namespace="usuario")),
    url(r'^articulo/', include('apps.Articulos_Cientificos.urls', namespace="articulosCientificos")),
    url(r'^investigacion/', include('apps.investigaciones.urls', namespace="investigacion")),
    url(r'^datosprofesionales/', include('apps.datosprofesionales.urls', namespace="datosprofe")),
    url(r'^formacionAcad/', include('apps.Formacion_Academica.urls', namespace="FormacionAcademica")),
    url(r'^formacionComple/', include('apps.Formacion_Complementaria.urls', namespace="FormacionComplementaria")),
    url(r'^Evento/', include('apps.Evento.urls', namespace="evento")),
    url(r'^otrainvestigacion/', include('apps.otrasinvestigaciones.urls', namespace="otrainvestigacion")),
    url(r'^participacioneventos/linea', include('apps.participacioneventos.urls', namespace="partevento")),
    url(r'^proyectos/', include('apps.Proyectos.urls', namespace="proyecto")),
    url(r'^roles/', include('apps.roles.urls', namespace="roles")),
    url(r'^index/', include('apps.inicio.urls', namespace="inicio")),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^accounts/login/', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^libro/', include('apps.Libro.urls', namespace="Libro")),
    url(r'^revista/', include('apps.Revista.urls', namespace="Revista")),
    url(r'^Publicaciones/', include('apps.Publicaciones.urls', namespace="publicaciones")),
    url(r'^ponencia/', include('apps.Ponencia.urls', namespace="Ponencia")),
    url(r'^capacitacion/', include('apps.capacitacion.urls', namespace="capacitacion")),
    url(r'^intereses/', include('apps.Intereses_Formativos.urls', namespace="interes")),
    url(r'^palabras/', include('apps.palabraClave.urls', namespace="pal")),
    url(r'^db/', include('apps.baseDatos.urls', namespace="base")),
    url(r'^autor/', include('apps.autoresArticulos.urls', namespace="autor")),
    url(r'^linea/', include('apps.Linea_Investigacion.urls', namespace="linea")),
    #///////////////////////PASSWORD RESET///////////////////////////////////////
    url(r'^password_reset/', password_reset,
       {'template_name': 'registration/password_reset_form.html',
   'email_template_name': 'registration/password_reset_email.html'},
     name='password_reset'),
    url(r'^password_reset_done/', password_reset_done,
       {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_listo'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_completado'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
