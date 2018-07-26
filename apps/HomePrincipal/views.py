from django.shortcuts import render
from apps.Investigador.models import Investigador



from apps.roles.models import Rol
# nuevo


from apps.zona.models import zona
from apps.universidad.models import universidad
from apps.facultad.models import facultad
from apps.carrera.models import carrera
from apps.campus.models import campus
from django.views.generic import ListView,TemplateView

from apps.Articulos_Cientificos.models import articulos_cientificos
from apps.autoresArticulos.models import autoresArticulos
from django.contrib.auth.models import User
from apps.Investigador.models import Investigador
from apps.informacionLaboral.models import informacionLaboral
from django.db import connection
from django.core import serializers
from django.http import HttpResponse
#para los reportes
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View

from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.lib.pagesizes import A4,cm





#nuevo
import json
import os
import collections
#DSN = "dbname=Cienciometrico2 user=postgres password=1945"
#nuevo

var="0"

# Create your views here.
def inde(request):
    return render(request, 'Home/inicio.html')

def producc(request):
    return render(request, 'Home/produccioncientifica.html')

def similar(request):
    perfil = Investigador.objects.all()
    privi = []
    for p in perfil:
        if p.roles == '3':
            privi.append(p)

    return render(request, 'Home/similares.html',{'usuario': perfil})



class BusquedaView(ListView):
    model = zona
    template_name = "Home/Graficas.html"
    context_object_name = 'zona'







class BusquedaAjaxView(TemplateView):


    def get(self,request,*args, **kwargs):
        id_zona=request.GET['id']

        #print (id_zona)





        univer=universidad.objects.filter(zona__id=id_zona)
        #print(univer)
        data= serializers.serialize('json',univer,
                            fields=('id','Nombre'))
        #print(data)
        return HttpResponse(data, content_type='application/json')



class BusquedaCampusView(TemplateView):
    def get(self,request,*args, **kwargs):
        id_uni=request.GET['id']
        #print (id_uni)

        facul=campus.objects.filter(universidad__id=id_uni)
        #print(facul)
        data= serializers.serialize('json',facul,
                            fields=('id','Nombre'))
        return HttpResponse(data, content_type='application/json')






class BusquedaFacuView(TemplateView):
    def get(self,request,*args, **kwargs):
        id_campus=request.GET['id']
        #print (id_campus)

        facul=facultad.objects.filter(campus__id=id_campus)
        #print(facul)
        data= serializers.serialize('json',facul,
                            fields=('id','Nombre'))
        return HttpResponse(data, content_type='application/json')

class BusquedaCarreraView(TemplateView):
    def get(self,request,*args, **kwargs):
        id_facul=request.GET['id']
        #print (id_facul)

        carrer=carrera.objects.filter(facultad__id=id_facul)

        #print(carrer)
        data= serializers.serialize('json',carrer,
                            fields=('id','Nombre'))
        #print(data)
        return HttpResponse(data, content_type='application/json')

class BusquedaFiltroView(TemplateView):
    def get(self,request,*args, **kwargs):
        zon=request.GET['z']
        uni=request.GET['u']
        camp=request.GET['cam']
        facu=request.GET['f']
        carr=request.GET['c']
        fy=request.GET['fy']
        #print (zon)
        #print (uni)
        #print (camp)
        #print (facu)
        #print (carr)
        #print (fy)

        if int(zon)>0 and int(uni)>0 and int(camp)>0 and int(facu)>0 and int(carr)>0 and int(fy) ==2:
            json=ProcesaGraficaCarrera(carr)
            s=[['utc',5],['uta',9]]
            return HttpResponse(json, content_type='application/json')
        if int(zon)>0 and int(uni)>0 and int(camp)>0 and int(facu)>0 and int(carr)==0 and int(fy) ==2:
            json=ProcesaGraficaCarrerasTodo(facu)
            return HttpResponse(json, content_type='application/json')
        if int(zon)>0 and int(uni)>0 and int(camp)>0 and int(facu)==0 and int(carr)==0 and int(fy) ==2:
            json=ProcesaGraficaFacultadesTodo(camp)
            return HttpResponse(json, content_type='application/json')
        if int(zon)>0 and int(uni)>0 and int(camp)==0 and int(facu)==0 and int(carr)==0 and int(fy) ==2:
            json=ProcesaGraficaCampusTodo(uni)
            return HttpResponse(json, content_type='application/json')
        if int(zon)>0 and int(uni)==0 and int(camp)==0 and int(facu)==0 and int(carr)==0 and int(fy) ==2:
            json=ProcesaGraficaUniversidadTodo(zon)
            return HttpResponse(json, content_type='application/json')
        if int(zon)==0 and int(uni)==0 and int(camp)==0 and int(facu)==0 and int(carr)==0 and int(fy) ==2:
            json=ProcesaGraficaZonaTodo()
            return HttpResponse(json, content_type='application/json')

