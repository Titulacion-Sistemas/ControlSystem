# Create your views here.
from soaplib.serializers import primitive
from soaplib.service import DefinitionBase, rpc
from handler import DjangoSoapApp

#servicio web de ejemplo
from usuarios.views import ingreso


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
        request = None
        request.POST['username'] = u
        request.POST['password'] = p
        request.POST = True
        data = ingreso(request)
        return str(data)


# the view to use in urls.py
sw_usuario = DjangoSoapApp([SW_Usuarios], __name__)