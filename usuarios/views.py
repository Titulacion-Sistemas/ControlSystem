# coding=utf-8
from dajax.core import Dajax
import datetime
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import password_change, password_change_done
from django.contrib.humanize.tests import now
from django.db.models import Sum
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django_ajax.decorators import ajax
from ControlSystem.pComm.conexion import manejadorDeConexion
from ControlSystem.settings import BASE_DIR
from ingresos.models import cuadrilla, materialDeActividad, detalleDeActividad
from inventario.models import detalleMaterialContrato, medidor
from usuarios.excel import ExcelResponse
from usuarios.models import SignUpForm, LogIn, usuarioSico, posicion, MyUserChangeForm

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
                            #    error = 'El Sistema Comercial(Sico Cnel) no esta disponible por el momento...'
                            #    user.sesion_sico=''
                            #    user.save()
                        else:
                            error = 'El Usuario Especificado no cuenta con permisos necesarios para acceder al contarto'
            elif username and password:
                error = "Su Usuario o Contraseña no son correctos, Intentelo nuevamente."
    form = LogIn()
    return render_to_response('usuarios/login.html', {'f': form, 'errors': error},
                              context_instance=RequestContext(request))


@login_required()
def home(request):
    print 'Sesion : %s' % request.user.sesion_sico
    #if request.user.sesion_sico:
    return render_to_response('usuarios/home.html', {}, context_instance=RequestContext(request))
    #return HttpResponseRedirect('/login')


def integracion(u, c, user):
    conn = None
    while True:
        conn = manejadorDeConexion()
        user.sesion_sico = str(conn.getAvailableConnection())
        if not User.objects.filter(sesion_sico=user.sesion_sico):
            user.save()
            break

    return conn.openSession(connectionName=user.sesion_sico, usuario=u, contrasenia=c)


@login_required()
def perfil(request):
    u = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = MyUserChangeForm(request.POST)
        if form.is_valid():
            u.username = form.cleaned_data["username"]
            #u.password = form.cleaned_data["password"]
            u.email = form.cleaned_data["email"]
            u.first_name = form.cleaned_data["first_name"]
            u.last_name = form.cleaned_data["last_name"]
            u.direccion = form.cleaned_data["direccion"]
            u.telefono = form.cleaned_data["telefono"]
            u.celular = form.cleaned_data["celular"]
            u.save(force_update=True)
            request.user = u
            return render_to_response('usuarios/password_change_done.html', {}, context_instance=RequestContext(request))
    else:
        form = MyUserChangeForm(instance=u)

    data = {
        'form': form,
        'action':'/perfil',
    }
    return render_to_response('usuarios/perfil.html', data, context_instance=RequestContext(request))


@login_required()
def password(request):
    return password_change(request, template_name='usuarios/perfil.html', post_change_redirect='/change_done', extra_context={'action':'/password'})


def my_password_change_done(request):
    return password_change_done(request, template_name='usuarios/password_change_done.html', extra_context=request)

@login_required()
def cuadrillas(request):
    #pos = posicion.objects.filter(User__usuario_sico__contrato=request.session['contrato'], fechaHora__gt='2014-12-14 0:0')
    pos = posicion.objects.filter(
        actividad__detalledeactividad__rubro__contrato=request.session['contrato'],
        fechaHora__gte='%s-%s-%s 0:0' % (
            str(datetime.datetime.today().year),
            str(datetime.datetime.today().month),
            str(datetime.datetime.today().day)
        )
    ).order_by('-fechaHora')

    data = {
        'cuadrillas': pos
    }

    return render_to_response('cuadrillas/cuadrillas.html', data, context_instance=RequestContext(request))


@ajax
def masCuadrillas(request):
    if request.method == 'POST':
        print request.POST
        t = request.POST['fechaHora']
        dajax = Dajax()
        pos = posicion.objects.filter(
            usuario__usuario_sico__contrato=request.session['contrato'],
            fechaHora__gt=str(t)
        ).order_by('-fechaHora')

        data = {
            'cuadrillas': pos
        }
        agregar = render_to_response('cuadrillas/renderCuadrilla.html', data)
        #print agregar
        dajax.prepend('#listaCuadrillas', 'innerHTML', agregar)

        return dajax.calls

    else:
        return None


def reporteMateriales(request):
    objs = list(detalleMaterialContrato.objects.filter(contrato=request.session['contrato']))
    utili = materialDeActividad.objects.filter(material__contrato=request.session['contrato'])
    milista = []
    for i in range(len(objs)):
        try:
            u = utili.filter(material__id=objs[i].id).aggregate(Sum('cantidad'))
            cant = u['cantidad__sum']
            if cant is None:
                cant = 0
        except:
            cant = 0
        milista.append(
            {
                'Item': i + 1,
                'Material': objs[i].material.__unicode__(),
                'Inicial': objs[i].stock,
                'Utilizado': cant,
                'Restante': objs[i].stock - cant,
            }
        )

    return ExcelResponse(
        milista,
        output_name='Detalle de Material Utilizado', headers=['Item', 'Material', 'Inicial', 'Utilizado', 'Restante'],
       # rini=3, cini=2
    )


def reportes(request):
    return render_to_response('reportes/reportes.html', {}, context_instance=RequestContext(request))