# area de funciones
def ProcesaGraficaCarrera(c):
    carr=consultar_articulos_carrera(c)
    num=0;
    vector_articulos=[]
    nombre_carrera="."
    for c in carr:
        doc=" "
        vec_temp=[]
        vec_temp.append(c.titulo)
        vec_temp.append(c.url)
        vec_temp.append(c.iSSN)
        vec_temp.append(c.volumen)
        doc=str(c.documento)
        vec_temp.append(doc)
        #print(doc)
        vec_temp.append(c.first_name)
        vec_temp.append(c.revista.Nombre)
        vector_articulos.append(vec_temp)
        nombre_carrera=c.Nombre
    num=Cuenta_registros(carr)
    #print("el vector articulo es")
    #print(vector_articulos)
    vector_carrera=[]
    vector_carrera.append(nombre_carrera)
    vector_carrera.append(num)
    vector_carrera.append(vector_articulos)
    #vector_carrera.append(vector_articulos)

    vector_final=[]
    vector_final.append(vector_carrera)
    json=serializaVector(vector_final)
    #print (json)
    return json



def ProcesaGraficaCarrerasTodo(facu):
        carrer=carrera.objects.filter(facultad__id=facu)
        nombres_carrera=[] #para los nombres de las carreras
        ids_carrera=[]     #para las ids de las carreras
        vector_contador=[] # para los vectores contadores de las carreras
        vector_final=[]    # para guardar el vector con la carrera y su repeticion
        vector_articulos=[]
        #guardamos en los vectores todos los nombres y ids de las carreras
        for row in carrer:
            nombres_carrera.append(row.Nombre)
            ids_carrera.append(row.id)
        #hafemos la consulta a la bd de cada carrera segun una id del vector de ids carrera
        cont=0

        vector_articulos_final=[]
        for contAR in ids_carrera:
            vector_articulos=[]
            #contamos el numero de articulos que hay en cada carrera y guardamos en vector_contador
            ar=consultar_articulos_carrera(str(ids_carrera[cont]))
            vector_contador.append(Cuenta_registros(ar))
            for c in ar:
                doc=" "
                vec_temp=[]
                #print(c.titulo)
                vec_temp.append(c.titulo)
                vec_temp.append(c.url)
                vec_temp.append(c.iSSN)
                vec_temp.append(c.volumen)
                doc=str(c.documento)
                vec_temp.append(doc)
                #print(doc)
                vec_temp.append(c.first_name)
                vec_temp.append(c.revista.Nombre)
                vector_articulos.append(vec_temp)
                nombre_carrera=c.Nombre
            vector_articulos_final.append(vector_articulos)
            cont=cont+1
            cont1=0
        for llena in vector_contador:
            vec_temp=[]
            vec_temp.append(nombres_carrera[cont1])
            vec_temp.append(vector_contador[cont1])
            vec_temp.append(vector_articulos_final[cont1])
            vector_final.append(vec_temp)
            cont1=cont1+1
        json=serializaVector(vector_final)
        return json
        #guardamos los articulos encontrados en esta carrera
