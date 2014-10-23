__author__ = 'Andreita'

#
#from soaplib.wsgi_soap import SimpleWSGISoapApp
#from soaplib.service import soapmethod
#from soaplib.serializers import primitive as soap_types
#
#from django.http import HttpResponse
#
#
#class DjangoSoapApp(SimpleWSGISoapApp):
#
#    #noinspection PyMethodOverriding
#    def __call__(self, request):
#        django_response = HttpResponse()
#        def start_response(status, headers):
#            status, reason = status.split(' ', 1)
#            django_response.status_code = int(status)
#            for header, value in headers:
#                django_response[header] = value
#        response = super(SimpleWSGISoapApp, self).__call__(request.META, start_response)
#        django_response.content = "\n".join(response)
#
#        return django_response


#from soaplib.wsgi_soap import SimpleWSGISoapApp
#from soaplib.service import soapmethod
#from soaplib.serializers import primitive as soap_types
#import StringIO
#
#from django.http import HttpResponse
#
#class DumbStringIO(StringIO.StringIO):
#    #noinspection PyMethodOverriding
#    def read(self, n):
#        return self.getvalue()
#
#class DjangoSoapApp(SimpleWSGISoapApp):
#    csrf_exempt = True
#    #noinspection PyMethodOverriding
#    def __call__(self, request):
#
#        django_response = HttpResponse()
#        def start_response(status, headers):
#            status, reason = status.split(' ', 1)
#            django_response.status_code = int(status)
#            for header, value in headers:
#                django_response[header] = value
#
#        environ = request.META.copy()
#        body = ''.join(['%s=%s' % v for v in request.POST.items()])
#        environ['CONTENT_LENGTH'] = len(body)
#        environ['wsgi.input'] = DumbStringIO(body)
#        environ['wsgi.multithread'] = False
#
#        response = super(DjangoSoapApp, self).__call__(environ, start_response)
#
#        django_response.content = "\n".join(response)
#
#        return django_response



from soaplib.serializers.primitive import Boolean, String
from soaplib.service import DefinitionBase, rpc
from soaplib.wsgi import Application

from django.http import HttpResponse


# the class which acts as a wrapper between soaplib WSGI functionality and Django
class DjangoSoapApp(Application):
    csrf_exempt = True

    #noinspection PyMethodOverriding
    def __call__(self, request):
        # wrap the soaplib response into a Django response object
        django_response = HttpResponse()
        def start_response(status, headers):
            status, reason = status.split(' ', 1)
            django_response.status_code = int(status)
            for header, value in headers:
                django_response[header] = value
        response = super(DjangoSoapApp, self).__call__(request.META, start_response)
        django_response.content = '\n'.join(response)
        django_response.csrf_exempt = True
        return django_response


