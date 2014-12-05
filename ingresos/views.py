# coding=utf-8
import decimal
from dajax.core import Dajax
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_ajax.decorators import ajax
from busquedas.models import BusquedaForm, vitacoraBusquedas, MedidorBuscado
from ingresos.forms import ingresoForm
from ControlSystem.pComm.busquedas.scriptsBusquedas import buscar as b
from ingresos.models import *
from inventario.models import medidor


@login_required()
def ingresarSico(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = ingresoForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/ingresarsico/') # Redirect after POST
    else:
        form = ingresoForm(contrato=request.session['contrato'])
        #form = ingresoForm()
    data = {
        'form': form
    }

    return render_to_response('ingresos/ingresarSico.html', data, context_instance=RequestContext(request))


@login_required()
def ingreso(request, pk):
    act = actividad.objects.get(id=int(pk))

    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = ingresoForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/ingresarsico/') # Redirect after POST
    else:
        form = ingresoForm(contrato=request.session['contrato'], actividad=act)
        #form = ingresoForm()
    data = {
        'form': form
    }

    return render_to_response('ingresos/ingresarSico.html', data, context_instance=RequestContext(request))

@ajax()
def buscarCliente(request):
    if request.method == 'POST':
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
                    dajax.assign('#id_codigoDeCliente', 'value', '' + str(data['formCliente'].instance.cuenta) + '')
                    dajax.assign('#id_nombreDeCliente', 'value', '' + str(data['formCliente'].instance.nombre) + '')
                    dajax.assign('#id_cedula', 'value', '' + str(data['formCliente'].instance.ci_ruc) + '')
                    dajax.assign('#id_estadoCli', 'value', '' + str(data['formCliente'].instance.estado) + '')
                    dajax.assign('#id_lugar', 'value', '' + str(data['formCliente'].fields['parroquia'].initial) + '')
                    dajax.assign('#id_calle', 'value', '' + str(data['formCliente'].fields['direccion'].initial) + '')
                    dajax.assign('#id_geocodigo', 'value', '' + str(data['formCliente'].fields['geo'].initial) + '')
                    dajax.assign('#id_fabricaRev', 'value', '' + str(data['cMedidores'][0].instance.fabrica) + '')
                    dajax.script("$('#id_serieRev').val('" + str(data['cMedidores'][0].instance.serie) + "').change();")
                    dajax.assign('#id_marcaRev', 'value', '' + str(data['cMedidores'][0].fields['marc'].initial) + '')
                    dajax.assign('#id_lecturaRev', 'value', '' + str(data['cMedidores'][0].instance.lectura) + '')
                    request.session['cliente'] = data['formCliente'].instance
                    request.session['medidor'] = data['cMedidores'][0]
                else:
                    dajax = mostraError(dajax, {'Cliente': 'No Encontrato'}, '#err')

            else:
                print form.errors
                dajax = mostraError(dajax, {'': dict(form.errors)['__all__']}, '#err')

        except:
            dajax = mostraError(dajax, {'Error': 'No se pudo Buscar Cliente...'}, '#err')

        dajax.add_css_class('#cargando', 'hidden')
        return dajax.calls
    else:
        return None


@ajax()
def buscarReferencia(request):
    if request.method == 'POST':
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
                request.session['clienteRef'] = data['formCliente'].instance
                request.session['medidorRef'] = data['cMedidores'][0]
                #data = MedidorBuscado('marca','tecnologia', 'tension', 'amp', 'fi', 'fd', 'li', 'ld',
                #instance=medidor.objects.first())
                if data is not None:
                    dajax.assign('#id_cuentaAnteriror', 'value', '' + str(data['formCliente'].instance.cuenta) + '')
                    dajax.script("$('#id_serieAnteriror').val('" + str(data['cMedidores'][0].instance.serie) + "');")
                    dajax.assign('#id_marcaAnteriror', 'value',
                                 '' + str(data['cMedidores'][0].fields['marc'].initial) + '')

                else:
                    dajax = mostraError(dajax, {'Referencia': 'No Encontrada'}, '#errRef')

            else:
                print form.errors
                dajax = mostraError(dajax, {'': dict(form.errors)['__all__']}, '#errRef')

        except:
            dajax = mostraError(dajax, {'Error': 'No se pudo Buscar'}, '#errRef')

        dajax.add_css_class('#cargandoRef', 'hidden')

        return dajax.calls
    else:
        return None


@ajax()
def buscarMedidor(request):
    if request.method == 'POST':
        idMedidor = request.POST['medidor']
        print idMedidor
        dajax = Dajax()
        try:
            med = medidor.objects.get(id=int(idMedidor))
            dajax.assign('#id_fabricaInst', 'value', '' + str(med.fabrica) + '')
            dajax.assign('#id_marcaInst', 'value', '' + str(med.marca) + '')
            dajax.script("$('#id_serieInst').val('" + str(med.serie) + "').change();")
            dajax.assign('#id_tipoDeMedidor', 'value', '' + str(med.tipo) + '')
            dajax.assign('#id_lecturaInst', 'value', '' + str(med.lectura) + '')
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


@ajax()
def guardarIngreso(request):
    if request.method == 'POST':

        print request.POST

        dajax = Dajax()
        dajax.script("$('#cargandoForm').addClass('hidden');")
        form = ingresoForm(data=QueryDict(request.POST.urlencode(), mutable=True))

        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            ts = form.data['tipoDeSolicitud']
            #if ts == '11' or ts == '13':
            #en caso de ser un nuevo guardado...

            med = medidor()
            cli = cliente()

            if form.data['id'] != '0':
                act=actividad.objects.get(id=int(form.data['id']))
                cli=act.cliente
                print 'Se obtuvo el id del cliente nuevo a actualizar'
                try:
                    med = medidor.objects.get(actividad=act, contrato=None)
                    med.lectura=str(form.data['lecturaRev'])
                except: pass

            if len(form.data['cedula']) == 13:
                t = 'J'
                print u'Es persona jurídica'
            else:
                t = 'N'
                print u'Es persona natural'
            cli.ci_ruc=form.data['cedula']
            cli.nombre=form.data['nombreDeCliente']
            cli.tipo=t
            cli.telefono=form.data['telefono']
            print 'se generó el cliente nuevo'

            try:
                if ts == '1':
                    cliref = request.session['clienteRef']
                    medref = request.session['medidorRef']
                    print 'es s/N (1)'
                else:
                    cli = request.session['cliente']
                    cli.tipo=t
                    cli.telefono=form.data['telefono']
                    med = request.session['medidor']
                    med.instance.lectura=str(form.data['lecturaRev'])
                    print 'NO es s/N'

            except:
                try:
                    #en caso de ser actualizacion
                    cli=cliente.objects.get(
                        id=cli.id,
                        cuenta=(form.data['codigoDeCliente']).strip(),
                        ci_ruc=(form.data['cedula']).strip()
                    )
                    cli.tipo=t
                    cli.telefono=form.data['telefono']
                    print 'cliente a actualizar'
                    cli.save(force_update=True)

                    if ts != '1':
                        med.save(force_update=True)

                        enlace = detalleClienteMedidor.objects.get(
                            cliente=cli,
                            medidor=med
                        )
                        print enlace

                    elif med:
                        med.delete()

                        #actualizar
                        #form.save(request.session['contrato'], cliente=cli)
                        #return dajax.calls

                except:
                    dajax = mostraError(dajax, {'Error': 'Datos invalidos para guardar...'}, '#err')
                    return dajax.calls


            #guardar por primera vez
            cli.save()

            if ts == '1':
                cliref.save()
                medref.instance.save()
                fi = formatFechas(medref.fields['fi'].initial)
                fd = formatFechas(medref.fields['fd'].initial)
                d = detalleClienteMedidor(
                    cliente=cliref,
                    medidor=medref.instance,
                    lectura_instalacion=float(medref.fields['li'].initial),
                    lectura_desinstalacion=float(medref.fields['ld'].initial),
                    fecha_instalacion=fi,
                    fecha_desinstalacion=fd,
                )
                d.save()

                dcr = detalleClienteReferencia(
                    ubicacion=cliref.ubicacionGeografica,
                    cliente=cli,
                    referencia=cliref,
                    medidorDeReferencia=medref.instance.fabrica
                )
                dcr.save()
                if med.id:
                    med.delete()
            else:
                med.instance.save()

                fi = formatFechas(med.fields['fi'].initial)
                fd = formatFechas(med.fields['fd'].initial)

                d = detalleClienteMedidor(
                    cliente=cli,
                    medidor=med.instance,
                    lectura_instalacion=float(med.fields['li'].initial),
                    lectura_desinstalacion=float(med.fields['ld'].initial),
                    fecha_instalacion=fi,
                    fecha_desinstalacion=fd,
                )
                d.save()

            print 'Correcto...'

            form.save(request.session['contrato'], cliente=cli)
        else:
            print dict(form.errors)
            dajax = mostraError(dajax, form.errors, '#err')

        return dajax.calls
    else:
        return None


def formatFechas(f):
    f = str(f).split('/')
    try:
        f = "-".join(str(x) for x in f[::-1])
        return datetime.date(*map(int, f.split('-')))
    except:
        return None


def mostraError(dajax, e, ide):
    dajax.assign(
        ide,
        'innerHTML',
        render_to_response('ingresos/error.html', {'errors': e})
    )
    return dajax