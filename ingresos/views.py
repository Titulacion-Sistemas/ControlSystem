# coding=utf-8

import datetime

from dajax.core import Dajax
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_ajax.decorators import ajax
from django.views.generic.base import TemplateView

from ControlSystem.pComm.cambiosDeMateriales.scriptCambiosDeMateriales import ingresarCambioDeMaterial
from ControlSystem.pComm.cambiosDeMedidor.scriptCambiosDeMedidor import ingresarCambioDeMedidor
from ControlSystem.pComm.serviciosNuevos.scriptServiciosNuevos import ingresarServicioNuevo
from busquedas.models import BusquedaForm, vitacoraBusquedas
from ingresos.forms import ingresoForm, BuscarActividad, FotoForm
from ControlSystem.pComm.busquedas.scriptsBusquedas import buscar as b
from ingresos.models import *
from inventario.models import medidor, sello


class ListaDeFotos(TemplateView):
    template_name = 'fotos/listaDeFotos.html'

    def get(self, request, *args, **kwargs):
        try:
            d = detalleDeActividad.objects.filter(
                rubro__contrato=request.session['contrato']
            ).distinct('actividad').order_by('-activiada.fechaDeActividad')
        except:
            return HttpResponseRedirect('/logout')
        entrada = []
        for act in d:
            entrada.append(act.actividad)

        ba = BuscarActividad()
        print request.GET
        try:

            criterio = request.GET.get('criterio')
            if criterio == '1':
                d = detalleDeActividad.objects.filter(
                    rubro__contrato=request.session['contrato'],
                    actividad__cliente__cuenta__contains=request.GET.get('dato')
                ).distinct('actividad').order_by('-activiada.fechaDeActividad')
                entrada = []
                for act in d:
                    entrada.append(act.actividad)
                ba = BuscarActividad(data=request.GET)
            elif criterio == '2':
                m = medidor.objects.filter(
                    fabrica__contains=request.GET.get('dato')
                ).distinct('actividad').order_by('-activiada.fechaDeActividad')
                entradatmp = []
                for act in m:
                    if act.actividad in entrada:
                        entradatmp.append(act.actividad)
                entrada = entradatmp
                ba = BuscarActividad(data=request.GET)
            elif criterio == '3':
                sp = str(request.GET.get('dato')).split(' ')
                if len(sp) > 1:
                    d = detalleDeActividad.objects.filter(
                        rubro__contrato=request.session['contrato'],
                        actividad__instalador__nombre__nombre__icontains=sp[0],
                        actividad__instalador__nombre__apellido__icontains=sp[1]
                    ).distinct('actividad').order_by('-activiada.fechaDeActividad')
                else:
                    d = detalleDeActividad.objects.filter(
                        rubro__contrato=request.session['contrato'],
                        actividad__instalador__nombre__nombre__icontains=str(request.GET.get('dato'))
                    ).distinct('actividad').order_by('-activiada.fechaDeActividad')
                entrada = []
                for act in d:
                    entrada.append(act.actividad)
                ba = BuscarActividad(data=request.GET)

        except:
            pass

        lines = []
        for i in entrada:
            lines.append(i)
        paginator = Paginator(lines, 50)
        page = request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        data = {
            'form': ba,
            'lines': show_lines
        }
        return render_to_response('fotos/listaDeFotos.html', data, context_instance=RequestContext(request))


