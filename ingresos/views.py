from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def cambioDeMaterial(request):
    return render_to_response('ingresos/cambioDeMaterial.html', {}, context_instance=RequestContext(request))


def cambioDeMedidor(request):
    return render_to_response('ingresos/cambioDeMedidor.html', {}, context_instance=RequestContext(request))


def servicioNuevo(request):
    return render_to_response('ingresos/servicioNuevo.html', {}, context_instance=RequestContext(request))