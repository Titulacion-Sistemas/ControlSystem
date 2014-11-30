from dajax.core import Dajax
from django.contrib.auth.decorators import login_required
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

@login_required()
def ingresarSico(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = cambioDeMaterialForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/ingresarsico/') # Redirect after POST
    else:
        form = cambioDeMaterialForm(contrato=request.session['contrato'])
        #form = cambioDeMaterialForm()
    data = {
        'form': form
    }

    return render_to_response('ingresos/ingresarSico.html', data, context_instance=RequestContext(request))

@ajax()
def buscarCliente(request):
    if request.POST:
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
                    dajax.script("$('#id_serieRev').val('"+str(data['cMedidores'][0].instance.serie)+"').change();")
                    dajax.assign('#id_marcaRev', 'value', ''+str(data['cMedidores'][0].fields['marc'].initial)+'')
                    dajax.assign('#id_lecturaRev', 'value', ''+str(data['cMedidores'][0].instance.lectura)+'')
                    request.session['cliente'] = data
                else:
                    dajax = mostraError(dajax, ['No Encontrato'], '#err')

            else:
                print form.errors
                dajax = mostraError(dajax, dict(form.errors)['__all__'], '#err')

        except:
            dajax = mostraError(dajax, ['Error al Buscar...'], '#err')

        dajax.add_css_class('#cargando', 'hidden')

        return dajax.calls
    else:
        return None

@ajax()
def buscarReferencia(request):
    if request.POST:
        dato = request.POST['dato']
        print dato
        print request.user

        dajax = Dajax()
        try:
            #validando ando
            usuario = request.user
            #usuario = User.objects.first()

            bucqModel = vitacoraBusquedas(tipoBusq='2', consulta=dato, usuario=usuario, estadoRetorno=True)
            form = BusquedaForm(
                {'usuario': usuario.id, 'estadoRetorno': True, 'tipoBusq': '2', 'consulta': dato},
                instance=bucqModel
            )

            if form.is_valid():
                buscando = b(usuario.sesion_sico)
                data = buscando.busquedaDeTipo('2', dato, paraIngreso=True)
                #data = MedidorBuscado('marca','tecnologia', 'tension', 'amp', 'fi', 'fd', 'li', 'ld',
                #instance=medidor.objects.first())
                if data != None:
                    dajax.assign('#id_cuentaAnteriror', 'value', ''+str(data['formCliente'].instance.cuenta)+'')
                    dajax.script("$('#id_serieAnteriror').val('"+str(data['cMedidores'][0].instance.serie)+"');")
                    dajax.assign('#id_marcaAnteriror', 'value', ''+str(data['cMedidores'][0].fields['marc'].initial)+'')
                    request.session['referencia'] = data
                else:
                    dajax = mostraError(dajax, ['No Encontrato'], '#errRef')

            else:
                print form.errors
                dajax = mostraError(dajax, dict(form.errors)['__all__'], '#errRef')

        except:
            dajax = mostraError(dajax, ['Error al Buscar'], '#errRef')

        dajax.add_css_class('#cargando', 'hidden')

        return dajax.calls
    else:
        return None




@ajax()
def buscarMedidor(request):
    if request.POST:
        idMedidor = request.POST['medidor']
        print idMedidor
        dajax = Dajax()
        try:
            med = medidor.objects.get(id=int(idMedidor))
            dajax.assign('#id_fabricaInst', 'value', ''+str(med.fabrica)+'')
            dajax.assign('#id_marcaInst', 'value', ''+str(med.marca)+'')
            dajax.script("$('#id_serieInst').val('"+str(med.serie)+"').change();")
            dajax.assign('#id_tipoDeMedidor', 'value', ''+str(med.tipo)+'')
            dajax.assign('#id_lecturaInst', 'value', ''+str(med.lectura)+'')
            dajax.script("$('#id_serieInst').change();")
        except:
            dajax.assign('#id_fabricaInst', 'value', '')
            dajax.assign('#id_marcaInst', 'value', '')
            dajax.assign('#id_serieInst', 'value', '')
            dajax.assign('#id_tipoDeMedidor', 'value', '')
            dajax.assign('#id_lecturaInst', 'value', '')
        return dajax.calls

    else:
        return None

def mostraError(dajax, e, id):
    dajax.append(
        id,
        'innerHTML',
        render_to_response('busqueda/error.html', {'errors': e})
    )
    return dajax