# coding=utf-8
# Create your views here.
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from soaplib.serializers import primitive
from soaplib.serializers.clazz import Array
from soaplib.service import DefinitionBase, rpc
from ControlSystem.pComm.busquedas.scriptsBusquedas import buscar
from ControlSystem.pComm.busquedas.SW_scriptsBusquedas import buscar as SW_buscar
from busquedas.models import vitacoraBusquedas
from handler import DjangoSoapApp
from ingresos.models import actividad, empleado, tipoDeSolicitud, cuadrilla, materialDeLaRed, formaDeConexion, estadoDeUnaInstalacion, tipoDeConstruccion, ubicacionDelMedidor, tipoDeAcometidaRed, calibreDeLaRed, usoDeEnergia, claseRed, tipoDeServicio, usoEspecificoDelInmueble, demanda, nivelSocieconomico, detalleClienteMedidor, detalleDeActividad, detalleClienteReferencia
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
                        #if integracion(u.nombre, u.clave, user):
                        error = [
                            'True',
                            str(user.id),
                            str(user.username),
                            str(user.sesion_sico),
                            ('%s %s' % (user.first_name, user.last_name)).encode('utf-8')
                        ]
                        #else:
                        #    error = ['El Sistema Comercial(Sico Cnel) no esta disponible por el momento, '
                        #             'intentelo nuevamente mas tarde...']
                        #    user.sesion_sico=''
                        #    user.save()
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
    @rpc(primitive.Integer, primitive.String, primitive.Integer, primitive.String, _returns=primitive.String)
    def buscarDjango(self, idUsuario, sesion, tipo, dato):
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
        if res:
            busc.save()
        return str(res)

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
                    med
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
        m = act.medidor_set.get(contrato=None)
        return [
            str(act.cliente.cuenta),
            str(act.cliente.ci_ruc),
            str(act.cliente.nombre),
            str(act.cliente.estado),
            str(act.cliente.telefono),
            str(act.cliente.ubicacionGeografica.parroquia.descripcion),
            str(act.cliente.ubicacionGeografica.calle.descripcion1),
            str(act.cliente.geocodigo),
            str(m.fabrica),
            str(m.serie),
            str(m.marca),
            str(m.lectura)
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
            else: reubicacion = False
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
            else: contrastacion = False
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
            else: directo = False
        except:
            directo = False

        b =  [
            [str(reubicacion),""],
            [str(contrastacion),""],
            [str(directo),""],
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
            est=True
        )
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
        for m in medidores:
            if m.fecha_desinstalacion == None or \
                            m.fecha_desinstalacion == '' or \
                            m.fecha_desinstalacion == '00/00/0000' or \
                            m.fecha_desinstalacion == '0/00/0000':
                actual=m.medidor
                break

        if actual:
            return [
                str(actual.fabrica),
                str(actual.serie),
                str(actual.marca),
                str(deta.referencia.cuenta)
            ]
        else:
            return [
                '',
                '',
                '',
                str(deta.referencia.cuenta)
            ]



sw_ingresos = DjangoSoapApp([SW_Ingresos], __name__)