def ProcesaGraficaFacultadesTodo(camp):

        facul=facultad.objects.filter(campus__id=camp)
        nombres_facultad=[] #para los nombres de las carreras
        ids_facultad=[]     #para las ids de las carreras
        vector_contador=[] # para los vectores contadores de las carreras
        vector_final=[]    # para guardar el vector con la carrera y su repeticion
        vector_articulos=[]
        #guardamos en los vectores todos los nombres y ids de las carreras
        for row in facul:
            nombres_facultad.append(row.Nombre)
            ids_facultad.append(row.id)
        #hafemos la consulta a la bd de cada carrera segun una id del vector de ids carrera
        vector_articulos_final=[]
        cont=0
        for contAR in ids_facultad:
            vector_articulos=[]
            #contamos el numero de articulos que hay en cada carrera y guardamos en vector_contador
            ar=consultar_articulos_facultad(str(ids_facultad[cont]))
            vector_contador.append(Cuenta_registros(ar))
            for c in ar:
                doc=" "
                vec_temp=[]
                #print(c.titulo)
                vec_temp.append(c.titulo)
                vec_temp.append(c.url)
                vec_temp.append(c.iSSN)
                vec_temp.append(c.volumen)
                doc=str(c.documento)
                vec_temp.append(doc)
                #print(doc)
                vec_temp.append(c.first_name)
                vec_temp.append(c.revista.Nombre)
                vector_articulos.append(vec_temp)
            vector_articulos_final.append(vector_articulos)

            cont=cont+1
            cont1=0
        for llena in vector_contador:
            vec_temp=[]
            vec_temp.append(nombres_facultad[cont1])
            vec_temp.append(vector_contador[cont1])
            vec_temp.append(vector_articulos_final[cont1])
            vector_final.append(vec_temp)
            cont1=cont1+1
        json=serializaVector(vector_final)
        print (json)
        return json
        #guardamos los articulos encontrados en esta carrera
def ProcesaGraficaCampusTodo(uni):

        camp=campus.objects.filter(universidad__id=uni)

        nombres_campus=[] #para los nombres de las carreras
        ids_campus=[]     #para las ids de las carreras
        vector_contador=[] # para los vectores contadores de las carreras
        vector_final=[]    # para guardar el vector con la carrera y su repeticion
        vector_articulos=[]
        #guardamos en los vectores todos los nombres y ids de las carreras
        for row in camp:
            nombres_campus.append(row.Nombre)
            ids_campus.append(row.id)
        #hafemos la consulta a la bd de cada carrera segun una id del vector de ids carrera
        vector_articulos_final=[]
        cont=0
        for contAR in ids_campus:
            vector_articulos=[]
            #contamos el numero de articulos que hay en cada carrera y guardamos en vector_contador
            ar=consultar_articulos_campus(str(ids_campus[cont]))
            vector_contador.append(Cuenta_registros(ar))
            for c in ar:
                doc=" "
                vec_temp=[]
                #print(c.titulo)
                vec_temp.append(c.titulo)
                vec_temp.append(c.url)
                vec_temp.append(c.iSSN)
                vec_temp.append(c.volumen)
                doc=str(c.documento)
                vec_temp.append(doc)
                #print(doc)
                vec_temp.append(c.first_name)
                vec_temp.append(c.revista.Nombre)
                vector_articulos.append(vec_temp)
            vector_articulos_final.append(vector_articulos)

            cont=cont+1

            cont1=0
        for llena in vector_contador:
            vec_temp=[]
            vec_temp.append(nombres_campus[cont1])
            vec_temp.append(vector_contador[cont1])
            vec_temp.append(vector_articulos_final[cont1])
            vector_final.append(vec_temp)
            cont1=cont1+1

            cont2=0

        json=serializaVector(vector_final)
        #print (json)
        return json
        #guardamos los articulos encontrados en esta carrera
def ProcesaGraficaUniversidadTodo(zona):

        univer=universidad.objects.filter(zona__id=zona)
        nombres_universidad=[] #para los nombres de las carreras
        ids_universidad=[]     #para las ids de las carreras
        vector_contador=[] # para los vectores contadores de las carreras
        vector_final=[]    # para guardar el vector con la carrera y su repeticion
        vector_articulos=[]
        #guardamos en los vectores todos los nombres y ids de las carreras
        for row in univer:
            nombres_universidad.append(row.Nombre)
            ids_universidad.append(row.id)
        #hafemos la consulta a la bd de cada carrera segun una id del vector de ids carrera
        vector_articulos_final=[]
        cont=0
        for contAR in ids_universidad:
            vector_articulos=[]
            #contamos el numero de articulos que hay en cada carrera y guardamos en vector_contador
            ar=consultar_articulos_universidad(str(ids_universidad[cont]))
            vector_contador.append(Cuenta_registros(ar))
            for c in ar:
                doc=" "
                vec_temp=[]
                #print(c.titulo)
                vec_temp.append(c.titulo)
                vec_temp.append(c.url)
                vec_temp.append(c.iSSN)
                vec_temp.append(c.volumen)
                doc=str(c.documento)
                vec_temp.append(doc)
                #print(doc)
                vec_temp.append(c.first_name)
                vec_temp.append(c.revista.Nombre)
                vector_articulos.append(vec_temp)
            vector_articulos_final.append(vector_articulos)
            cont=cont+1

            cont1=0
        for llena in vector_contador:
            vec_temp=[]
            vec_temp.append(nombres_universidad[cont1])
            vec_temp.append(vector_contador[cont1])
            vec_temp.append(vector_articulos_final[cont1])
            vector_final.append(vec_temp)
            cont1=cont1+1

            cont2=0
        json=serializaVector(vector_final)
        print (json)
        return json
        #guardamos los articulos encontrados en esta carrera
