from dajax.core import Dajax
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django_ajax.decorators import ajax
from busqueda.models import BusquedaForm, VitacoraBusquedas

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

        Vitacora.usuario = User.objects.get(id = u)
    #
    #     #Vitacora.estadoRetorno = BusquedaEnSico(tipoBusq, consulta)
    #
        Vitacora.save()

        form = BusquedaForm()
        data = {
            'formulario': form,
        }

        dajax.append('#listaResultados', 'innerHTML', render_to_response('busqueda/form.html', data))
        return dajax.calls

    else:

        print "NO es post"
