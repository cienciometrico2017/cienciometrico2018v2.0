from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
from django.views.generic import CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from apps.Investigador.form import RegistroForm,UserForm, InformacionForm,PasswordForm
from django.contrib.auth.models import User
from apps.informacionLaboral.models import informacionLaboral
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from apps.pais.models import pais
from apps.provincia.models import provincia
from apps.ciudad.models import ciudad
import json

class RegistroUsuario(CreateView):
        model = Investigador
        template_name = "usuario/registrar.html"
        form_class = RegistroForm
        second_form_class = UserForm
        third_form_class = InformacionForm
        success_url = reverse_lazy('usuario:registrar')
        def get_context_data(self, **kwargs):
            persona = Investigador.objects.all()  # Esto si retorna un QuerySet
            exi = persona.exists() #metodo_comprobar
            context= super(RegistroUsuario,self).get_context_data(**kwargs)
            usuario = self.request.user.id  #usuario loggeado
            perfil = Investigador.objects.get(user_id=usuario) #buscar el perfil del usuario
            roles = perfil.roles.all() # todos los roles
            privi = [] #array vacio
            privilegios = [] #array vacio
            privilegio = [] #array vacio
            for r in roles:
                 privi.append(r.id) #almacena roles por id
            for p in privi:
                 roles5 = Rol.objects.get(pk=p)
                 priv = roles5.privilegios.all()
                 for pr in priv:
                     privilegios.append(pr.codename)
            for i in privilegios:
                 if i not in privilegio:
                     privilegio.append(i)
            context['usuario'] = privilegio
            if 'form' not in context:
                context['form']= self.form_class(self.request.GET)
            if 'form2' not in context:
                context['form2']= self.second_form_class(self.request.GET)
            if 'form3' not in context:
                context['form3']= self.third_form_class(self.request.GET)
            return context
        def post(self, request, *args, **kwargs):
            self.object= self.get_object
            form= self.form_class(request.POST)
            form2 = self.second_form_class(request.POST)
            form3 = self.third_form_class(request.POST)
            if form.is_valid() and form2.is_valid() :
                investigador = form.save(commit=False)
                investigador.user = form2.save()
                #investigador.u ser.set_password(form2.cleaned_data['password'])
                investigador.user.save()
                investigador.informacionLaboral=form3.save()
                investigador.informacionLaboral.save()
                investigador.save()
                form.save_m2m()
                data = form2.cleaned_data
                usu = data['username']
                passw = data['password']
                subject = 'Usuario creado exitosamente'
                text_content = 'This is an important message.'
                html_content = '<p>Username:<strong>' + usu + '</strong></p><p>Password:<strong>' + passw + '</strong></p>'
                msg = EmailMultiAlternatives(
                   subject,
                   text_content,
                   'admin@mail.com',  # FROM
                   [data['email']]
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                messages.success(request,('Se ha registrado satisfactoriamente'),extra_tags='alert')
                return HttpResponseRedirect(self.get_success_url())
            else:
                messages.error(request,('Por favor registrese nuevamente'))
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


class ActualizarUsuario(UpdateView):
    model = Investigador
    second_model = User
    third_model = informacionLaboral
    template_name = "usuario/update.html"
    form_class = RegistroForm
    second_form_class = UserForm
    third_form_class = InformacionForm
    success_url = reverse_lazy('usuario:registrar')
    def get_context_data(self, **kwargs):
        context = super(ActualizarUsuario, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        perfil = self.model.objects.get(id=pk)
        usuario = self.second_model.objects.get(id=perfil.user_id)
        if perfil.informacionLaboral:
            informacion = perfil.informacionLaboral
        else:
            f = informacionLaboral.objects.create()
            perfil.informacionLaboral = f
            perfil.save()
            informacion = perfil.informacionLaboral
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
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=usuario)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance=informacion)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        perfil = self.model.objects.get(id=id_solicitud)
        usuario = self.second_model.objects.get(id=perfil.user_id)
        informacion = self.third_model.objects.get(id=perfil.informacionLaboral_id)
        form = self.form_class(request.POST, request.FILES , instance=perfil)
        form2 = self.second_form_class(request.POST, request.FILES, instance=usuario)
        form3 = self.third_form_class(request.POST, request.FILES,instance=informacion)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            perfil = form.save(commit=False)
            perfil.user = form2.save()
            perfil.user.save()
            perfil.informacionLaboral =form3.save()
            perfil.informacionLaboral.save()
            perfil.save()
            form.save_m2m()
            messages.success(request, ('La información se ha actualizado correctamente.'))
            return HttpResponseRedirect('/index/')
        else:
            messages.error(request, ('Revise el formulario, no se ha podido enviar la información'))
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