class ListaDeIngreso(TemplateView):
    template_name = 'ingresos/listadeingreso.html'

    def get(self, request, *args, **kwargs):
        try:
            d = detalleDeActividad.objects.filter(
                rubro__contrato=request.session['contrato']
            ).distinct('actividad').order_by('-activiada.fechaDeActividad')
        except:
            return HttpResponseRedirect('/logout')
        entrada = []
        for act in d:
            entrada.append(act.actividad)
            #     .raw(
        #     "SELECT "
        #     "ingresos_actividad.* "
        #     "FROM "
        #     "ingresos_actividad, "
        #     "ingresos_detalledeactividad, "
        #     "inventario_detallerubro, "
        #     "inventario_contrato "
        #     "WHERE "
        #     "ingresos_actividad.id=ingresos_detalledeactividad.actividad_id and "
        #     "ingresos_detalledeactividad.rubro_id=inventario_detallerubro.id and "
        #     "inventario_detallerubro.contrato_id=inventario_contrato.num and "
        #     "inventario_contrato.num='%s' "
        #     "group by ingresos_actividad.id "
        #     "order by ingresos_actividad.\"fechaDeActividad\" desc;" % request.session['contrato'].num
        # )

        ba = BuscarActividad()
        print request.GET
        try:

            criterio = request.GET.get('criterio')
            if criterio == '1':
                d = detalleDeActividad.objects.filter(
                    rubro__contrato=request.session['contrato'],
                    actividad__cliente__cuenta__contains=request.GET.get('dato')
                ).distinct('actividad').order_by('-activiada.fechaDeActividad')
                entrada = []
                for act in d:
                    entrada.append(act.actividad)
                ba = BuscarActividad(data=request.GET)
            elif criterio == '2':
                m = medidor.objects.filter(
                    fabrica__contains=request.GET.get('dato')
                ).distinct('actividad').order_by('-activiada.fechaDeActividad')
                entradatmp = []
                for act in m:
                    if act.actividad in entrada:
                        entradatmp.append(act.actividad)
                entrada = entradatmp
                ba = BuscarActividad(data=request.GET)
            elif criterio == '3':
                sp = str(request.GET.get('dato')).split(' ')
                if len(sp) > 1:
                    d = detalleDeActividad.objects.filter(
                        rubro__contrato=request.session['contrato'],
                        actividad__instalador__nombre__nombre__icontains=sp[0],
                        actividad__instalador__nombre__apellido__icontains=sp[1]
                    ).distinct('actividad').order_by('-activiada.fechaDeActividad')
                else:
                    d = detalleDeActividad.objects.filter(
                        rubro__contrato=request.session['contrato'],
                        actividad__instalador__nombre__nombre__icontains=str(request.GET.get('dato'))
                    ).distinct('actividad').order_by('-activiada.fechaDeActividad')
                entrada = []
                for act in d:
                    entrada.append(act.actividad)
                ba = BuscarActividad(data=request.GET)

        except:
            pass

        lines = []
        for i in entrada:
            lines.append(i)
        paginator = Paginator(lines, 10)
        page = request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            show_lines = paginator.page(1)
        except EmptyPage:
            show_lines = paginator.page(paginator.num_pages)
        data = {
            'form': ba,
            'lines': show_lines
        }
        return render_to_response('ingresos/listadeingreso.html', data, context_instance=RequestContext(request))


@login_required()
def ingresarSico(request):
    form = ingresoForm(contrato=request.session['contrato'])

    data = {
        'form': form
    }

    return render_to_response('ingresos/ingresarSico.html', data, context_instance=RequestContext(request))


