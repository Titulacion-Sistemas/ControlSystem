# coding=utf-8
# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from soaplib.serializers import primitive
from soaplib.serializers.clazz import Array
from soaplib.service import DefinitionBase, rpc
from ControlSystem.pComm.scriptsBusquedas import buscar
from ControlSystem.pComm.SW_scriptsBusquedas import buscar as SW_buscar
from busquedas.models import vitacoraBusquedas
from handler import DjangoSoapApp
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
    @rpc(primitive.String, primitive.String, _returns=Array(primitive.String))
    def login(self, u, p):
        error = []
        user = authenticate(username=u, password=p)
        if user is not None:
            if user.is_active:
                if user.sesion_sico:
                    error = ["El Usuario especificado ya esta en uso."]
                else:
                    user.sesion_sico = (integracion(user.usuario_sico, user.contrasenia_sico)).activeConnection
                    user.save()
                    error = [
                        'True',
                        str(user.id),
                        str(user.username),
                        str(user.sesion_sico),
                        ('%s %s' % (user.first_name, user.last_name)).encode('utf-8')
                    ]
        elif u and p:
            error=["Su Usuario o Contraseña no son correctos, Intentelo nuevamente."]
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
        #return str((((res['cMedidores'])[0]).save(commit=False)).digitos)
        #return str((((res['cMedidores'])[0]).fields['marc'].initial))
        return str(res)

    @rpc(primitive.Integer, primitive.String, primitive.Integer, primitive.String,
         _returns=Array(Array(primitive.String)))
    def buscarMovil(self, idUsuario, sesion, tipo, dato):
        busc = vitacoraBusquedas(
            tipoBusq=str(tipo),
            consulta=dato,
            usuario=User.objects.get(id=idUsuario, sesion_sico=sesion),
            estadoRetorno=True
        )
        movilBusqueda = SW_buscar(sesion)
        if movilBusqueda:
            busc.save()
            return movilBusqueda.busquedaIntegrada(tipo, dato)
        return ''

sw_busquedas = DjangoSoapApp([SW_Busquedas], __name__)