def reporteActividades(request):
    objs=[]
    try:
        objs = detalleDeActividad.objects.filter(
            rubro__contrato=request.session['contrato']
        ).distinct('actividad').order_by('-activiada.fechaDeActividad')
    except:
        d=None

    materialesDeContrato = list(detalleMaterialContrato.objects.filter(contrato=request.session['contrato']))
    milista = []

    for i in range(len(objs)):

        rub = ['','','','','','','','','','','','','']
        clie = objs[i].actividad.cliente
        if objs[i].actividad.tipoDeSolicitud_id == 13:
            revisado = objs[i].actividad.cliente.detalleclientemedidor_set.last().medidor
            instalado = objs[i].actividad.medidor_set.exclude(contrato=None).last()


        elif objs[i].actividad.tipoDeSolicitud_id == 11:
            revisado = objs[i].actividad.cliente.detalleclientemedidor_set.last().medidor
            instalado = medidor(fabrica='', serie='', voltaje='', marca=revisado.marca)

        if objs[i].actividad.tipoDeSolicitud_id == 1 and (not objs[i].actividad.cliente.geocodigo):
            revisado = medidor(fabrica='', serie='', voltaje='')
            instalado = objs[i].actividad.medidor_set.exclude(contrato=None).last()
            clie = objs[i].actividad.cliente.cliente.last().referencia

        sellos=''
        for sl in objs[i].actividad.sello_set.filter():
            if not sellos == '':
                sellos += ' - '
            sellos += str(sl.numero)


        for r in objs[i].actividad.detalledeactividad_set.filter():
            if r.rubro.servicio_id == 1 and r.rubro.rubro_id == 1:
                rub[0]='1'
            if r.rubro.servicio_id == 6 and r.rubro.rubro_id == 2:
                rub[1]='1'
            if r.rubro.servicio_id == 2 and r.rubro.rubro_id == 2:
                rub[2]='1'

            if r.rubro.servicio_id == 3 and r.rubro.rubro_id == 1:
                rub[4]='1'

            if r.rubro.servicio_id == 4:
                if r.rubro.rubro_id == 2:
                    rub[7]='1'
                if r.rubro.rubro_id == 3:
                    rub[8]='1'
                if r.rubro.rubro_id == 4:
                    rub[9]='SI'
                if r.rubro.rubro_id == 5:
                    rub[10]='1'

            if r.rubro.servicio_id == 5:
                if r.rubro.rubro_id == 6:
                    rub[11]='1'
                if r.rubro.rubro_id == 7:
                    rub[12]='1'
                if r.rubro.rubro_id == 8:
                    rub[11]='1'

        data = {
            'Item': i + 1,
            'Fecha': objs[i].actividad.fechaDeActividad,
            'Agencia': clie.ubicacionGeografica.parroquia.canton.descripcion,
            'Direccion': clie.ubicacionGeografica.calle.descripcion1,
            'Provincia': '%02d' % clie.ubicacionGeografica.parroquia.canton.provincia.id,
            'Canton': '%02d' % clie.ubicacionGeografica.parroquia.canton.num,
            'Sector': '%02d' % clie.geocodigo.ruta.sector.num,
            'Ruta': '%03d' % clie.geocodigo.ruta.num,
            'Secuencia': '%07d' % clie.geocodigo.num,
            'Cuenta': objs[i].actividad.cliente.cuenta,
            'Titular': objs[i].actividad.cliente.nombre,
            'RFabrica': revisado.fabrica,
            'RFSerie': revisado.serie,
            'RPlan': '',
            'RVoltaje': revisado.voltaje,
            'IFabrica': instalado.fabrica,
            'IFSerie': instalado.serie,
            'IPlan': '',
            'IVoltaje': instalado.voltaje,
            'Marca': instalado.marca.descripcion,
            'Sello': sellos,
            'ServicioNuevo': rub[0],
            'Directo': rub[1],
            'CambioDeMedidor ': rub[2],
            'ConCaja': rub[3],
            'Acometida': rub[4],
            'ConMedidor': rub[5],
            'MantenimientoMedidor': rub[6],
            'CambioDeCaja': rub[7],
            'SoloAcometida': rub[8],
            'Contrastacion': rub[9],
            'Revision': rub[10],
            'TramiteSico': rub[11],
            'TrammiteSig': rub[12],
        }



        for m in materialesDeContrato:
            existe = materialDeActividad.objects.filter(material=m, actividad=objs[i].actividad)
            if existe:
                data[''+str(m.material)]=str(existe.last().cantidad)
            else:
                data[''+str(m.material)]=''

        milista.append(data)


    encabezados = [
        'Item',
        'Fecha',
        'Agencia',
        'Direccion',
        'Provincia',
        'Canton',
        'Sector',
        'Ruta',
        'Secuencia',
        'Cuenta',
        'Titular',
        'RFabrica',
        'RFSerie',
        'RPlan',
        'RVoltaje',
        'IFabrica',
        'IFSerie',
        'IPlan',
        'IVoltaje',
        'Marca',
        'Sello',
        'ServicioNuevo',
        'Directo',
        'CambioDeMedidor ',
        'ConCaja',
        'Acometida',
        'ConMedidor',
        'MantenimientoMedidor',
        'CambioDeCaja',
        'SoloAcometida',
        'Contrastacion',
        'Revision',
        'TramiteSico',
        'TrammiteSig'
    ]

    for m in materialesDeContrato:
        encabezados.append(str(m.material))

    print milista

    return ExcelResponse(
        milista,
        output_name='Detalle de Actividades Realizadas', headers=encabezados,
        rini=7, cini=0
    )

def acercade(request):
    return render_to_response('usuarios/acercade.html', {}, context_instance=RequestContext(request))


@ajax
def multiply(request):
    a = int(request.POST['a'])
    b = int(request.POST['b'])
    c = a * b
    dajax = Dajax()
    dajax.assign('#result', 'value', str(c))
    return dajax.calls