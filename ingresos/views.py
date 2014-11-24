from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from ingresos.forms import cambioDeMaterialForm


def cambioDeMaterial(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = cambioDeMaterialForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/ingresarcambiomaterial/') # Redirect after POST
    else:
        form = cambioDeMaterialForm() # An unbound form

    data={
        'form': form
    }

    return render_to_response('ingresos/cambioDeMaterial.html', data, context_instance=RequestContext(request))


def cambioDeMedidor(request):
    return render_to_response('ingresos/cambioDeMedidor.html', {}, context_instance=RequestContext(request))


def servicioNuevo(request):
    return render_to_response('ingresos/servicioNuevo.html', {}, context_instance=RequestContext(request))