@login_required()
def ingreso(request, pk):
    act = actividad.objects.get(id=int(pk))

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
                act = actividad.objects.get(id=int(form.data['id']))
                cli = act.cliente
                print 'Se obtuvo el id del cliente nuevo a actualizar'
                try:
                    med = medidor.objects.get(actividad=act, contrato=None)
                    med.lectura = str(form.data['lecturaRev'])
                    print 'medidor revisado'
                except:
                    pass

            if len(form.data['cedula']) == 13:
                t = 'J'
                print u'Es persona jurídica'
            else:
                t = 'N'
                print u'Es persona natural'
            cli.ci_ruc = form.data['cedula']
            cli.nombre = form.data['nombreDeCliente']
            cli.tipo = t
            cli.telefono = form.data['telefono']
            print 'se generó el cliente nuevo'

            try:
                if ts == '1':

                    cliref = request.session['clienteRef']
                    cliref.ubicacionGeografica.calle.descripcion1 = form.data['direccionRef']
                    medref = request.session['medidorRef']
                    print 'es s/N (1)'
                else:
                    cli = request.session['cliente']
                    cli.tipo = t
                    cli.telefono = form.data['telefono']
                    med = request.session['medidor']
                    med.instance.lectura = str(form.data['lecturaRev'])
                    print 'NO es s/N'

            except:
                try:
                #en caso de ser actualizacion
                    cli = cliente.objects.get(
                        id=cli.id,
                        cuenta=(form.data['codigoDeCliente']).strip(),
                        ci_ruc=(form.data['cedula']).strip()
                    )
                    cli.nombre = form.data['nombreDeCliente']
                    cli.tipo = t
                    cli.telefono = form.data['telefono']
                    print 'cliente a actualizar'
                    cli.save(force_update=True)

                    if ts != '1':
                        med.save(force_update=True)

                        enlace = detalleClienteMedidor.objects.get(
                            cliente=cli,
                            medidor=med
                        )
                        print enlace

                    else:
                        if med.id > 0:
                            med.delete()

                        ref = detalleClienteReferencia.objects.get(cliente=cli).referencia
                        call = ref.ubicacionGeografica.calle
                        call.descripcion1 = form.data['direccionRef']
                        call.save(force_update=True)

                        #actualizar
                    id = form.save(request.session['contrato'], cliente=cli)
                    dajax.script("GuardadoCorrectamenteAjax('/ingreso/" + str(id) + "');")
                    return dajax.calls

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

            id = form.save(request.session['contrato'], cliente=cli)
            dajax.script("GuardadoCorrectamenteAjax('/ingreso/" + str(id) + "');")
            #dajax.script("window.setTimeout(\"newUrl('/ingreso/" + str(id) + "')\",5000);")
        else:
            print dict(form.errors)
            dajax = mostraError(dajax, form.errors, '#err')
        try:
            del request.session['clienteRef']
            del request.session['medidorRef']
            del request.session['cliente']
            del request.session['medidor']
        except:
            pass
        return dajax.calls
    else:
        return None


@ajax()
def eliminarIngreso(request, pk):
    if request.method == 'POST':
        print request.POST
        dajax = Dajax()
        dajax.script("$('#cargandoForm').addClass('hidden');")
        form = ingresoForm(data=QueryDict(request.POST.urlencode(), mutable=True))
        if form.is_valid():
            act = actividad.objects.get(id=int(pk))
            if int(form.data['id']) == act.id:
            #borrando detalles de existir
            #de medidores...
                for m in list(medidor.objects.filter(actividad__id=act.id)):
                    try:
                        m.actividad = None
                        if m.contrato:
                            m.est = True
                        m.save(force_update=True)
                    except:
                        pass


                    #de sellos
                for s in list(sello.objects.filter(utilizado__id=act.id)):
                    try:
                        s.utilizado = None
                        s.ubicacion = 'N/A'
                        s.save(force_update=True)
                    except:
                        pass


                    #de rubros
                for r in list(detalleDeActividad.objects.filter(actividad__id=act.id)):
                    try:
                        r.delete()
                    except:
                        pass


                    #de materiales
                for m in list(materialDeActividad.objects.filter(actividad=act)):
                    #mat = detalleMaterialContrato.objects.get(id=m.material.id)
                    #mat.stock += m.cantidad
                    #mat.save(force_update=True)
                    m.delete()

                    #deFotos
                for fot in list(foto.objects.filter(actividad=act)):
                    fot.delete()

                for p in act.posicion_set.all():
                    p.actividad=None
                    p.save(force_update=True)

                act.delete()

                dajax.script("newUrl('/listadeingresos');")
                return dajax.calls

        dajax = mostraError(dajax, {'Error': 'Datos inconsistentes para proceder a eliminacion de actividad...'},
                            '#err')
        return dajax.calls
    else:
        return None


def fotos(request, pk):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            print 'es valido...'
            try:
                act = actividad.objects.get(id=int(pk))
                newdoc = foto(foto=request.FILES['foto'], actividad=act)
                newdoc.save()
            except:
                pass

            # Redirect to the document list after POST
            return HttpResponseRedirect('/fotos/%s/' % str(pk))
    else:
        form = FotoForm() # A empty, unbound form

    # Load documents for the list page
    documents = foto.objects.filter(actividad__id=int(pk))

    # Render list page with the documents and the form
    return render_to_response(
        'fotos/fotos.html',
        {
            'documents': documents,
            'form': form,
            'act': str(pk)
        },
        context_instance=RequestContext(request)
    )