class ActualizarPassword(UpdateView):
    model = Investigador
    second_model = User
    template_name = "usuario/updatePass.html"
    form_class = PasswordForm
    success_url = reverse_lazy('usuario:registrar')

    def get_context_data(self, **kwargs):
        context = super(ActualizarPassword, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        perfil = self.model.objects.get(id=pk)
        usuario = self.second_model.objects.get(id=perfil.user_id)
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
        if 'form2' not in context:
            context['form2'] = self.form_class(instance=usuario)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        perfil = self.model.objects.get(id=id_solicitud)
        usuario = self.second_model.objects.get(id=perfil.user_id)
        form2 = self.form_class(request.POST, instance=usuario)
        password1 = self.request.POST['password']
        password2 = self.request.POST['password1']
        if form2.is_valid() and password1 == password2:

            perfil.user = form2.save()
            perfil.user.set_password(perfil.user.password)
            perfil.user.save()
            perfil.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, ('Se a completado la petición, contraseña actualizada'))
            return HttpResponseRedirect('/index/')
        else:
            messages.error(request, ('Las contraseñas no coinciden, vuelva a intentarlo'))
            return HttpResponseRedirect(f'/investigador/editarPass/{perfil.user_id}')


def autor(request):
    results = []
    dbjson = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        #username = request.POST.get('username')
        first_name = request.POST.get('name')
        last_name = request.POST.get('lastname')
        print('Mi email', email,first_name,last_name)

        if not User.objects.filter(email=email):
            rol = Rol.objects.get(id=1);
            us = User.objects.create_user(username=email, email=email, password = email , first_name=first_name, last_name=last_name, )
            #us.save()
            inf = informacionLaboral.objects.create()
            inf.save()
            inv = Investigador(cambio = False, user= us, informacionLaboral=inf)
            inv.save(force_insert=True)
            inv.roles.add(rol)
            dbjson['text'] = us.first_name + ' ' + us.last_name
            dbjson['value'] = us.id
            results.append(dbjson)
            data_json = json.dumps(results)
            mimetype = "application/json"
            return HttpResponse(data_json, mimetype)

def new(request):
    #nuevoUser("nahir.dugarte9193@utc.edu.ec", "1753479193", "NAHIR YERELY", "DUGARTE JIMENEZ	")


    '''
    rol = Rol.objects.get(id=1)
    us = User.objects.create_user(username='alex.cevallos@utc.edu.ec', email='alex.cevallos@utc.edu.ec', password='0502594427', first_name='Alex', last_name='Cevallos',)
    us.save()
    inf = informacionLaboral.objects.create()
    inf.save()
    inv = Investigador(cedula = '0502594427',cambio = False, user = us, informacionLaboral = inf)
    inv.save(force_insert=True)
    inv.roles.add(rol)

    us = User.objects.create_user(username='gustavo.rodriguez@utc.edu.ec', email='sochoa@uchile.edu.ec', password='1757001357',first_name='Sergio', last_name='Ochoa', )
    us.save()
    inf = informacionLaboral.objects.create()
    inf.save()
    inv = Investigador(cedula='1757001357', cambio=True, user=us, informacionLaboral=inf)
    inv.save(force_insert=True)
    inv.roles.add(rol)

    us = User.objects.create_user(username='jonny.allauca0@utc.edu.ec', email='jonny.allauca0@utc.edu.ec', password='1725776320', first_name='Jonny Javier', last_name='Allauca Ch', )
    us.save()
    inf = informacionLaboral.objects.create()
    inf.save()
    inv = Investigador(cedula='1725776320', cambio=True, user=us, informacionLaboral=inf)
    inv.save(force_insert=True)
    inv.roles.add(rol)
    '''
    return HttpResponseRedirect('/index/')

