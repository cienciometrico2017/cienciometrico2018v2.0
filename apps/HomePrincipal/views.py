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
        f=request.GET['f']
        c=request.GET['c']
        fx=request.GET['fx']
        txtC=request.GET['txtC']
        print (f)
        print (c)
        print (fx)
        print(txtC)

        if int(f)>0 and int(c)>0 and int(fx) > 0:


             obj= consultar_articulos_carrera(c)
             num_ar=Cuenta_registros(obj)
        #construyeJson(num_ar,txtC)
             var="1"
             #for a in obj:
        #     print(a.Nombre)
             data= serializers.serialize('json',obj,
                            fields=('titulo','url','iSSN','volumen','documento','first_name','Nombre'))
        #print(data)
             return HttpResponse(data, content_type='application/json')
        elif int(f)>0 and int(c)==0 and int(fx) > 0:
            obj= consultar_articulos_facultad(f)
            num_ar=Cuenta_registros(obj)
       #construyeJson(num_ar,txtC)
            var="1"
            #for a in obj:
       #     print(a.Nombre)
            data= serializers.serialize('json',obj,
                           fields=('titulo','url','iSSN','volumen','documento','first_name','Nombre'))
       #print(data)
            return HttpResponse(data, content_type='application/json')

        else:

            return HttpResponse(1, content_type='application/json')










# funcion que construye el json y lo guarda en una ruta
#def construyeJson(valor,carrer):
#    ruta = {}
#    ruta[carrer] = valor
#    carpeta = 'C:%sworkpase_py\cienciometrico2018v2.0\static\json' % os.sep
#    os.chdir(carpeta)  # esta es la linea que hace que se cambie el lugar de trabajo
#    with open('data1.json', 'w') as outfile:
#        carpeta = 'C:%sworkpase_py\cienciometrico2018v2.0\static\json' % os.sep
#        archivo = json.dump(ruta, outfile)




        # funcion para contar el numero de objetos
def Cuenta_registros(obj):
    contador=0
    for row in obj:
        contador=contador+1
    return contador


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
          y_table = 650
          x_table=60
          y_ocupaTable=600
          x_ocupaTable=800
          #Creamos una tupla de encabezados para neustra tabla
          encabezados = ('TITULO', 'URL','ISSN','VOLUMEN','DOCUMENTO','AUTOR','REVISTA')

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
    query3= ' "auth_user".id,"auth_user".first_name,"Revista_revista".id ,"Revista_revista"."Nombre"'
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





  # c=0
 #  print(id_infolabo[c+1])

    #    for au_ar in autorarticulo:
    #        investigador=Investigador.objects.filter(user=au_ar.user)
    #        informacionLaboral=informacionLaboral.objects.filter(id=investigador.informacionLaboral)
    #        if informacionLaboral.carrera_id==valor
    #           articuloCaer.ADD



    #    articulos = articulos_cientificos.objects.all()



    #    carrer=carrera.objects.filter(facultad__id=id_facul)
