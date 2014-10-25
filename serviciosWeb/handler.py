
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


