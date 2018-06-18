from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy

from apps.Articulos_Cientificos.models import articulos_cientificos
from apps.Revista.form import DocumentForm
from apps.Revista.models import revista
from apps.baseDatos.models import baseDatos
from django.views.generic import ListView,DeleteView
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
from django.http import JsonResponse
from django.http import HttpResponse
import json
from collections import Counter
# Create your views here.

def revCreate(request):
    Nombre = request.POST.get('Nombre')
    print('Mi base de datos', Nombre)

    if not revista.objects.filter(Nombre__iexact=Nombre):
        if request.method == 'POST':
            ISSN = request.POST.get('ISSN')
            base = request.POST.getlist('baseData[]')
            dataBase = []
            print(base)
            for i in base:
                dataBase.append(baseDatos.objects.get(id=i))
            for i in dataBase:
                print(i.BaseDatos)
            Cuartil_Pertenece  = request.POST.get('Cuartil_Pertenece')
            Factor_Impacto  = request.POST.get('Factor_Impacto')
            Url  = request.POST.get('Url')
            us = request.POST.get('user')
            validada = request.POST.get('validada')

            USER = User.objects.get(id=int(us))
            rev = revista.objects.create(
                Nombre=Nombre,
                ISSN=ISSN,
                Cuartil_Pertenece = Cuartil_Pertenece,
                Factor_Impacto = Factor_Impacto,
                Url = Url,
                validar = validada,
            )
            rev.user = USER
            rev.save()
            for i in dataBase:
                rev.base.add(i)
            rev.save
            results = []
            revjson = {}
            revjson['text'] = rev.Nombre
            print(rev.Nombre)
            revjson['value'] = rev.id
            print(rev.id)
            results.append(revjson)
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


def listSelectedItems(request):
    if request.method == 'POST':
        data = request.POST.getlist('datos[]')
        bd = revista.objects.all()
        l = []
        for i in bd:
            for j in i.base.all():
                #print('revista: ', i , ' Base de datos anexada: ',j.id, j.BaseDatos)
                for k in data:
                    #print('bases Sel ',k)
                    #print('b REV ',j.id)
                    if int(k) == int(j.id):
                        #print(i, i.id)
                        l.append(i.id)
        revistas = list(set(l))
        r = revista.objects.filter(id__in = revistas)
        results=[]
        doctor_json = {}
        doctor_json['text'] = '----------'
        doctor_json['value'] = ''
        results.append(doctor_json)
        for i in r:
            doctor_json={}
            doctor_json['text']=i.Nombre
            doctor_json['value']=i.id
            results.append(doctor_json)
        data_json=json.dumps(results)
    else:
        data_json='fail'
    mimetype="application/json"
    return HttpResponse(data_json,mimetype)

############################################
def listRev(request):
    if request.is_ajax:
        bd=revista.objects.all()
        results=[]
        for i in bd:
            doctor_json={}
            doctor_json['text']=i.Nombre
            doctor_json['value']=i.id
            results.append(doctor_json)
        data_json=json.dumps(results)
    else:
        data_json='fail'
    mimetype="application/json"
    return HttpResponse(data_json,mimetype)


def listRevUp(request):
    if request.method == 'POST':
        # search=request.POST.get('start','')
        ArticuloID = request.POST.get('ArticuloID')
        articulo = articulos_cientificos.objects.get(id=ArticuloID)
        revD = [val.id for val in articulo.revista.all()]

        revSel = [val for val in articulo.revista.all()]

        rev = revista.objects.all()

        revNoSel = revista.objects.exclude(id__in=revD)

        results = []
        for i in revSel:
            doctor_json = {}
            doctor_json['text'] = i.Nombre
            doctor_json['value'] = i.id
            doctor_json['selected'] = 'selected'
            results.append(doctor_json)

        for i in revNoSel:
            doctor_json = {}
            doctor_json['text'] = i.Nombre
            doctor_json['value'] = i.id
            doctor_json['selected'] = ''
            results.append(doctor_json)

        data_json = json.dumps(results)

    else:
        data_json = 'fail'
    mimetype = "application/json"
    return HttpResponse(data_json, mimetype)

def Revistacrear(request):
    usuario = request.user.id
    perfil = Investigador.objects.get(user_id=usuario)
    roles = perfil.roles.all()
    privi = []
    privilegios = []
    privilegio = []
    for r in roles:
        privi.append(r.id)
    for p in privi:
        roles5 = Rol.objects.get(pk=p)
        priv = roles5.privilegios.all()
        for pr in priv:
            privilegios.append(pr.codename)
    for i in privilegios:
        if i not in privilegio:
            privilegio.append(i)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Revista:lista_Revista')
    else:
        form = DocumentForm()
    return render(request, 'revista/CreateRevista.html', {
        'form': form, 'usuario': privilegio
    })

class RevistaList(ListView):
    model = revista
    template_name = 'revista/ListRevista.html'
    def get_context_data(self, **kwargs):
        context = super(RevistaList, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        try:
            capa = revista.objects.filter(user_id=usuario)
        except revista.DoesNotExist:
            capa = None
        context['Pon'] = capa
        context['perfil'] = Investigador.objects.get(user_id=self.request.user.id)
        return context
    

def RevistaEdit(request, id_revista):
    usuario = request.user.id
    articulo = revista.objects.get(id=id_revista)
    basesD = [val.id for val in articulo.base.all()]
    proy = revista.objects.get(id=id_revista)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=proy)
        if form.is_valid():
            form.save()
            return redirect('Revista:lista_Revista')
    else:
        form = DocumentForm(instance=proy)
    return render(request, 'revista/UpdateRevista.html', {
        'perfil': Investigador.objects.get(user_id=request.user.id),
        'form': form,
        'Datos': baseDatos.objects.exclude(id__in=basesD),
        'base': baseDatos.objects.all()
    })

class RevistaDelete(DeleteView):
    model = revista
    template_name = 'revista/DeleteRevista.html'
    success_url = reverse_lazy('Revista:lista_Revista')
    def get_context_data(self, **kwargs):
        context = super(RevistaDelete, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Investigador.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context