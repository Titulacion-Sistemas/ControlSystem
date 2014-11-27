from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from ingresos.forms import cambioDeMaterialForm


def ingresarSico(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = cambioDeMaterialForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/ingresarcambiomaterial/') # Redirect after POST
    else:
        #form = cambioDeMaterialForm(request.session['contrato'])
        form = cambioDeMaterialForm()
    data={
        'form': form
    }

    return render_to_response('ingresos/ingresarSico.html', data, context_instance=RequestContext(request))

