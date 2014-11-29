from dajax.core import Dajax
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_ajax.decorators import ajax
from busquedas.models import BusquedaForm, vitacoraBusquedas, MedidorBuscado
from ingresos.forms import cambioDeMaterialForm
from ControlSystem.pComm.busquedas.scriptsBusquedas import buscar as b
from inventario.models import medidor


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

@ajax()
def buscarCliente(request):
    tipo = request.POST['tipo']
    dato = request.POST['dato']
    print tipo
    print dato
    print request.user

    dajax = Dajax()
    try:
        #validando ando
        usuario = request.user
        #usuario = User.objects.first()

        bucqModel = vitacoraBusquedas(tipoBusq=tipo, consulta=dato, usuario=usuario, estadoRetorno=True)
        form = BusquedaForm(
            {'usuario': usuario.id, 'estadoRetorno': True, 'tipoBusq': tipo, 'consulta': dato},
            instance=bucqModel
        )

        if form.is_valid():
            buscando = b(usuario.sesion_sico)
            data = buscando.busquedaDeTipo(tipo, dato, paraIngreso=True)
            #data = MedidorBuscado('marca','tecnologia', 'tension', 'amp', 'fi', 'fd', 'li', 'ld',
            #instance=medidor.objects.first())
            if data != None:
                dajax.assign('#id_codigoDeCliente', 'value', ''+str(data['formCliente'].instance.cuenta)+'')
                dajax.assign('#id_nombreDeCliente', 'value', ''+str(data['formCliente'].instance.nombre)+'')
                dajax.assign('#id_cedula', 'value', ''+str(data['formCliente'].instance.ci_ruc)+'')
                dajax.assign('#id_lugar', 'value', ''+str(data['formCliente'].fields['parroquia'].initial)+'')
                dajax.assign('#id_calle', 'value', ''+str(data['formCliente'].fields['direccion'].initial)+'')
                dajax.assign('#id_geocodigo', 'value', ''+str(data['formCliente'].fields['geo'].initial)+'')
                dajax.assign('#id_fabricaRev', 'value', ''+str(data['cMedidores'][0].instance.fabrica)+'')
                dajax.assign('#id_serieRev', 'value', ''+str(data['cMedidores'][0].instance.serie)+'')
                dajax.assign('#id_marcaRev', 'value', ''+str(data['cMedidores'][0].fields['marc'].initial)+'')
                dajax.assign('#id_lecturaRev', 'value', ''+str(data['cMedidores'][0].instance.lectura)+'')
            else:
                dajax = mostraError(dajax, ['No Encontrato'])

        else:
            print form.errors
            dajax = mostraError(dajax, dict(form.errors)['__all__'])

    except: dajax = mostraError(dajax, ['No Encontrato'])

    dajax.add_css_class('#cargando', 'hidden')

    return dajax.calls

def mostraError(dajax, e):
    dajax.append(
        '#err',
        'innerHTML',
        render_to_response('busqueda/error.html', {'errors': e})
    )
    return dajax