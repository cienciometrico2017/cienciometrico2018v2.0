from django.shortcuts import render
from apps.Linea_Investigacion.models import linea_investigacion
from apps.Sub_Lin_Investigacion.models import sub_lin_investigacion
from django.http import HttpResponse
import json

# Create your views here.
def listSelectedItems(request):
    if request.method == 'POST':
        data = request.POST.get('datos')
        if data:
            line = linea_investigacion.objects.get(id = data)
            sub = sub_lin_investigacion.objects.filter(linea_investigacion = line)
            results = []
            doctor_json = {}
            doctor_json['text'] = '----------'
            doctor_json['value'] = ''
            results.append(doctor_json)
            for i in sub:
                doctor_json = {}
                doctor_json['text'] = i.Nombre
                doctor_json['value'] = i.id
                results.append(doctor_json)
            data_json = json.dumps(results)
        else:
            results = []
            doctor_json = {}
            doctor_json['text'] = '----------'
            doctor_json['value'] = ''
            results.append(doctor_json)
            data_json = json.dumps(results)
    else:
        data_json='fail'
    mimetype="application/json"
    return HttpResponse(data_json,mimetype)