def ProcesaGraficaZonaTodo():

        zon=zona.objects.filter(pais__id=52)
        nombres_zona=[] #para los nombres de las carreras
        ids_zona=[]     #para las ids de las carreras
        vector_contador=[] # para los vectores contadores de las carreras
        vector_final=[]    # para guardar el vector con la carrera y su repeticion
        vector_articulos=[]
        #guardamos en los vectores todos los nombres y ids de las carreras
        for row in zon:
            nombres_zona.append(row.Nombre)
            ids_zona.append(row.id)
        #hafemos la consulta a la bd de cada carrera segun una id del vector de ids carrera
        vector_articulos_final=[]
        cont=0
        for contAR in ids_zona:
            vector_articulos=[]
            #contamos el numero de articulos que hay en cada carrera y guardamos en vector_contador
            ar=consultar_articulos_zona(str(ids_zona[cont]))
            vector_contador.append(Cuenta_registros(ar))
            for c in ar:
                doc=" "
                vec_temp=[]
                #print(c.titulo)
                vec_temp.append(c.titulo)
                vec_temp.append(c.url)
                vec_temp.append(c.iSSN)
                vec_temp.append(c.volumen)
                doc=str(c.documento)
                vec_temp.append(doc)
                #print(doc)
                vec_temp.append(c.first_name)
                vec_temp.append(c.revista.Nombre)
                vector_articulos.append(vec_temp)
            vector_articulos_final.append(vector_articulos)
            cont=cont+1

            cont1=0
        for llena in vector_contador:
            vec_temp=[]
            vec_temp.append(nombres_zona[cont1])
            vec_temp.append(vector_contador[cont1])
            vec_temp.append(vector_articulos_final[cont1])
            vector_final.append(vec_temp)
            cont1=cont1+1

            cont2=0

        json=serializaVector(vector_final)
        print (json)
        return json
        #guardamos los articulos encontrados en esta carrera













def serializaVector(vector):
    v=json.dumps(vector)
    return v


def Cuenta_registros(obj):
    contador=0;
    for row in obj:
        contador=contador+1
    return contador



class Docs_pdf(View):
    def get(self, request, *args, **kwargs):
        print("holaaaaa")
        response = HttpResponse(content_type='application/pdf')
        return response


