# coding=utf-8
# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from soaplib.serializers import primitive
from soaplib.service import DefinitionBase, rpc
from handler import DjangoSoapApp

#servicio web de ejemplo
from usuarios.views import ingreso, integracion, cerrarSico


class HelloWorldService(DefinitionBase):
    @rpc(primitive.String, primitive.Integer, _returns=primitive.String)
    def say_hello(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s ' % name)
        return str(results)
hello_world_service = DjangoSoapApp([HelloWorldService], 'HelloWorldService')



class SW_Usuarios(DefinitionBase):
    @rpc(primitive.String, primitive.String, _returns=primitive.String)
    def login(self, u, p):
        error = None

        user = authenticate(username=u, password=p)
        if user is not None:
            if user.is_active:
                if user.sesion_sico:
                    error = "El Usuario especificado ya esta en uso."
                else:
                    user.sesion_sico = (integracion(user.usuario_sico, user.contrasenia_sico)).activeConnection
                    user.save()
                    error = [
                        True,
                        user.id,
                        user.username,
                        user.sesion_sico
                    ]
        elif u and p:
            error = "Su Usuario o Contraseña no son correctos, Intentelo nuevamente."

        return str(error)


    @rpc(primitive.Integer, primitive.String, primitive.String, _returns=primitive.Boolean)
    def logout(self, id, u, s):

        user = User.objects.get(id=id, username=u, sesion_sico=s)
        if user:
            cerrarSico(s)
            user.sesion_sico=''
            user.save()
            return True

        return False


# the view to use in urls.py
sw_usuario = DjangoSoapApp([SW_Usuarios], __name__)