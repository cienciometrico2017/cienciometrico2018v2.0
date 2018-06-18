from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from apps.Investigador.models import Investigador
from apps.Investigador.form import cambioForm, PasswordForm, document
from apps.roles.models import Rol
from django.contrib.auth.models import User
from apps.Formacion_Academica.models import formacion_academica
from apps.Formacion_Academica.form import FormacionAform
# Create your views here.
def inicio(request):
    usuario = request.user.id
    perfil = Investigador.objects.get(user_id=usuario)
    form_Academico = FormacionAform
    try:
        Formacion = formacion_academica.objects.filter(user_id=usuario)
    except formacion_academica.DoesNotExist:
        Formacion = None
    usuario1 = User.objects.get(id = usuario)
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
    if request.method == 'GET':
        form = cambioForm(instance=perfil)
        form_second = PasswordForm(instance=usuario1)
        form_four = document(instance=perfil)
        #print("No Llegue :(")
    else:
        form = cambioForm(request.POST, instance=perfil)
        form_second = PasswordForm(request.POST, instance=usuario1)
        form_third = FormacionAform(request.POST, request.FILES)
        form_four = document(request.POST, request.FILES, instance=perfil)
        if 'val' in request.POST:
            variable = request.POST['val']

            if int(variable) == 2:
                if form_third.is_valid():
                    form_third.save()
                    messages.success(request, ('Se ha guardado la del título información correctamente'))
                    return redirect('inicio:logeo')
            if int(variable) == 1:
                if form_four.is_valid():
                    form_four.save()
                    messages.success(request, ('Se ha guardado la información del documento correctamente'))
                    return redirect('inicio:logeo')

        if 'password' in request.POST and 'password1' in request.POST:
            password1 = request.POST['password']
            password2 = request.POST['password1']
            if form.is_valid() and form_second.is_valid() and password1 == password2:
                perfil = form.save()
                perfil.user = form_second.save()
                perfil.user.set_password(perfil.user.password)
                perfil.save()
                form_second.save()
            else:
                messages.error(request, ('Las contraseñas no coinciden, vuelva a intentarlo'))
                return render(request, 'usuario/newPass.html', {'form': form, 'form2': form_second})

        return redirect('inicio:logeo')
    if not perfil.cambio:
        return render(request, 'usuario/newPass.html', {'form': form, 'form2': form_second})
    else:
        return render(request, 'base1/inicio.html', {'usuario': privilegio, 'perfil': perfil, 'Formacion':Formacion, 'formAca': form_Academico, 'formDoc':form_four})



