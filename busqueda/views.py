from dajax.core import Dajax
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django_ajax.decorators import ajax
from busqueda.models import BusquedaForm, VitacoraBusquedas


@login_required()
def buscar(request):

    form = BusquedaForm()

    data = {
        'form': form,
    }
    return render_to_response('busqueda/buscar.html', data, context_instance=RequestContext(request))

@ajax
def busqueda(request):
    dajax = Dajax()
    if request.method == 'POST':

        tipo = int(request.POST['tipo'])
        dato = str(request.POST['dato'])
        u = int(request.POST['u'])


        Vitacora = VitacoraBusquedas(consulta=dato, tipoBusq=tipo)

        Vitacora.usuario = User.objects.get(id = u)
    #
    #     #Vitacora.estadoRetorno = BusquedaEnSico(tipoBusq, consulta)
    #
        Vitacora.save()

        dajax.append('#result', 'innerHTML', 'ok')
        return dajax.calls

    else:

        print "NO es post"