def borrarFoto(request, pk):
    try:
        f = foto.objects.get(id=int(pk))
        act = str(f.actividad.id)
    except:
        act = str(pk)
        return HttpResponseRedirect('/fotos/%s/' % str(act))
    if request.method == 'POST':
        f.delete()
        return HttpResponseRedirect('/fotos/%s/' % act)
    else:
        return HttpResponseRedirect('/fotos/%s/' % act)


#funciones para ingreso en sico...#####################################################################################

def ingresar(sesion, act, estado, contrato):
    dajax = Dajax()

    scripting = None
    if act.tipoDeSolicitud.id == 1:
        scripting = ingresarServicioNuevo(sesion, contrato)
    elif act.tipoDeSolicitud.id == 13:
        scripting = ingresarCambioDeMedidor(sesion, contrato)
    elif act.tipoDeSolicitud.id == 11:
        scripting = ingresarCambioDeMaterial(sesion, contrato)
    if scripting is not None:
        scripting = scripting.elegirPunto(estado, act)
        print scripting
        if scripting['estado']:
            if str(scripting['estado']) == '13':
                dajax.script("$('#cargandoForm').addClass('hidden');")
                dajax.script("newUrl('/ingreso/" + str(act.id) + "');")
            else:

                dajax.assign('id_numeroDeSolicitud', 'value', scripting['solicitud'])
                dajax.script("$('#lblEspera').html('" + str(scripting['mensaje']) + "');")
                dajax.script(
                    "continuarIngresoSico('/continuaringreso/" + str(act.id) + "');"
                )

        else:
            dajax.script("$('#cargandoForm').addClass('hidden');")
            dajax = mostraError(dajax, {'Error': scripting['mensaje']}, '#err')
    else:
        dajax.script("$('#cargandoForm').addClass('hidden');")
        dajax = mostraError(dajax, {'Error': 'No se pudo completar la accion...'}, '#err')

    return dajax.calls

@ajax()
def continuar(request, pk):
    if request.method == 'POST':
        print request.POST
        #dajax.script("$('#cargandoForm').addClass('hidden');")
        mydict = QueryDict(request.POST.urlencode(), mutable=True)
        if len(mydict) > 3:
            form = ingresoForm(data=mydict)
            if form.is_valid():
                pass
                #guardarIngreso(request)
                #detectar estado
            else:
                dajax = Dajax()
                #dajax = mostraError(dajax, {'': dict(form.errors)['__all__']}, '#err')
                dajax = mostraError(dajax, {'Error': 'No se pudo guardar...'}, '#err')
                return dajax.calls

        #dajax.script("continuarIngresoSico('/continuaringreso/"+str(pk)+"/"+str(estado)+"');")
        act = actividad.objects.get(id=int(pk))
        return ingresar(request.user.sesion_sico, act, int(act.estadoDeSolicitud_id), request.session['contrato'])

    else:
        return None

#######################################################################################################################

def avance(request):

    contrato = request.session['contrato']
    try:
        utili = detalleDeActividad.objects.filter(rubro__contrato=contrato)
        sn = utili.filter(actividad__tipoDeSolicitud__id=1).aggregate(Sum('rubro__precioUnitario'))['rubro__precioUnitario__sum']
        if not sn:
            sn = 0
        cmat = utili.filter(actividad__tipoDeSolicitud__id=11).aggregate(Sum('rubro__precioUnitario'))['rubro__precioUnitario__sum']
        if not cmat:
            cmat = 0
        cmed = utili.filter(actividad__tipoDeSolicitud__id=13).aggregate(Sum('rubro__precioUnitario'))['rubro__precioUnitario__sum']
        if not cmed:
            cmed = 0
        diferencia = contrato.monto - (sn + cmat + cmed)
    except:
        sn = cmat = cmed = '0.0'
        diferencia = contrato.monto

    total = contrato.monto

    data = {
        'sn': str(sn).replace(',','.'),
        'cmed': str(cmed).replace(',','.'),
        'cmat': str(cmat).replace(',','.'),
        'dif': str(diferencia).replace(',','.'),
        'tot': str(total).replace(',','.')
    }

    return render_to_response('avancedeobra/avance.html', data, context_instance=RequestContext(request))


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