class Reporte(View):
  def get(self, request, *args, **kwargs):
      #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        self.tabla(pdf)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
  def cabecera(self,pdf):
          #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
          archivo_imagen = settings.MEDIA_ROOT+'/reportes/UTC.png'
          #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
          #                             x    y
          pdf.drawImage(archivo_imagen, 10, 740, 120, 90,preserveAspectRatio=True)
          #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
          pdf.setFont("Helvetica", 16)
          #Dibujamos una cadena en la ubicación X,Y especificada
          # x=590
          #  y=840
          #              x    y
          pdf.drawString(190, 800, "UNIDAD DE INVESTIGACIÓN UTC")
          pdf.setFont("Helvetica", 14)
          pdf.drawString(255, 770, "Artículos Científicos")

  def tabla(self,pdf):
          styles=getSampleStyleSheet()
          y_table = 650
          x_table=60
          y_ocupaTable=600
          x_ocupaTable=800
          #Creamos una tupla de encabezados para neustra tabla
          p=Paragraph('DOCUMENTO',styles['Normal'])
          encabezados = ('TITULO', 'URL','ISSN','VOLUMEN',p,'AUTOR','REVISTA')

          obj=consultar_articulos_carrera(var)
          print (obj)
          detalles = [( zon.titulo, zon.url,zon.iSSN,zon.volumen,zon.documento,zon.first_name,zon.Nombre) for zon in obj]
          #Establecemos el tamaño de cada una de las columnas de la tabla
          #                      encabezado     contenido           colum 1   colum 2
          detalle_orden = Table([encabezados]+ detalles, colWidths=[2* cm,3 * cm,2* cm,3 * cm,2* cm,3 * cm,2* cm])
          #Aplicamos estilos a las celdas de la tabla
          detalle_orden.setStyle(  TableStyle(
              [       #La primera fila(encabezados) va a estar centrada
                      #('ALIGN',(0,0),(3,0),'CENTER'),

                      #Los bordes de todas las celdas serán de color negro y con un grosor de 1

                      ('GRID', (0, 0), (-1, -1), 1, colors.black),
                      #El tamaño de las letras de cada una de las celdas será de 10
                      ('FONTSIZE', (0, 0), (-1, -1), 10),
                      ]
              ))
          #Establecemos el tamaño de la hoja que ocupará la tabla
          detalle_orden.wrapOn(pdf, y_ocupaTable, x_ocupaTable)
          #Definimos la coordenada donde se dibujará la tabla
          detalle_orden.drawOn(pdf, x_table,y_table)
          #Con show page hacemos un corte de página para pasar a la siguient
def consultar_articulos_carrera(valor):
    query ='SELECT "Articulos_Cientificos_articulos_cientificos".id,titulo,url,'
    query2= ' "iSSN",volumen,"Articulos_Cientificos_articulos_cientificos".documento,'
    query3= ' "auth_user".id,"auth_user".first_name,"Revista_revista".id ,"Revista_revista"."Nombre","carrera_carrera"."Nombre"'
    query4= ' FROM "Articulos_Cientificos_articulos_cientificos","autoresArticulos_autoresarticulos",'
    query5= ' "auth_user","Investigador_investigador","informacionLaboral_informacionlaboral",'
    query6= ' "carrera_carrera","Revista_revista"'
    query7= ' WHERE "Articulos_Cientificos_articulos_cientificos".id = "autoresArticulos_autoresarticulos".articulo_id'
    query8= ' AND "autoresArticulos_autoresarticulos".user_id= "auth_user".id'
    query9= ' and "auth_user".id= "Investigador_investigador".user_id'
    query10=' and "Investigador_investigador"."informacionLaboral_id"="informacionLaboral_informacionlaboral".id'
    query11=' and "informacionLaboral_informacionlaboral".carrera_id="carrera_carrera".id'
    query12=' and  "Revista_revista".id ="Articulos_Cientificos_articulos_cientificos".revista_id'
    txt="'Primero'"
    query13=' and "autoresArticulos_autoresarticulos"."gradoAutoria"= '+txt
    query14=' and "carrera_carrera".id='+valor
    queryTotal=query+query2+query3+query4+query5+query6+query7+query8+query9+query10+query11+query12+query13+query14
    #print(queryTotal)
    ar=articulos_cientificos.objects.raw(queryTotal)
    #print (ar)
    return(ar)

def consultar_articulos_facultad(valor):
    query ='SELECT "Articulos_Cientificos_articulos_cientificos".id,titulo,url,'
    query2= ' "iSSN",volumen,"Articulos_Cientificos_articulos_cientificos".documento,'
    query3= ' "auth_user".id,"auth_user".first_name,"Revista_revista".id ,"Revista_revista"."Nombre"'
    query4= ' FROM "Articulos_Cientificos_articulos_cientificos","autoresArticulos_autoresarticulos",'
    query5= ' "auth_user","Investigador_investigador","informacionLaboral_informacionlaboral",'
    query6= ' "facultad_facultad","Revista_revista"'
    query7= ' WHERE "Articulos_Cientificos_articulos_cientificos".id = "autoresArticulos_autoresarticulos".articulo_id'
    query8= ' AND "autoresArticulos_autoresarticulos".user_id= "auth_user".id'
    query9= ' and "auth_user".id= "Investigador_investigador".user_id'
    query10=' and "Investigador_investigador"."informacionLaboral_id"="informacionLaboral_informacionlaboral".id'
    query11=' and "informacionLaboral_informacionlaboral".facultad_id="facultad_facultad".id'
    query12=' and  "Revista_revista".id ="Articulos_Cientificos_articulos_cientificos".revista_id'
    txt="'Primero'"
    query13=' and "autoresArticulos_autoresarticulos"."gradoAutoria"= '+txt
    query14=' and "facultad_facultad".id='+valor
    queryTotal=query+query2+query3+query4+query5+query6+query7+query8+query9+query10+query11+query12+query13+query14
    #print(queryTotal)
    ar=articulos_cientificos.objects.raw(queryTotal)
    #print (ar)
    return(ar)

