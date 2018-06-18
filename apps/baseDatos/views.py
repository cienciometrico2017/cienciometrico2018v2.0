from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from apps.Articulos_Cientificos.models import articulos_cientificos
from apps.baseDatos import form
from apps.baseDatos.models import baseDatos
import json

def listBD(request):
    if request.is_ajax:
        #search=request.POST.get('start','')

        bd=baseDatos.objects.all()
        results=[]
        for i in bd:
            doctor_json={}
            doctor_json['text']=i.BaseDatos
            doctor_json['value']=i.id
            results.append(doctor_json)
        data_json=json.dumps(results)
    else:
        data_json='fail'
    mimetype="application/json"
    return HttpResponse(data_json,mimetype)

def existe(x):
    base = baseDatos.objects.get(BaseDatos = x)
    if base:
        return True
    else:
        return False


def listDbUp(request):
    if request.method == 'POST':
        # search=request.POST.get('start','')
        ArticuloID = request.POST.get('ArticuloID')
        articulo = articulos_cientificos.objects.get(id=ArticuloID)

        basesD = [val.id for val in articulo.baseDatos.all()]

        dbSel = [val for val in articulo.baseDatos.all()]

        bd = baseDatos.objects.all()

        dbNoSel = baseDatos.objects.exclude(id__in=basesD)

        results = []
        for i in dbSel:
            doctor_json = {}
            doctor_json['text'] = i.BaseDatos
            doctor_json['value'] = i.id
            doctor_json['selected'] = 'selected'
            results.append(doctor_json)

        for i in dbNoSel:
            doctor_json = {}
            doctor_json['text'] = i.BaseDatos
            doctor_json['value'] = i.id
            doctor_json['selected'] = ''
            results.append(doctor_json)

        data_json = json.dumps(results)

    else:
        data_json = 'fail'
    mimetype = "application/json"
    return HttpResponse(data_json, mimetype)

def createBD(request):
    results = []
    dbjson = {}
    BaseDatos = request.POST.get('BaseDatos')
    print('Mi base de datos', BaseDatos)
    if not baseDatos.objects.filter(BaseDatos__iexact = BaseDatos):
        if request.method == 'POST':
            Url = request.POST.get('Url')
            us = request.POST.get('user')
            USER = User.objects.get(id=int(us))
            newDB = baseDatos.objects.create(
                BaseDatos=BaseDatos,
                Url=Url,
                user= USER
            )
            dbjson['text'] = newDB.BaseDatos
            dbjson['value'] = newDB.id
            results.append(dbjson)
            data_json = json.dumps(results)
            mimetype = "application/json"
            return HttpResponse(data_json, mimetype)
        else:
            response = HttpResponse('Your message here', status=401)
            response['Content-Length'] = len(response.content)
            return response
    else:
        response = HttpResponse('Your message here', status=401)
        response['Content-Length'] = len(response.content)
        return response




