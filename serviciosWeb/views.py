# coding=utf-8
# Create your views here.
import datetime
from decimal import *
import os
from django.core.files.base import ContentFile
from django.utils import timezone
from time import time
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from soaplib.serializers import primitive
from soaplib.serializers.clazz import Array
from soaplib.service import DefinitionBase, rpc
from ControlSystem import settings
from ControlSystem.pComm.busquedas.scriptsBusquedas import buscar
from ControlSystem.pComm.busquedas.SW_scriptsBusquedas import buscar as SW_buscar
from busquedas.models import vitacoraBusquedas
from handler import DjangoSoapApp
from ingresos.models import actividad, empleado, tipoDeSolicitud, cuadrilla, materialDeLaRed, formaDeConexion, estadoDeUnaInstalacion, tipoDeConstruccion, ubicacionDelMedidor, tipoDeAcometidaRed, calibreDeLaRed, usoDeEnergia, claseRed, tipoDeServicio, usoEspecificoDelInmueble, demanda, nivelSocieconomico, detalleClienteMedidor, detalleDeActividad, detalleClienteReferencia, cliente, instalador, motivoParaSolicitud, materialDeActividad, foto
from inventario.models import detalleMaterialContrato, sello, medidor, detalleRubro
from usuarios.models import usuarioSico, contrato, posicion
from usuarios.views import integracion, cerrarSico


