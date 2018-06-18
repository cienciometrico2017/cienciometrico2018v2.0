from django.conf.urls import url
from apps.palabraClave.views import view
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^json$', login_required(view), name="json"),

]
