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

from io import BytesIO

from django.http import HttpResponse
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table




#nuevo
import json
import os
import collections
#DSN = "dbname=Cienciometrico2 user=postgres password=1945"
#nuevo


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


# nuevo ////////////////////////////////////////////////////////////////
def grafica(request):

# sql para consulta directa a la bd
    con = psycopg2.connect(DSN)
    libro = []  # declaramos un vector para almacenar los numeros de cedula
    a = ""
    cur = con.cursor()
    query = 'SELECT *FROM "Libro_libro";'
    cur.execute(query)
    cont = 0  # declaramos un contadorpara controlar las iserciones en el vector
    for datos in cur.fetchall():  # ejecutamos la consulta a la base de datos
        # print(datos[4])
        a = datos[2]  # guardamos en una varible el datos de la pos 4 es decir los numeros de cedula de los usuarios
        libro.insert(cont, a)  # incertamos los datosde la consuta en el vector

        cont = cont + 1
    cur.close()
    con.close()





#   escribimos el json




   #consultamos a la bd y traemos los objetos
    zon = zona.objects.all()
    uni = universidad.objects.all()
    facu=facultad.objects.all()
    carrer=carrera.objects.all()

    return render(request, 'Home/Graficas.html',{'zona': zon,'universidad':uni,"facultad":facu, "carrera":carrer })






class BusquedaView(ListView):
    model = zona
    template_name = "Home/Graficas.html"
    context_object_name = 'zona'







class BusquedaAjaxView(TemplateView):


    def get(self,request,*args, **kwargs):
        id_zona=request.GET['id']

        print (id_zona)





        univer=universidad.objects.filter(zona__id=id_zona)
        print(univer)
        data= serializers.serialize('json',univer,
                            fields=('id','Nombre'))
        print(data)
        return HttpResponse(data, content_type='application/json')



class BusquedaCampusView(TemplateView):
    def get(self,request,*args, **kwargs):
        id_uni=request.GET['id']
        print (id_uni)

        facul=campus.objects.filter(universidad__id=id_uni)
        print(facul)
        data= serializers.serialize('json',facul,
                            fields=('id','Nombre'))
        return HttpResponse(data, content_type='application/json')






class BusquedaFacuView(TemplateView):
    def get(self,request,*args, **kwargs):
        id_campus=request.GET['id']
        print (id_campus)

        facul=facultad.objects.filter(campus__id=id_campus)
        print(facul)
        data= serializers.serialize('json',facul,
                            fields=('id','Nombre'))
        return HttpResponse(data, content_type='application/json')

class BusquedaCarreraView(TemplateView):
    def get(self,request,*args, **kwargs):
        id_facul=request.GET['id']
        print (id_facul)

        carrer=carrera.objects.filter(facultad__id=id_facul)
        carrer
        print(carrer)
        data= serializers.serialize('json',carrer,
                            fields=('id','Nombre'))
        print(data)
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
        obj= consultar_articulos_carrera(c)
        num_ar=Cuenta_registros(obj)
        construyeJson(num_ar,txtC)
        data= serializers.serialize('json',obj,
                            fields=('titulo','url','doi','documento','estado'))
        print(data)
        return HttpResponse(data, content_type='application/json')


# funcion que construye el json y lo guarda en una ruta
def construyeJson(valor,carrer):
    ruta = {}
    ruta[carrer] = valor
    carpeta = 'C:%sworkpase_py\cienciometrico2018\static\json' % os.sep
    os.chdir(carpeta)  # esta es la linea que hace que se cambie el lugar de trabajo
    with open('data1.json', 'w') as outfile:
        carpeta = 'C:%sworkpase_py\cienciometrico2018\static\json' % os.sep
        archivo = json.dump(ruta, outfile)


def consultar_articulos_carrera(valor):
    articulos= articulos_cientificos.objects.all()
    query = 'SELECT "Articulos_Cientificos_articulos_cientificos".id,titulo,url,doi,"Articulos_Cientificos_articulos_cientificos".documento,estado'
    query2=  ' FROM "Articulos_Cientificos_articulos_cientificos","autoresArticulos_autoresarticulos","auth_user",'
    query3= ' "Investigador_investigador","informacionLaboral_informacionlaboral",'
    query4= ' "carrera_carrera" WHERE "Articulos_Cientificos_articulos_cientificos".id= "autoresArticulos_autoresarticulos".articulo_id'
    query5= ' AND "autoresArticulos_autoresarticulos".user_id= "auth_user".id and "auth_user".id= "Investigador_investigador".user_id'
    query6= ' and "Investigador_investigador"."informacionLaboral_id"="informacionLaboral_informacionlaboral".id'
    query7= ' and "informacionLaboral_informacionlaboral".carrera_id="carrera_carrera".id'
    query8= ' and "carrera_carrera".id='+valor
    txt="'Primero'"
    query9= 'and "autoresArticulos_autoresarticulos"."gradoAutoria"='+txt

    queryTotal=query+query2+query3+query4+query5+query6+query7+query8+query9
    ar=articulos_cientificos.objects.raw(queryTotal)
    #for z in ar:
        #print(z.titulo)
    return(ar)


        # funcion para contar el numero de objetos
def Cuenta_registros(obj):
    contador=0
    for row in obj:
        contador=contador+1
    return contador


class ReportePersonasPDF(View):


  def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/reportes/UTC.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, "UNIDAD DE INVESTIGACIÓN UTC")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE")


  def get(self, request, *args, **kwargs):
      #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response







  # c=0
 #  print(id_infolabo[c+1])








    #    for au_ar in autorarticulo:
    #        investigador=Investigador.objects.filter(user=au_ar.user)
    #        informacionLaboral=informacionLaboral.objects.filter(id=investigador.informacionLaboral)
    #        if informacionLaboral.carrera_id==valor
    #           articuloCaer.ADD



    #    articulos = articulos_cientificos.objects.all()



    #    carrer=carrera.objects.filter(facultad__id=id_facul)