def consultar_articulos_campus(valor):
    query ='SELECT "Articulos_Cientificos_articulos_cientificos".id,titulo,url, "iSSN",volumen,'
    query2= '"Articulos_Cientificos_articulos_cientificos".documento, "auth_user".first_name,"Revista_revista"."Nombre"'
    query3= ' FROM "Articulos_Cientificos_articulos_cientificos","autoresArticulos_autoresarticulos", "auth_user",'
    query4= ' "Investigador_investigador","informacionLaboral_informacionlaboral", "facultad_facultad","campus_campus","Revista_revista"'
    query5= ' WHERE "Articulos_Cientificos_articulos_cientificos".id = "autoresArticulos_autoresarticulos".articulo_id '
    query6= ' AND "autoresArticulos_autoresarticulos".user_id= "auth_user".id'
    query7= ' and "auth_user".id= "Investigador_investigador".user_id'
    query8= ' and "Investigador_investigador"."informacionLaboral_id"="informacionLaboral_informacionlaboral".id'
    query9=' and "informacionLaboral_informacionlaboral".facultad_id="facultad_facultad".id'
    query10=' and "Revista_revista".id="Articulos_Cientificos_articulos_cientificos".revista_id'
    query11=' and "facultad_facultad".campus_id ="campus_campus".id'
    txt="'Primero'"
    query12=' and "autoresArticulos_autoresarticulos"."gradoAutoria"='+txt
    query13=' and "campus_campus".id='+valor
    queryTotal=query+query2+query3+query4+query5+query6+query7+query8+query9+query10+query11+query12+query13
    #print(queryTotal)
    ar=articulos_cientificos.objects.raw(queryTotal)
    #print (ar)
    return(ar)

def consultar_articulos_universidad(valor):
    query ='SELECT "Articulos_Cientificos_articulos_cientificos".id,titulo,url, "iSSN",volumen,'
    query2= '"Articulos_Cientificos_articulos_cientificos".documento, "auth_user".first_name,"Revista_revista"."Nombre"'
    query3= ' FROM "Articulos_Cientificos_articulos_cientificos","autoresArticulos_autoresarticulos", "auth_user",'
    query4= ' "Investigador_investigador","informacionLaboral_informacionlaboral", "facultad_facultad","campus_campus","Revista_revista","universidad_universidad"'
    query5= ' WHERE "Articulos_Cientificos_articulos_cientificos".id = "autoresArticulos_autoresarticulos".articulo_id '
    query6= ' AND "autoresArticulos_autoresarticulos".user_id= "auth_user".id'
    query7= ' and "auth_user".id= "Investigador_investigador".user_id'
    query8= ' and "Investigador_investigador"."informacionLaboral_id"="informacionLaboral_informacionlaboral".id'
    query9=' and "informacionLaboral_informacionlaboral".facultad_id="facultad_facultad".id'
    query10=' and "Revista_revista".id="Articulos_Cientificos_articulos_cientificos".revista_id'
    query11=' and "facultad_facultad".campus_id ="campus_campus".id and "campus_campus".universidad_id ="universidad_universidad".id'
    txt="'Primero'"
    query12=' and "autoresArticulos_autoresarticulos"."gradoAutoria"='+txt
    query13=' and "universidad_universidad".id='+valor
    queryTotal=query+query2+query3+query4+query5+query6+query7+query8+query9+query10+query11+query12+query13
    #print(queryTotal)
    ar=articulos_cientificos.objects.raw(queryTotal)
    #print (ar)
    return(ar)