def nuevoUser(email, cedula, name, last):
    rol = Rol.objects.get(id=1)
    us = User.objects.create_user(username=email, email=email, password=cedula, first_name=name, last_name=last, )
    us.save()
    inf = informacionLaboral.objects.create()
    inf.save()
    inv = Investigador(cedula=cedula, cambio=False, user=us, informacionLaboral=inf)
    inv.save(force_insert=True)
    inv.roles.add(rol)



"""
def new(request):
    ciudad.objects.create(Nombre='CUENCA', provincia_id=199)
    ciudad.objects.create(Nombre='GIRON', provincia_id=199)
    ciudad.objects.create(Nombre='GUALACEO', provincia_id=199)
    ciudad.objects.create(Nombre='NABON', provincia_id=199)
    ciudad.objects.create(Nombre='PAUTE', provincia_id=199)
    ciudad.objects.create(Nombre='PUCARA', provincia_id=199)
    ciudad.objects.create(Nombre='SAN FERNANDO', provincia_id=199)
    ciudad.objects.create(Nombre='STA. ISABEL', provincia_id=199)
    ciudad.objects.create(Nombre='SIGSIG', provincia_id=199)
    ciudad.objects.create(Nombre='OÑA', provincia_id=199)
    ciudad.objects.create(Nombre='CHORDELEG', provincia_id=199)
    ciudad.objects.create(Nombre='EL PAN', provincia_id=199)
    ciudad.objects.create(Nombre='SEVILLA DE ORO', provincia_id=199)
    ciudad.objects.create(Nombre='GUACHAPALA', provincia_id=199)
    ciudad.objects.create(Nombre='CAMILO PONCE E.', provincia_id=199)

    ciudad.objects.create(Nombre='GUARANDA', provincia_id=200)
    ciudad.objects.create(Nombre='CHILLANES', provincia_id=200)
    ciudad.objects.create(Nombre='CHIMBO', provincia_id=200)
    ciudad.objects.create(Nombre='ECHEANDIA', provincia_id=200)
    ciudad.objects.create(Nombre='SAN MIGUEL', provincia_id=200)
    ciudad.objects.create(Nombre='CALUMA', provincia_id=200)
    ciudad.objects.create(Nombre='LAS NAVES', provincia_id=200)

    ciudad.objects.create(Nombre='AZOGUES', provincia_id=201)
    ciudad.objects.create(Nombre='BIBLIAN', provincia_id=201)
    ciudad.objects.create(Nombre='CAÑAR', provincia_id=201)
    ciudad.objects.create(Nombre='LA TRONCAL', provincia_id=201)
    ciudad.objects.create(Nombre='EL TAMBO', provincia_id=201)
    ciudad.objects.create(Nombre='DELEG', provincia_id=201)
    ciudad.objects.create(Nombre='SUSCAL', provincia_id=201)

    ciudad.objects.create(Nombre='TULCAN', provincia_id=202)
    ciudad.objects.create(Nombre='BOLIVAR', provincia_id=202)
    ciudad.objects.create(Nombre='ESPEJO', provincia_id=202)
    ciudad.objects.create(Nombre='MIRA', provincia_id=202)
    ciudad.objects.create(Nombre='MONTUFAR', provincia_id=202)
    ciudad.objects.create(Nombre='SAN PEDRO DE HUACA', provincia_id=202)

    ciudad.objects.create(Nombre='LATACUNGA', provincia_id=204)
    ciudad.objects.create(Nombre='LA MANA', provincia_id=204)
    ciudad.objects.create(Nombre='PANGUA', provincia_id=204)
    ciudad.objects.create(Nombre='PUJILI', provincia_id=204)
    ciudad.objects.create(Nombre='SALCEDO', provincia_id=204)
    ciudad.objects.create(Nombre='SAQUISILI', provincia_id=204)
    ciudad.objects.create(Nombre='SIGCHOS', provincia_id=204)

    ciudad.objects.create(Nombre='RIOBAMBA', provincia_id=203)
    ciudad.objects.create(Nombre='ALAUSI', provincia_id=203)
    ciudad.objects.create(Nombre='COLTA', provincia_id=203)
    ciudad.objects.create(Nombre='CHAMBO', provincia_id=203)
    ciudad.objects.create(Nombre='CHUNCHI', provincia_id=203)
    ciudad.objects.create(Nombre='GUAMOTE', provincia_id=203)
    ciudad.objects.create(Nombre='GUANO', provincia_id=203)
    ciudad.objects.create(Nombre='PALLATANGA', provincia_id=203)
    ciudad.objects.create(Nombre='PENIPE', provincia_id=203)
    ciudad.objects.create(Nombre='CUMANDA', provincia_id=203)

    ciudad.objects.create(Nombre='MACHALA', provincia_id=205)
    ciudad.objects.create(Nombre='ARENILLAS', provincia_id=205)
    ciudad.objects.create(Nombre='ATAHUALPA', provincia_id=205)
    ciudad.objects.create(Nombre='BALSAS', provincia_id=205)
    ciudad.objects.create(Nombre='CHILLA', provincia_id=205)
    ciudad.objects.create(Nombre='EL GUABO', provincia_id=205)
    ciudad.objects.create(Nombre='HUAQUILLAS', provincia_id=205)
    ciudad.objects.create(Nombre='MARCABELI', provincia_id=205)
    ciudad.objects.create(Nombre='PASAJE', provincia_id=205)
    ciudad.objects.create(Nombre='PIÑAS', provincia_id=205)
    ciudad.objects.create(Nombre='PORTOVELO', provincia_id=205)
    ciudad.objects.create(Nombre='SANTA ROSA', provincia_id=205)
    ciudad.objects.create(Nombre='ZARUMA', provincia_id=205)
    ciudad.objects.create(Nombre='LAS LAJAS', provincia_id=205)

    ciudad.objects.create(Nombre='ESMERALDAS', provincia_id=206)
    ciudad.objects.create(Nombre='ELOY ALFARO', provincia_id=206)
    ciudad.objects.create(Nombre='MUISNE', provincia_id=206)
    ciudad.objects.create(Nombre='QUININDE', provincia_id=206)
    ciudad.objects.create(Nombre='SAN LORENZO', provincia_id=206)
    ciudad.objects.create(Nombre='ATACAMES', provincia_id=206)
    ciudad.objects.create(Nombre='RIOVERDE', provincia_id=206)

    ciudad.objects.create(Nombre='GUAYAQUIL', provincia_id=208)
    ciudad.objects.create(Nombre='ALFREDO BAQUERIZO MORENO (JUJAN)', provincia_id=208)
    ciudad.objects.create(Nombre='BALAO', provincia_id=208)
    ciudad.objects.create(Nombre='BALZAR', provincia_id=208)
    ciudad.objects.create(Nombre='COLIMES', provincia_id=208)
    ciudad.objects.create(Nombre='DAULE', provincia_id=208)
    ciudad.objects.create(Nombre='DURAN', provincia_id=208)
    ciudad.objects.create(Nombre='EMPALME', provincia_id=208)
    ciudad.objects.create(Nombre='EL TRIUNFO', provincia_id=208)
    ciudad.objects.create(Nombre='MILAGRO', provincia_id=208)
    ciudad.objects.create(Nombre='NARANJAL', provincia_id=208)
    ciudad.objects.create(Nombre='NARANJITO', provincia_id=208)
    ciudad.objects.create(Nombre='PALESTINA', provincia_id=208)
    ciudad.objects.create(Nombre='PEDRO CARBO', provincia_id=208)
    ciudad.objects.create(Nombre='SALINAS', provincia_id=208)
    ciudad.objects.create(Nombre='SAMBORONDON', provincia_id=208)
    ciudad.objects.create(Nombre='SANTA ELENA', provincia_id=208)
    ciudad.objects.create(Nombre='SANTA LUCIA', provincia_id=208)
    ciudad.objects.create(Nombre='SALITRE', provincia_id=208)
    ciudad.objects.create(Nombre='SAN JACINTO DE YAGUACHI', provincia_id=208)
    ciudad.objects.create(Nombre='PLAYAS', provincia_id=208)
    ciudad.objects.create(Nombre='SIMON BOLIVAR', provincia_id=208)
    ciudad.objects.create(Nombre='CORONEL MARCELINO MARIDUEÑA', provincia_id=208)
    ciudad.objects.create(Nombre='LOMAS DE SARGENTILLO', provincia_id=208)
    ciudad.objects.create(Nombre='NOBOL', provincia_id=208)
    ciudad.objects.create(Nombre='LA LIBERTAD', provincia_id=208)
    ciudad.objects.create(Nombre='GENERAL ANTONIO ELIZALDE', provincia_id=208)
    ciudad.objects.create(Nombre='ISIDRO AYORA', provincia_id=208)

    ciudad.objects.create(Nombre='IBARRA', provincia_id=209)
    ciudad.objects.create(Nombre='ANTONIO ANTE', provincia_id=209)
    ciudad.objects.create(Nombre='COTACACHI', provincia_id=209)
    ciudad.objects.create(Nombre='OTAVALO', provincia_id=209)
    ciudad.objects.create(Nombre='PIMAMPIRO', provincia_id=209)
    ciudad.objects.create(Nombre='SAN MIGUEL DE URCUQUI', provincia_id=209)

    ciudad.objects.create(Nombre='LOJA', provincia_id=210)
    ciudad.objects.create(Nombre='CALVAS', provincia_id=210)
    ciudad.objects.create(Nombre='CATAMAYO', provincia_id=210)
    ciudad.objects.create(Nombre='CELICA', provincia_id=210)
    ciudad.objects.create(Nombre='CHAGUARPAMBA', provincia_id=210)
    ciudad.objects.create(Nombre='ESPINDOLA', provincia_id=210)
    ciudad.objects.create(Nombre='GONZANAMA', provincia_id=210)
    ciudad.objects.create(Nombre='MACARA', provincia_id=210)
    ciudad.objects.create(Nombre='PALTAS', provincia_id=210)
    ciudad.objects.create(Nombre='PUYANGO', provincia_id=210)
    ciudad.objects.create(Nombre='SARAGURO', provincia_id=210)
    ciudad.objects.create(Nombre='SOZORANGA', provincia_id=210)
    ciudad.objects.create(Nombre='ZAPOTILLO', provincia_id=210)
    ciudad.objects.create(Nombre='PINDAL', provincia_id=210)
    ciudad.objects.create(Nombre='QUILANGA', provincia_id=210)
    ciudad.objects.create(Nombre='OLMEDO', provincia_id=210)

    ciudad.objects.create(Nombre='BABAHOYO', provincia_id=211)
    ciudad.objects.create(Nombre='BABA', provincia_id=211)
    ciudad.objects.create(Nombre='MONTALVO', provincia_id=211)
    ciudad.objects.create(Nombre='PUEBLOVIEJO', provincia_id=211)
    ciudad.objects.create(Nombre='QUEVEDO', provincia_id=211)
    ciudad.objects.create(Nombre='VENTANAS', provincia_id=211)
    ciudad.objects.create(Nombre='VINCES', provincia_id=211)
    ciudad.objects.create(Nombre='PALENQUE', provincia_id=211)
    ciudad.objects.create(Nombre='BUENA FE', provincia_id=211)
    ciudad.objects.create(Nombre='VALENCIA', provincia_id=211)
    ciudad.objects.create(Nombre='MOCACHE', provincia_id=211)

    ciudad.objects.create(Nombre='PORTOVIEJO', provincia_id=212)
    ciudad.objects.create(Nombre='BOLIVAR', provincia_id=212)
    ciudad.objects.create(Nombre='CHONE', provincia_id=212)
    ciudad.objects.create(Nombre='EL CARMEN', provincia_id=212)
    ciudad.objects.create(Nombre='FLAVIO ALFARO', provincia_id=212)
    ciudad.objects.create(Nombre='JIPIJAPA', provincia_id=212)
    ciudad.objects.create(Nombre='JUNIN', provincia_id=212)
    ciudad.objects.create(Nombre='MANTA', provincia_id=212)
    ciudad.objects.create(Nombre='MONTECRISTI', provincia_id=212)
    ciudad.objects.create(Nombre='PAJAN', provincia_id=212)
    ciudad.objects.create(Nombre='PICHINCHA', provincia_id=212)
    ciudad.objects.create(Nombre='ROCAFUERTE', provincia_id=212)
    ciudad.objects.create(Nombre='SANTA ANA', provincia_id=212)
    ciudad.objects.create(Nombre='SUCRE', provincia_id=212)
    ciudad.objects.create(Nombre='TOSAGUA', provincia_id=212)
    ciudad.objects.create(Nombre='24 DE MAYO', provincia_id=212)
    ciudad.objects.create(Nombre='PEDERNALES', provincia_id=212)
    ciudad.objects.create(Nombre='OLMEDO', provincia_id=212)
    ciudad.objects.create(Nombre='PUERTO LOPEZ', provincia_id=212)
    ciudad.objects.create(Nombre='JAMA', provincia_id=212)
    ciudad.objects.create(Nombre='JARAMIJO', provincia_id=212)
    ciudad.objects.create(Nombre='SAN VICENTE', provincia_id=212)

    ciudad.objects.create(Nombre='MORONA', provincia_id=211)
    ciudad.objects.create(Nombre='GUALAQUIZA', provincia_id=211)
    ciudad.objects.create(Nombre='LIMON INDANZA', provincia_id=211)
    ciudad.objects.create(Nombre='PALORA', provincia_id=211)
    ciudad.objects.create(Nombre='SANTIAGO', provincia_id=211)
    ciudad.objects.create(Nombre='SUCUA', provincia_id=211)
    ciudad.objects.create(Nombre='HUAMBOYA', provincia_id=211)
    ciudad.objects.create(Nombre='SAN JUAN BOSCO', provincia_id=211)
    ciudad.objects.create(Nombre='TAISHA', provincia_id=211)
    ciudad.objects.create(Nombre='LOGROÑO', provincia_id=211)
    ciudad.objects.create(Nombre='PABLO SEXTO', provincia_id=211)
    ciudad.objects.create(Nombre='TIWINTZA', provincia_id=211)

    ciudad.objects.create(Nombre='TENA', provincia_id=212)
    ciudad.objects.create(Nombre='AGUARICO', provincia_id=212)
    ciudad.objects.create(Nombre='ARCHIDONA', provincia_id=212)
    ciudad.objects.create(Nombre='EL CHACO', provincia_id=212)
    ciudad.objects.create(Nombre='LA JOYA DE LOS SACHAS', provincia_id=212)
    ciudad.objects.create(Nombre='ORELLANA', provincia_id=212)
    ciudad.objects.create(Nombre='QUIJOS', provincia_id=212)
    ciudad.objects.create(Nombre='CLORETO', provincia_id=212)
    ciudad.objects.create(Nombre='CARLOS JULIO AROSEMENA TOLA', provincia_id=212)

    ciudad.objects.create(Nombre='PASTAZA', provincia_id=213)
    ciudad.objects.create(Nombre='MERA', provincia_id=213)
    ciudad.objects.create(Nombre='SANTA CLARA', provincia_id=213)
    ciudad.objects.create(Nombre='ARAJUNO', provincia_id=213)

    ciudad.objects.create(Nombre='QUITO', provincia_id=214)
    ciudad.objects.create(Nombre='CAYAMBE', provincia_id=214)
    ciudad.objects.create(Nombre='MEJIA', provincia_id=214)
    ciudad.objects.create(Nombre='PEDRO MONCAYO', provincia_id=214)
    ciudad.objects.create(Nombre='RUMIÑAHUI', provincia_id=214)
    ciudad.objects.create(Nombre='SANTO DOMINGO', provincia_id=214)
    ciudad.objects.create(Nombre='SAN MIGUEL DE LOS BANCOS', provincia_id=214)
    ciudad.objects.create(Nombre='PEDRO VICENTE MALDONADO', provincia_id=214)
    ciudad.objects.create(Nombre='PUERTO QUITO', provincia_id=214)

    ciudad.objects.create(Nombre='AMBATO', provincia_id=215)
    ciudad.objects.create(Nombre='BAÑOS DE AGUA SANTA', provincia_id=215)
    ciudad.objects.create(Nombre='CEVALLOS', provincia_id=215)
    ciudad.objects.create(Nombre='MOCHA', provincia_id=215)
    ciudad.objects.create(Nombre='PATATE', provincia_id=215)
    ciudad.objects.create(Nombre='QUERO', provincia_id=215)
    ciudad.objects.create(Nombre='SAN PEDRO DE PELILEO', provincia_id=215)
    ciudad.objects.create(Nombre='SANTIAGO DE PILLARO', provincia_id=215)
    ciudad.objects.create(Nombre='TISALEO', provincia_id=215)

    ciudad.objects.create(Nombre='ZAMORA', provincia_id=216)
    ciudad.objects.create(Nombre='CHINCHIPE', provincia_id=216)
    ciudad.objects.create(Nombre='NANGARITZA', provincia_id=216)
    ciudad.objects.create(Nombre='YACUAMBI', provincia_id=216)
    ciudad.objects.create(Nombre='YANTZAZA (YANZATZA)', provincia_id=216)
    ciudad.objects.create(Nombre='EL PANGUI', provincia_id=216)
    ciudad.objects.create(Nombre='CENTINELA DEL CONDOR', provincia_id=216)
    ciudad.objects.create(Nombre='PALANDA', provincia_id=216)
    ciudad.objects.create(Nombre='PAQUISHA', provincia_id=216)

    ciudad.objects.create(Nombre='SAN CRISTOBAL', provincia_id=217)
    ciudad.objects.create(Nombre='ISABELA', provincia_id=217)
    ciudad.objects.create(Nombre='SANTA CRUZ', provincia_id=217)

    ciudad.objects.create(Nombre='LAGO AGRIO', provincia_id=218)
    ciudad.objects.create(Nombre='GONZALO PIZARRO', provincia_id=218)
    ciudad.objects.create(Nombre='PUTUMAYO', provincia_id=218)
    ciudad.objects.create(Nombre='SHUSHUFINDI', provincia_id=218)
    ciudad.objects.create(Nombre='SUCUMBIOS', provincia_id=218)
    ciudad.objects.create(Nombre='CASCALES', provincia_id=218)
    ciudad.objects.create(Nombre='CUYABENO', provincia_id=218)

    ciudad.objects.create(Nombre='ORELLANA', provincia_id=219)
    ciudad.objects.create(Nombre='AGUARICO', provincia_id=219)
    ciudad.objects.create(Nombre='LA JOYA DE LOS SACHAS', provincia_id=219)
    ciudad.objects.create(Nombre='LORETO', provincia_id=219)

    return HttpResponseRedirect('/index/')
    
"""
