from dajax.core import Dajax
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_ajax.decorators import ajax
from busquedas.models import BusquedaForm
from ControlSystem.pComm.busquedas.scriptsBusquedas import buscar as b

# Create your views here.
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
    form = BusquedaForm(initial={'usuario': request.user, 'estadoRetorno': True, })

    data = {
        'form': form,
        'tipo': tipo,
        'nav': 'buscar'
    }
    return render_to_response('busqueda/buscar.html', data, context_instance=RequestContext(request))


def comprobarFormBusqueda(form, sesionAct):
    dajax = Dajax()
    dajax.clear('#listaResultados', 'innerHTML')
    dajax.script("$('#cargando').hide();")
    if form.is_valid():
        tipo = str(form.cleaned_data["tipoBusq"])
        dato = str(form.cleaned_data["consulta"])
        #pythoncom.CoInitialize()
        buscando = b(sesionAct)
        dajax.script("$('#listaResultados').show();")
        dajax.script("$('#resultado').show();")
        dajax.append('#listaResultados', 'innerHTML', buscando.renderBusqueda(tipo, dato))
        dajax.script("$('#resultado').html($('#r').html());")
        dajax.script("$('#r').empty();")
        form.save()
    else:
        print form.errors

        try:
            dajax.append(
                '#err',
                'innerHTML',
                render_to_response('busqueda/error.html', {'errors': dict(form.errors)['__all__']})
            )
        except:
            dajax.append(
                '#err',
                'innerHTML',
                render_to_response('busqueda/error.html', {'errors': dict(form.errors)['consulta']})
            )
    return dajax.calls


@ajax()
def busqueda(request):
    if request.method == 'POST':
        print request.POST
        form = BusquedaForm(request.POST)
        return comprobarFormBusqueda(form, request.user.sesion_sico)
    else:
        cuenta(request)