def consultar_articulos_zona(valor):
    query ='SELECT "Articulos_Cientificos_articulos_cientificos".id,titulo,url, "iSSN",volumen,'
    query2= '"Articulos_Cientificos_articulos_cientificos".documento, "auth_user".first_name,"Revista_revista"."Nombre"'
    query3= ' FROM "Articulos_Cientificos_articulos_cientificos","autoresArticulos_autoresarticulos", "auth_user",'
    query4= ' "Investigador_investigador","informacionLaboral_informacionlaboral", "facultad_facultad","campus_campus","Revista_revista","universidad_universidad","zona_zona"'
    query5= ' WHERE "Articulos_Cientificos_articulos_cientificos".id = "autoresArticulos_autoresarticulos".articulo_id '
    query6= ' AND "autoresArticulos_autoresarticulos".user_id= "auth_user".id'
    query7= ' and "auth_user".id= "Investigador_investigador".user_id'
    query8= ' and "Investigador_investigador"."informacionLaboral_id"="informacionLaboral_informacionlaboral".id'
    query9=' and "informacionLaboral_informacionlaboral".facultad_id="facultad_facultad".id'
    query10=' and "Revista_revista".id="Articulos_Cientificos_articulos_cientificos".revista_id'
    query11=' and "facultad_facultad".campus_id ="campus_campus".id and "campus_campus".universidad_id ="universidad_universidad".id and "universidad_universidad".zona_id="zona_zona".id'
    txt="'Primero'"
    query12=' and "autoresArticulos_autoresarticulos"."gradoAutoria"='+txt
    query13=' and "zona_zona".id='+valor
    queryTotal=query+query2+query3+query4+query5+query6+query7+query8+query9+query10+query11+query12+query13
    #print(queryTotal)
    ar=articulos_cientificos.objects.raw(queryTotal)
    #print (ar)
    return(ar)




def consultar_libros_carrera(valor):


    query ='SELECT "Libro_libro".id,"Titulo",'
    query2= '"ISBN","Editorial","Url",tipo,"Libro_libro"."Documento","auth_user".first_name'
    query3= ' "auth_user".id,"auth_user".first_name,"Revista_revista".id ,"Revista_revista"."Nombre"'
    query4= ' FROM "Libro_libro","autoresLibro_autoreslibro", "auth_user",'
    query5= ' "Investigador_investigador","informacionLaboral_informacionlaboral", "carrera_carrera"'
    query6= ' WHERE "Libro_libro".id = "autoresLibro_autoreslibro".libro_id '
    query7= ' AND "autoresLibro_autoreslibro".user_id= "auth_user".id'
    query8= ' and "auth_user".id= "Investigador_investigador".user_id'
    query9=' and "Investigador_investigador"."informacionLaboral_id"="informacionLaboral_informacionlaboral".id'
    txt="'Primero'"
    query10=' and "autoresLibro_autoreslibro"."gradoAutoria='+txt
    query11=' and "carrera_carrera".id='+valor
    queryTotal=query+query2+query3+query4+query5+query6+query7+query8+query9+query10+query11
    #print(queryTotal)
    ar=articulos_cientificos.objects.raw(queryTotal)
    #print (ar)
    return(ar)





  # c=0
 #  print(id_infolabo[c+1])

    #    for au_ar in autorarticulo:
    #        investigador=Investigador.objects.filter(user=au_ar.user)
    #        informacionLaboral=informacionLaboral.objects.filter(id=investigador.informacionLaboral)
    #        if informacionLaboral.carrera_id==valor
    #           articuloCaer.ADD



    #    articulos = articulos_cientificos.objects.all()

    #    carrer=carrera.objects.filter(facultad__id=id_facul)
class BusquedaFiltroFacultadView(TemplateView):


    def get(self,request,*args, **kwargs):
        campus=request.GET['campus']
        facultad=request.GET['facultad']
        carrera=request.GET['carrera']
        filtroY=request.GET['filtroY']
        universidad=request.GET['universidad']
        zona=request.GET['zona']
        print(campus)
        print(facultad)
        print(carrera)
        print(filtroY)
        print(universidad)
        print(zona)


        if(int(zona)>0 and int(universidad)> 0 and int(campus)>0 and int(facultad)==0 and int(carrera)==0 and int(filtroY)==2):
            print('entre en articulos campus')
            print (campus);
            obj= consultar_Articulos_campus(campus)
            #num_ar=Cuenta_registros(obj)
            #var="1"
            #for a in obj:
             #     print(a.Nombre)
            data= serializers.serialize('json',obj,
                           fields=('titulo','url','iSSN','volumen','documento','first_name','Nombre'))
          #print(data)
            return HttpResponse(data, content_type='application/json')

        if(int(zona)>0 and int(universidad)> 0 and int(campus)>0 and int(facultad)>0 and int(carrera)==0 and int(filtroY)==2):
            print('entre articulos facultad')
            print (campus);
            obj= consultar_articulos_facultad(facultad)
            #num_ar=Cuenta_registros(obj)
            #var="1"
            #for a in obj:
             #     print(a.Nombre)
            data= serializers.serialize('json',obj,
                           fields=('titulo','url','iSSN','volumen','documento','first_name','Nombre'))
          #print(data)
            return HttpResponse(data, content_type='application/json')


