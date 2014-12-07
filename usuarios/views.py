# coding=utf-8
from dajax.core import Dajax
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django_ajax.decorators import ajax
from ControlSystem.pComm.conexion import manejadorDeConexion
from ControlSystem.settings import BASE_DIR
from usuarios.models import SignUpForm, LogIn, usuarioSico

# Create your views here.

def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            #usuario_sico = form.cleaned_data["usuario_sico"]
            #contrasenia_sico = form.cleaned_data["contrasenia_sico"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            #user.usuario_sico = usuario_sico
            #user.contrasenia_sico = contrasenia_sico

            # Save new user attributes
            user.save()

            return HttpResponseRedirect(reverse('main'))  # Redirect after POST
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('signup.html', data, context_instance=RequestContext(request))


def main(request):
    #return render_to_response('main.html', {}, context_instance=RequestContext(request))
    return ingreso(request)


@login_required()
def salir(request):
    cerrarSico(request.user.sesion_sico)
    request.user.sesion_sico = ''
    request.user.save()
    logout(request)
    return HttpResponseRedirect('/login')

def cerrarSico(sesionAct):
    c = manejadorDeConexion()
    c.closeProgram(sesionAct)


def ingreso(request):
    error = None
    try:
        if request.user.sesion_sico:
            return home(request)
        else:
            salir(request)
    except:
        pass
    if request.POST:
        form = LogIn(request.POST)
        if form.is_valid():
            username = form.cleaned_data["usuario"]
            password = form.cleaned_data["clave"]
            contrato = form.cleaned_data["sico"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    if user.sesion_sico:
                        error = "El Usuario especificado ya esta en uso."
                        try:
                            logout(request)
                        except:
                            pass
                    else:
                        try:
                            u = usuarioSico.objects.get(user=user, contrato=contrato)
                        except:
                            u = False
                        if isinstance(u, usuarioSico):
                            #if integracion(u.nombre, u.clave, user):
                            login(request, user)
                            request.session['contrato'] = contrato
                            return HttpResponseRedirect('/home')
                            #else:
                            #   error = 'El Sistema Comercial(Sico Cnel) no esta disponible por el momento...'
                            #    user.sesion_sico=''
                            #    user.save()
                        else:
                            error = 'El Usuario Especificado no cuenta con permisos necesarios para acceder al contarto'
            elif username and password:
                error = "Su Usuario o Contraseña no son correctos, Intentelo nuevamente."

    form = LogIn()

    return render_to_response('usuarios/login.html', {'f': form, 'errors': error}, context_instance=RequestContext(request))


@login_required()
def home(request):
    print 'Sesion : %s' % request.user.sesion_sico
    #if request.user.sesion_sico:
    return render_to_response('usuarios/home.html', {}, context_instance=RequestContext(request))
    #return HttpResponseRedirect('/login')

def integracion(u, c, user):
    conn=None
    while True:
        conn = manejadorDeConexion()
        user.sesion_sico = str(conn.getAvailableConnection())
        if not User.objects.filter(sesion_sico=user.sesion_sico):
            user.save()
            break

    return conn.openSession(connectionName=user.sesion_sico, usuario=u, contrasenia=c)


@ajax
def multiply(request):
    a = int(request.POST['a'])
    b = int(request.POST['b'])
    c = a * b
    dajax = Dajax()
    dajax.assign('#result', 'value', str(c))
    return dajax.calls