#servicio web de ejemplo
class HelloWorldService(DefinitionBase):
    @rpc(primitive.String, primitive.Integer, _returns=primitive.String)
    def say_hello(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s ' % name)
        return str(results)


hello_world_service = DjangoSoapApp([HelloWorldService], __name__)


class SW_Usuarios(DefinitionBase):
    @rpc(_returns=Array(Array(primitive.String)))
    def getContratos(self, ):
        m = []
        r = contrato.objects.filter(finalVigencia__gte=datetime.date.today())
        for cont in r:
            m.append([cont.num, cont.zonas])
        return m

    @rpc(primitive.String, primitive.String, primitive.String, _returns=Array(primitive.String))
    def login(self, u, p, c):
        error = []
        user = authenticate(username=u, password=p)
        if user is not None:
            if user.is_active:
                if user.sesion_sico:
                    error = ["El Usuario especificado ya esta en uso."]
                else:
                    try:
                        print c
                        u = usuarioSico.objects.get(user=user, contrato=c)
                    except:
                        u = False
                    if isinstance(u, usuarioSico):
                        if integracion(u.nombre, u.clave, user):
                            error = [
                                'True',
                                str(user.id),
                                str(user.username),
                                str(user.sesion_sico),
                                ('%s %s' % (user.first_name, user.last_name)).encode('utf-8')
                            ]
                        else:
                            error = ['El Sistema Comercial(Sico Cnel) no esta disponible por el momento, '
                                     'intentelo nuevamente mas tarde...']
                            user.sesion_sico = ''
                            user.save()
                    else:
                        error = ['El Usuario Especificado no cuenta con permisos necesarios para acceder al contarto']

        elif u and p:
            error = ["Su Usuario o Contraseña no son correctos, Intentelo nuevamente."]
        return error

    @rpc(primitive.Integer, primitive.String, primitive.String, _returns=primitive.Boolean)
    def logout(self, id, u, s):
        user = User.objects.get(id=id, username=u, sesion_sico=s)
        if user:
            cerrarSico(s)
            user.sesion_sico = ''
            user.save()
            return True
        return False


sw_usuarios = DjangoSoapApp([SW_Usuarios], __name__)


class SW_Busquedas(DefinitionBase):
    @rpc(primitive.Integer, primitive.String, primitive.Integer, primitive.String, primitive.Boolean,
         _returns=Array(Array(primitive.String)))
    def buscarDjango(self, idUsuario, sesion, tipo, dato, esIngreso):
        client = None
        busc = vitacoraBusquedas(
            tipoBusq=str(tipo),
            consulta=dato,
            usuario=User.objects.get(id=idUsuario, sesion_sico=sesion),
            estadoRetorno=True
        )
        b = buscar(sesion)
        operaciones = {
            '1': b.porCuenta,
            '2': b.porMedidor,
            '3': b.porNombre,
            '4': b.porGeocodigo
        }
        res = operaciones[str(tipo)](dato)

        coincidencias = []
        cli = []
        medidores = []

        #print res

        if res:
            busc.save()

            for c in res['cClientes']:

                if tipo == 1:
                    coincidencias.append(c.cuenta)
                    coincidencias.append(c.nombre)
                    coincidencias.append(c.ubicacionGeografica.calle.descripcion1)
                    coincidencias.append(str(c.deuda))
                    coincidencias.append(str(c.meses))
                elif tipo == 2:
                    coincidencias.append(c.ubicacionGeografica.urbanizacion.descripcion)
                    coincidencias.append(c.estado)
                    coincidencias.append(c.cuenta)
                    coincidencias.append(c.nombre)
                    coincidencias.append(c.ubicacionGeografica.calle.descripcion1)
                elif tipo == 3:
                    coincidencias.append(c.nombre)
                    coincidencias.append(c.ubicacionGeografica.calle.descripcion1)
                    coincidencias.append(c.cuenta)
                    coincidencias.append(str(c.deuda))
                    coincidencias.append(str(c.meses))
                elif tipo == 4:
                    coincidencias.append(c.ubicacionGeografica.interseccion.descripcion1)
                    coincidencias.append(c.cuenta)
                    coincidencias.append(c.nombre)
                    coincidencias.append(c.ubicacionGeografica.calle.descripcion1)
                    coincidencias.append(c.ubicacionGeografica.urbanizacion.descripcion)
                    coincidencias.append(str(c.deuda))

            c = res['formCliente']

            cli.append(c.instance.ci_ruc)
            cli.append(c.instance.cuenta)
            cli.append(c.instance.nombre)
            cli.append(c.fields['direccion'].initial)
            cli.append(c.fields['interseccion'].initial)
            cli.append(c.fields['urbanizacion'].initial)
            cli.append(c.instance.estado)
            cli.append(c.fields['geo'].initial)
            cli.append(c.fields['nparr'].initial)
            cli.append(c.fields['parroquia'].initial)
            cli.append(str(c.instance.meses))
            cli.append(str(c.instance.deuda))

            client = c.instance
            if esIngreso:
                client.save()

            for c in res['cMedidores']:

                medidores.append(c.fields['marc'].initial)
                medidores.append(c.fields['tecnologia'].initial)
                medidores.append(c.fields['tension'].initial)
                medidores.append(c.fields['amperaje'].initial)
                medidores.append(c.fields['fi'].initial)
                medidores.append(c.fields['fd'].initial)
                medidores.append(c.fields['li'].initial)
                medidores.append(c.fields['ld'].initial)
                medidores.append(c.instance.fabrica)
                medidores.append(str(c.instance.serie))
                medidores.append(str(c.instance.tipo))
                medidores.append(str(c.instance.digitos))
                medidores.append(str(c.instance.fases))
                medidores.append(str(c.instance.hilos))
                med = c.instance

                if esIngreso:
                    med.save()
                    try:
                        li = Decimal((str(c.fields['li'].initial).strip()))
                    except:
                        li = Decimal('0000')

                    try:
                        ld = Decimal((str(c.fields['ld'].initial).strip()))
                    except:
                        ld = Decimal('0000')

                    try:
                        fi = datetime.datetime.strptime((str(c.fields['fi'].initial).strip()), "%d/%m/%Y").date()
                    except:
                        fi = datetime.datetime.strptime('1/01/1900', "%d/%m/%Y").date()

                    try:
                        fd = datetime.datetime.strptime((str(c.fields['fd'].initial).strip()), "%d/%m/%Y").date()
                    except:
                        fd = None
                    print 'guardar detalle'
                    d = detalleClienteMedidor(
                        lectura_instalacion=li,
                        lectura_desinstalacion=ld,
                        fecha_instalacion=fi,
                        fecha_desinstalacion=fd,
                        medidor=med,
                        cliente=client
                    )
                    d.save()

        if esIngreso:
            return [
                coincidencias,
                cli,
                medidores,
                [str(client.id)],
            ]

        return [
            coincidencias,
            cli,
            medidores
        ]


    @rpc(primitive.String, primitive.String, primitive.String, primitive.String,
         _returns=Array(Array(primitive.String)))
    def buscarMovil(self, idUsuario, sesion, tipo, dato):
        busc = vitacoraBusquedas(
            tipoBusq=str(tipo),
            consulta=dato,
            usuario=User.objects.get(id=int(idUsuario), sesion_sico=sesion),
            estadoRetorno=True
        )
        print 'buscando por %s , %s' % (str(tipo), str(dato))
        movilBusqueda = SW_buscar(sesion)
        if movilBusqueda:
            busc.save()
            return movilBusqueda.busquedaIntegrada(tipo, dato)
        return None


sw_busquedas = DjangoSoapApp([SW_Busquedas], __name__)


class SW_Ingresos(DefinitionBase):
    @rpc(primitive.String, primitive.String, _returns=Array(Array(primitive.String)))
    def realizados(self, idUsuario, contrato):
        rel = posicion.objects.filter(
            actividad__detalledeactividad__rubro__contrato=contrato
        ).filter(
            usuario_id=int(idUsuario), fechaHora__gte='%s-%s-%s 00:00:00' % (
                str(datetime.datetime.today().year),
                str(datetime.datetime.today().month),
                str(datetime.datetime.today().day)
            )
        ).distinct('actividad').exclude(actividad=None)

        ret = []

        for r in rel:
            act = r.actividad
            try:
                med = str(act.medidor_set.filter(contrato=None).first().fabrica)
            except:
                med = 'Sin Medidor Desc.'
            ret.append(
                [
                    str(act.id),
                    str(act.cliente.cuenta),
                    str(act.cliente.nombre),
                    str(act.tipoDeSolicitud.descripcion),
                    med,
                    str(act.tipoDeSolicitud.id),
                    str(act.observaciones)
                ]
            )
        print ret
        return ret


    @rpc(_returns=Array(Array(primitive.String)))
    def ingresoActividadInstalador(self, ):
        return [
            [str(v) for v in empleado.objects.all()],
            [str(v) for v in cuadrilla.objects.all()],
            [str(v) for v in tipoDeSolicitud.objects.all()]
        ]


    @rpc(primitive.String, _returns=Array(primitive.String))
    def ingresoActividadInstaladorActividadSeleccionada(self, ide):
        act = actividad.objects.get(id=int(ide))
        return [
            str(act.instalador.nombre),
            str(act.instalador.cuadrilla),
            str(act.tipoDeSolicitud),
            str(act.fechaDeActividad),
            str(act.horaDeActividad)
        ]


    @rpc(primitive.String, _returns=Array(primitive.String))
    def ingresoDatosAbonadoSeleccionado(self, ide):
        act = actividad.objects.get(id=int(ide))
        m = act.medidor_set.all().filter(contrato=None)

        if m.count() <= 0:
            return [
                str(act.cliente.cuenta),
                str(act.cliente.ci_ruc),
                str(act.cliente.nombre),
                str(act.cliente.estado),
                str(act.cliente.telefono),
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                str(act.cliente.id),
            ]

        else:
            return [
                str(act.cliente.cuenta),
                str(act.cliente.ci_ruc),
                str(act.cliente.nombre),
                str(act.cliente.estado),
                str(act.cliente.telefono),
                str(act.cliente.ubicacionGeografica.parroquia.descripcion),
                str(act.cliente.ubicacionGeografica.calle.descripcion1),
                str(act.cliente.geocodigo),
                str(m.first().fabrica),
                str(m.first().serie),
                str(m.first().marca),
                str(m.first().lectura),
                str(act.cliente.id)
            ]


    @rpc(_returns=Array(Array(primitive.String)))
    def ingresoDetalleInstalacion(self, ):
        return [
            [str(v) for v in materialDeLaRed.objects.all()],
            [str(v) for v in formaDeConexion.objects.all()],
            [str(v) for v in estadoDeUnaInstalacion.objects.all()],
            [str(v) for v in tipoDeConstruccion.objects.all()],
            [str(v) for v in ubicacionDelMedidor.objects.all()],
            [str(v) for v in tipoDeAcometidaRed.objects.all()],
            [str(v) for v in calibreDeLaRed.objects.all()],
            [str(v) for v in usoDeEnergia.objects.all()],
            [str(v) for v in claseRed.objects.all()],
            [str(v) for v in tipoDeServicio.objects.all()],
            [str(v) for v in usoEspecificoDelInmueble.objects.all()],
            [str(v) for v in demanda.objects.all()],
            [str(v) for v in nivelSocieconomico.objects.all()]
        ]


    @rpc(primitive.String, _returns=Array(primitive.String))
    def ingresoDetalleInstalacionSeleccionada(self, ide):
        act = actividad.objects.get(id=int(ide))

        return [
            str(act.materialDeLaRed),
            str(act.formaDeConexion),
            str(act.estadoDeLaInstalacion),
            str(act.tipoDeConstruccion),
            str(act.ubicacionDelMedidor),
            str(act.tipoDeAcometidaRed),
            str(act.calibreDeLaRed),
            str(act.usoDeEnergia),
            str(act.claseRed),
            str(act.tipoDeServicio),
            str(act.usoEspecificoDelInmueble),
            str(act.demanda),
            str(act.nivelSocieconomico)
        ]


    @rpc(primitive.String, _returns=Array(Array(primitive.String)))
    def ingresoMateriales(self, contrato):
        return [
            [str(v) for v in detalleMaterialContrato.objects.filter(contrato=contrato)
            .exclude(material__tipoDeMaterial__material__descripcion='KIT ')],
            [str(v) for v in sello.objects.filter(detalleMaterialContrato__contrato=contrato, utilizado=None)],
            [
                'Caja',
                'Bornera',
                'Panel',
                'N/A'
            ]
        ]

    @rpc(primitive.String, primitive.String, _returns=Array(Array(primitive.String)))
    def ingresoMaterialesSeleccionados(self, ide, cont):
        act = actividad.objects.get(id=int(ide))
        deta = act.detalledeactividad_set.all()
        mat = act.materialdeactividad_set.all()
        sell = act.sello_set.all()

        print act.cliente.cuenta
        print cont

        try:
            if len(list(deta.filter(
                    actividad=act,
                    rubro=detalleRubro.objects.get(
                            servicio__id=3,
                            rubro__id=1
                    )))) > 0:
                reubicacion = True
            else:
                reubicacion = False
        except:
            reubicacion = False

        try:
            if len(list(deta.filter(
                    actividad=act,
                    rubro=detalleRubro.objects.get(
                            servicio__id=4,
                            rubro__id=4
                    )))) > 0:
                contrastacion = True
            else:
                contrastacion = False
        except:
            contrastacion = False

        try:
            if len(list(deta.filter(
                    actividad=act,
                    rubro=detalleRubro.objects.get(
                            servicio__id=6,
                            rubro__id=2
                    )))) > 0:
                directo = True
            else:
                directo = False
        except:
            directo = False

        b = [
            [str(reubicacion), ""],
            [str(contrastacion), ""],
            [str(directo), ""],
            [str(v.cantidad) for v in mat],
            [str(v.material) for v in mat],
            [str(v) for v in sell],
            [str(v.ubicacion) for v in sell]
        ]
        print b
        return b


    @rpc(primitive.String, _returns=Array(primitive.String))
    def ingresoMedidorInstalado(self, contrato):
        return [
            str(v) for v in medidor.objects.filter(
                contrato__contrato=contrato,
                est=True,
                actividad=None
            )
        ]


    @rpc(primitive.String, primitive.String, primitive.String, _returns=Array(primitive.String))
    def ingresoMedidorInstaladoSel(self, contrato, med, ide):
        medidores = medidor.objects.filter(
            contrato__contrato=contrato,
            est=True,
            actividad=None
        ).order_by('fabrica')
        print ide
        print med
        if ide:
            medidores = medidor.objects.filter(
                contrato__contrato=contrato,
                actividad=actividad.objects.get(id=int(ide))
            )

        for m in medidores:
            if med == str(m.__unicode__()):
                return [
                    str(m.id),
                    str(m.fabrica),
                    str(m.serie),
                    str(m.marca),
                    str(m.tipo),
                    str(m.lectura)
                ]

        return []


    @rpc(primitive.String, primitive.String, _returns=Array(primitive.String))
    def ingresoMedidorInstaladoSeleccionado(self, contrato, ide):
        medidores = medidor.objects.filter(
            contrato__contrato=contrato,
            actividad=actividad.objects.get(id=int(ide))
        )
        print ide
        if medidores.first():
            m = medidores.first()
            return [
                str(m)
            ]

        return []


    @rpc(primitive.String, _returns=Array(primitive.String))
    def ingresosReferenciaSeleccionada(self, ide):
        act = actividad.objects.get(id=int(ide))
        deta = detalleClienteReferencia.objects.get(cliente=act.cliente)
        medidores = deta.referencia.detalleclientemedidor_set.all()
        actual = None
        for m in medidores:
            if m.fecha_desinstalacion == None or \
                            m.fecha_desinstalacion == '' or \
                            m.fecha_desinstalacion == '00/00/0000' or \
                            m.fecha_desinstalacion == '0/00/0000':
                actual = m.medidor
                break

        if actual:
            return [
                str(actual.fabrica),
                str(actual.serie),
                str(actual.marca),
                str(deta.referencia.cuenta),
                str(deta.referencia.id)
            ]
        else:
            return [
                '',
                '',
                '',
                str(deta.referencia.cuenta),
                str(deta.referencia.id)
            ]

    @rpc(Array(Array(primitive.String)), _returns=Array(Array(primitive.String)))
    def prueba_array(self, arr):
        print arr
        return arr


    @rpc(_returns=Array(Array(primitive.String)))
    def ubicacion(self, ):
        rel = posicion.objects.filter(
            fechaHora__gte='%s-%s-%s 00:00:00' % (
                str(datetime.datetime.today().year),
                str(datetime.datetime.today().month),
                str(datetime.datetime.today().day)
            )
        ).order_by('-fechaHora').distinct('fechaHora')

        ret = []

        for r in rel:
            ret.append(
                [
                    '%s %s' % (r.usuario.first_name, r.usuario.last_name),
                    str((timezone.localtime(r.fechaHora).time())),
                    str(r.latitud),
                    str(r.longitud),
                ]
            )
        print ret
        return ret

    @rpc(primitive.String, primitive.String, primitive.String, primitive.String, _returns=primitive.Boolean)
    def guardarUbicacion(self, idUsuario, fechahora, latitud, longitud):
        rel = posicion(
            fechaHora=fechahora,
            latitud=latitud,
            longitud=longitud,
            usuario=User.objects.get(id=int(idUsuario))
        )

        if isinstance(rel.save(), posicion):
            return True
        else:
            return False


    @rpc(Array(Array(primitive.String)), _returns=Array(primitive.String))
    def guardarActividad(self, datas):

        data = datas[0]
        ts = '%d' % tipoDeSolicitud.objects.get(id=data[0][:2]).id

        try:
            cli = cliente.objects.get(id=int(data[1]))
            med = cli.detalleclientemedidor_set.all().filter(
                medidor__fabrica=str(data[9]),
                medidor__serie=str(data[32]),
                fecha_desinstalacion=None
            ).first().medidor
        except:
            cli = None
            med = None

        try:
            idact = int(data[2])
        except:
            idact = 0

        if idact != 0:
            act = actividad.objects.get(id=int(idact))
            cli = act.cliente
            print 'Se obtuvo el id del cliente nuevo a actualizar'
            try:
                med = medidor.objects.get(actividad=act, contrato=None)
                med.lectura = str(data[3])
                print 'medidor revisado'
            except:
                pass

        t = 'N'
        if cli:
            if len(str(data[4])) == 13:
                t = 'J'
                print u'Es persona jurídica'
            else:
                t = 'N'
                print u'Es persona natural'
            cli.ci_ruc = data[4]
            cli.nombre = data[5]
            cli.tipo = t
            cli.telefono = data[6]
            print 'se generó el cliente nuevo'
        cliref = None
        medref = None
        try:
            if ts == '1':
                if not cli:
                    cli = cliente(
                        ci_ruc=data[4],
                        nombre=data[5],
                        telefono=data[6]
                    )
                cliref = cliente.objects.get(id=data[7])
                #cliref.ubicacionGeografica.calle.descripcion1 = form.data['direccionRef']
                medref = cliref.detalleclientemedidor_set.all().filter(
                    medidor__fabrica=str(data[8]),
                    fecha_desinstalacion=None
                ).first()
                print 'es s/N (1)'
            else:
                cli.tipo = t
                cli.telefono = data[6]
                #med = request.session['medidor']
                med.lectura = str(data[3])
                print 'NO es s/N'

        except:
            try:
            #en caso de ser actualizacion
                cli = cliente.objects.get(
                    id=cli.id,
                    cuenta=(data[10]).strip(),
                    ci_ruc=(data[4]).strip()
                )
                cli.nombre = data[5]
                cli.tipo = t
                cli.telefono = data[6]
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
                    #call.descripcion1 = form.data['direccionRef']
                    call.save(force_update=True)

                    #actualizar
                id = formSave(data[11], datas, cliente=cli)
                #dajax.script("newUrl('/ingreso/" + str(id) + "');")
                if id > 0:
                    msj = 'Actividad modificada Correctamente'
                else:
                    msj = 'Error al guardar la actividad...'
                return [
                    str(id),
                    msj
                ]

            except:
                #dajax = mostraError(dajax, {'Error': 'Datos invalidos para guardar...'}, '#err')
                return [
                    '0',
                    'Error al actualizar la actividad...'
                ]


        #guardar por primera vez
        cli.save()

        if ts == '1':
            #cliref.save()
            #medref.instance.save()
            #fi = formatFechas(medref.fields['fi'].initial)
            #fd = formatFechas(medref.fields['fd'].initial)
            #d = detalleClienteMedidor(
            #    cliente=cliref,
            #    medidor=medref,
            #    lectura_instalacion=float(medref.fields['li'].initial),
            #    lectura_desinstalacion=float(medref.fields['ld'].initial),
            #    fecha_instalacion=fi,
            #    fecha_desinstalacion=fd,
            #)
            #d.save()
            dcr = detalleClienteReferencia(
                cliente=cli,
                referencia=cliref,
                medidorDeReferencia=str(data[8]),
                ubicacion=cliref.ubicacionGeografica
            )

            dcr.save()
            if med:
                med.delete()
        else:
            med.save()

            #fi = formatFechas(med.fields['fi'].initial)
            #fd = formatFechas(med.fields['fd'].initial)
            #
            #d = detalleClienteMedidor(
            #    cliente=cli,
            #    medidor=med.instance,
            #    lectura_instalacion=float(med.fields['li'].initial),
            #    lectura_desinstalacion=float(med.fields['ld'].initial),
            #    fecha_instalacion=fi,
            #    fecha_desinstalacion=fd,
            #)
            #d.save()

        print 'Correcto...'

        id = formSave(data[11], datas, cliente=cli)
        #dajax.script("newUrl('/ingreso/" + str(id) + "');")
        msj1 = ''
        if id > 0:
            msj = 'Actividad guardada Correctamente'
            print msj
            rel = posicion(
                fechaHora=data[40],
                latitud=Decimal(data[41]),
                longitud=Decimal(data[42]),
                usuario=User.objects.get(id=int(data[39])),
                actividad=actividad.objects.get(id=id)
            )
            if isinstance(rel.save(), posicion):
                msj1 = 'Posicion Guardada'
                print msj1
            else:
                msj1 = 'Posicion NO Guardada'
                print msj1
        else:
            msj = 'Error al guardar la actividad...'
            print msj

        return [
            str(id),
            msj,
            msj1
        ]


    @rpc(primitive.String, _returns=Array(primitive.String))
    def eliminarActividad(self, pk):

        try:
            act = actividad.objects.get(id=int(pk))
            #borrando detalles de existir
            #de medidores...
            for m in list(medidor.objects.filter(actividad__id=act.id)):
                try:
                    m.actividad = None
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
                p.actividad = None
                p.save(force_update=True)

            act.delete()

            return [
                '0',
                'Actividad Eliminada Permanentemente...'
            ]
        except Exception:
            return [
                '1',
                'Error, No se pudo eliminar correctamente la actividad...'
            ]


    @rpc(primitive.String, primitive.String, primitive.String, _returns=primitive.String)
    def guardarFoto(self, strFoto, pk, nombreFoto):

        try:

            # saving base string from post data
            base64_string = strFoto

            #filename = str(nombreFoto)
            filename = "(tomada-%s)-(subida-%s).png" % (
                str(nombreFoto).replace(':','_'),
                str(timezone.localtime(timezone.now())).replace(':','_').replace('.','_')
            )
            print filename

            # decoding base string to image and saving in to your media root folder
            #fh = open(os.path.join(settings.MEDIA_ROOT, filename), "wb")
            #fh.write(base64_string.decode('base64'))
            #fh.close()

            # saving decoded image to database
            decoded_image = base64_string.decode('base64')

            newdoc = foto()
            newdoc.actividad = actividad.objects.get(id=int(pk))
            newdoc.foto = ContentFile(decoded_image, filename)
            newdoc.save()
            print 'Foto guardada...'
            # add blur effect to saved image and saving in to media root folder
            #im = Image.open(os.path.join(settings.MEDIA_ROOT, filename))
            #im_blur = im.filter(ImageFilter.EMBOSS)
            # save blur image to media root
            #new_filename="blur_"+filename
            #im_blur.save(os.path.join(settings.MEDIA_ROOT, new_filename))

            return 'Foto %s Guardada' % str(nombreFoto)

        except :
            return 'Foto %s NO Guardada' % str(nombreFoto)

sw_ingresos = DjangoSoapApp([SW_Ingresos], __name__)


def formSave(contrato, datas, cliente=None):
    data = datas[0]

    print data[2]

    act = actividad()
    if cliente is not None:
        act.cliente = cliente
    print datas
    act.tipoDeConstruccion = tipoDeConstruccion.objects.get(id=int(str(data[12])[:2]))

    instala = None
    for ins in empleado.objects.all():
        if ins.__unicode__() == data[13]:
            instala = ins
            break

    cuadrill = None
    for cua in cuadrilla.objects.all():
        if cua.__unicode__() == data[14]:
            cuadrill = cua
            break
    print str(instala) + " - " + str(cuadrill)
    try:
        inst = instalador.objects.get(
            nombre=empleado.objects.get(id=instala.id),
            cuadrilla=cuadrilla.objects.get(id=cuadrill.id)
        )
    except:
        inst = instalador(
            nombre=empleado.objects.get(id=instala.id),
            cuadrilla=cuadrilla.objects.get(id=cuadrill.id),
            observacion=str(data[22])
        )
        inst.save()

    act.instalador = inst
    act.ubicacionDelMedidor = ubicacionDelMedidor.objects.get(id=int(str(data[15])[:2]))
    act.claseRed = claseRed.objects.get(id=str(data[16])[:1])
    act.nivelSocieconomico = nivelSocieconomico.objects.get(id=str(data[17][:2]))
    act.calibreDeLaRed = calibreDeLaRed.objects.get(id=int(str(data[18])[:2]))
    act.estadoDeLaInstalacion = estadoDeUnaInstalacion.objects.get(id=int(str(data[19])[:2]))
    act.tipoDeAcometidaRed = tipoDeAcometidaRed.objects.get(id=str(data[20][:2]))
    act.tipoDeServicio = tipoDeServicio.objects.get(id=str(data[21][:3]))

    act.fechaDeActividad = datetime.date(
        int(str(data[22]).split('/')[2]),
        int(str(data[22]).split('/')[1]) + 1,
        int(str(data[22]).split('/')[0])
    )

    try:
        act.horaDeActividad = datetime.datetime.strptime(str(data[23]), '%H:%M')
    except:
        act.horaDeActividad = datetime.time(hour=10, minute=30, second=0)

    act.usoDeEnergia = usoDeEnergia.objects.get(id=str(data[24])[:2])
    act.usoEspecificoDelInmueble = usoEspecificoDelInmueble.objects.get(id=int(str(data[25])[:2]))
    act.formaDeConexion = formaDeConexion.objects.get(id=int(str(data[26])[:2]))
    act.demanda = demanda.objects.get(id=int(str(data[27])[:2]))
    act.motivoDeSolicitud = motivoParaSolicitud.objects.get(id=int(str(data[28])[:2]))
    act.tipoDeSolicitud = tipoDeSolicitud.objects.get(id=int(str(data[29])[:2]))
    act.materialDeLaRed = materialDeLaRed.objects.get(id=str(data[30])[:2])
    act.observaciones = str(data[31])

    if data[2] != '':
        act.id = int(str(data[2]))
        #act.numeroDeSolicitud = self.data['numeroDeSolicitud']
        #act.estadoDeSolicitud = estadoDeSolicitud.objects.get(id=int(self.data['estadoSolicitud']))
        act.save(force_update=True)
    else:
        act.save()

    print data[22]

    #borrando detalles de existir
    #de medidores...
    for m in list(medidor.objects.filter(actividad__id=act.id)):
        try:
            m.est = True
            m.actividad = None
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

        #hay que generar detalles...
        #empezando con medidores
    try:
        medDeActividad = medidor.objects.get(
            fabrica=str(data[9]),
            serie=str(data[32])
        )
        medDeActividad.est = False
        medDeActividad.actividad = act
        medDeActividad.save(force_update=True)
    except:
        pass
    try:
        medDeActividad = medidor.objects.get(
            fabrica=str(data[33]),
            serie=str(data[34])
        )
        medDeActividad.est = False
        medDeActividad.lectura = str('%05d' % int(data[35]))
        medDeActividad.actividad = act
        medDeActividad.save(force_update=True)
    except:
        pass


    #luego con sellos
    sellosInstalados = list(datas[1])
    for s in sello.objects.all():
        for i in range(len(sellosInstalados)):
            if s.__unicode__() == sellosInstalados[i]:
                sellosInstalados[i] = s.id

    ubiSellosInstalados = list(datas[2])
    print sellosInstalados[0]
    print ubiSellosInstalados

    for sell in range(len(sellosInstalados)):
        si = sello.objects.get(id=sellosInstalados[sell])
        si.ubicacion = ubiSellosInstalados[sell]
        si.utilizado = act
        si.save(force_update=True)
        print si

        #continuando con detalle de materiales para actividad

    materialInstalado = list(datas[3])
    for s in detalleMaterialContrato.objects.all():
        for i in range(len(materialInstalado)):
            if s.__unicode__() == materialInstalado[i]:
                materialInstalado[i] = s.id
    cantMaterialInstado = list(datas[4])
    #print materialInstalado
    for m in range(len(cantMaterialInstado)):
        mat = detalleMaterialContrato.objects.get(id=materialInstalado[m])
        #print int(materialInstalado[m])
        actMat = materialDeActividad(
            material=mat,
            actividad=act,
            cantidad=long(cantMaterialInstado[m])
        )
        #mat.stock -= actMat.cantidad
        actMat.save()
        print actMat
        #mat.save(force_update=True)

    #actividades realizadas para desgloce de valores a facturar
    realizadas = [[5, 6], [5, 8]]
    if act.tipoDeSolicitud_id == 1:
        realizadas.append([1, 1])
        realizadas.append([5, 7])
        print 'servicio nuevo...'
    elif act.tipoDeSolicitud_id == 11 or act.tipoDeSolicitud_id == 13:
        try:
            print
            if parseBoolString(data[36]):
                realizadas.append([4, 4])
                print 'Contrastacion...'
        except:
            pass
        try:
            if parseBoolString(data[37]):
                realizadas.append([3, 1])
                print 'Reubicacion...'
        except:
            pass
        try:
            if materialDeActividad.objects.get(
                    actividad=act,
                    material=detalleMaterialContrato.objects.get(
                            contrato=contrato,
                            material__tipoDeMaterial__material__id=6#cable
                    )
            ):
                try:
                    if realizadas.index([3, 1]) >= 0:
                        realizadas.append([5, 7])
                        print 'Reubicacion y desgloce para cable...'
                except ValueError:
                    realizadas.append([4, 3])
                    realizadas.append([5, 7])
                    print 'Hay Solo Acometida...'
        except:
            pass

        if act.tipoDeSolicitud_id == 11:
            try:
                if materialDeActividad.objects.get(
                        actividad=act,
                        material=detalleMaterialContrato.objects.get(
                                contrato=contrato,
                                material__tipoDeMaterial__material__id=4#caja
                        )
                ):
                    realizadas.append([4, 2])
                    print u'Se realizó cambio de caja...'
            except:
                try:
                    if materialDeActividad.objects.get(
                            actividad=act,
                            material=detalleMaterialContrato.objects.get(
                                    contrato=contrato,
                                    material__tipoDeMaterial__material__id=16#sello
                            )
                    ) and len(cantMaterialInstado) == 1:
                        realizadas.append([4, 5])
                        print u'Se realizó revision que no incluye material...'
                except:
                    pass
        elif act.tipoDeSolicitud_id == 13:
            try:
                if parseBoolString(data[38]):
                    realizadas.append([6, 2])
                    print 'Directo...'
            except:
                realizadas.append([2, 2])
                print 'Cambio de Medidor...'
            try:
                if realizadas.index([5, 7]) >= 0:
                    print 'desgloce de Gis...'
            except:
                realizadas.append([5, 7])
                print 'se agregó desgloce de Gis...'

    for a in realizadas:
        try:
            actDeta = detalleDeActividad(
                rubro=detalleRubro.objects.get(
                    servicio__id=a[0],
                    rubro__id=a[1],
                    contrato=contrato
                ),
                actividad=act
            )
            actDeta.save()
        except:
            print 'nose pudo guardar :' + str(a)

    print 'Guardado completo de Actividad...id : %s ' % act.id
    return act.id


def parseBoolString(theString):
    return theString[0].upper() == 'T'