def consultar_Articulos_campus(valor):
    query ='SELECT "Articulos_Cientificos_articulos_cientificos".id,titulo,url, "iSSN",volumen,'
    query2= '"Articulos_Cientificos_articulos_cientificos".documento, "auth_user".first_name,"Revista_revista"."Nombre"'
    query3= ' FROM "Articulos_Cientificos_articulos_cientificos","autoresArticulos_autoresarticulos", "auth_user",'
    query4= ' "Investigador_investigador","informacionLaboral_informacionlaboral", "facultad_facultad","campus_campus","Revista_revista"'
    query5= ' WHERE "Articulos_Cientificos_articulos_cientificos".id = "autoresArticulos_autoresarticulos".articulo_id '
    query6= ' AND "autoresArticulos_autoresarticulos".user_id= "auth_user".id'
    query7= ' and "auth_user".id= "Investigador_investigador".user_id'
    query8= ' and "Investigador_investigador"."informacionLaboral_id"="informacionLaboral_informacionlaboral".id'
    query9=' and "informacionLaboral_informacionlaboral".facultad_id="facultad_facultad".id'
    query10=' and "Revista_revista".id="Articulos_Cientificos_articulos_cientificos".revista_id'

    query11=' and "facultad_facultad".id="campus_campus".id'
    txt="'Primero'"
    query12=' and "autoresArticulos_autoresarticulos"."gradoAutoria"='+txt
    query13=' and "campus_campus".id='+valor
    queryTotal=query+query2+query3+query4+query5+query6+query7+query8+query9+query10+query11+query12+query13
    #print(queryTotal)
    ar=articulos_cientificos.objects.raw(queryTotal)
    #print (ar)
    return(ar)
def consultar_articulos_facultad(valor):
    query ='SELECT "Articulos_Cientificos_articulos_cientificos".id,titulo,url,'
    query2= ' "iSSN",volumen,"Articulos_Cientificos_articulos_cientificos".documento,'
    query3= ' "auth_user".id,"auth_user".first_name,"Revista_revista".id ,"Revista_revista"."Nombre"'
    query4= ' FROM "Articulos_Cientificos_articulos_cientificos","autoresArticulos_autoresarticulos",'
    query5= ' "auth_user","Investigador_investigador","informacionLaboral_informacionlaboral",'
    query6= ' "facultad_facultad","Revista_revista"'
    query7= ' WHERE "Articulos_Cientificos_articulos_cientificos".id = "autoresArticulos_autoresarticulos".articulo_id'
    query8= ' AND "autoresArticulos_autoresarticulos".user_id= "auth_user".id'
    query9= ' and "auth_user".id= "Investigador_investigador".user_id'
    query10=' and "Investigador_investigador"."informacionLaboral_id"="informacionLaboral_informacionlaboral".id'
    query11=' and "informacionLaboral_informacionlaboral".facultad_id="facultad_facultad".id'
    query12=' and  "Revista_revista".id ="Articulos_Cientificos_articulos_cientificos".revista_id'
    txt="'Primero'"
    query13=' and "autoresArticulos_autoresarticulos"."gradoAutoria"= '+txt
    query14=' and "facultad_facultad".id='+valor
    queryTotal=query+query2+query3+query4+query5+query6+query7+query8+query9+query10+query11+query12+query13+query14
    #print(queryTotal)
    ar=articulos_cientificos.objects.raw(queryTotal)
    #print (ar)
    #print (queryTotal);
    return(ar)


class BusquedaFiltroCampusView(TemplateView):
    def get(self,request,*args, **kwargs):
        campus=request.GET['campus']
        print("el campus es")
        print (campus);
