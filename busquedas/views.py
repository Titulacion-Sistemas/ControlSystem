from dajax.core import Dajax
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext
from django_ajax.decorators import ajax
import pythoncom
from busquedas.models import BusquedaForm, VitacoraBusquedas
from ControlSystem.pComm.scripts import buscar as b


@login_required()
def cuenta(request):
    return buscar(request, 1)

@login_required()
def medidor(request):
    return buscar(request, 2)

@login_required()
def nombre(request):
    return buscar(request, 3)

@login_required()
def geocodigo(request):
    return buscar(request, 4)

def buscar(request, tipo):

    form = BusquedaForm()

    data = {
        'form': form,
        'tipo': tipo,
        'nav': 'buscar'
    }
    return render_to_response('busqueda/buscar.html', data, context_instance=RequestContext(request))

@ajax()
def busqueda(request):
    dajax = Dajax()
    if request.method == 'POST':

        tipo = int(request.POST['tipo'])
        dato = str(request.POST['dato'])
        print tipo
        print dato
        u = int(request.POST['u'])


        Vitacora = VitacoraBusquedas(consulta=dato, tipoBusq=tipo)

        usuario = User.objects.get(id = u)

        Vitacora.usuario = usuario
        Vitacora.save()

        pythoncom.CoInitialize()
        print usuario.sesion_sico
        if tipo == 1:
            buscando = b()
            dajax.clear('#listaResultados', 'innerHTML')
            dajax.script("$('#cargando').hide();")
            dajax.append('#listaResultados', 'innerHTML', buscando.porCuenta(usuario.sesion_sico, dato))
        return dajax.calls

    else:

        print "NO es post"
