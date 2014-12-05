# coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
from usuarios.views import multiply

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ControlSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Administración
    url(r'^admin/', include(admin.site.urls)),

    #Usuarios
    url(r'^$', 'usuarios.views.main', name='main'),
    url(r'^login$', "usuarios.views.ingreso", name='login'),
    url(r'^logout$', 'usuarios.views.salir', name="logout"),
    url(r'^signup$', 'usuarios.views.signup', name='signup'),
    url(r'^home$', 'usuarios.views.home', name='home'),

    #Búsquedas
    url(r'^buscar/1$', 'busquedas.views.cuenta', name='buscarCuenta'),
    url(r'^buscar/2$', 'busquedas.views.medidor', name='buscarMedidor'),
    url(r'^buscar/3$', 'busquedas.views.nombre', name='buscarNombre'),
    url(r'^buscar/4$', 'busquedas.views.geocodigo', name='buscarGeocodigo'),
    url(r'^busqueda$', 'busquedas.views.busqueda', name='busqueda'),

    url(r'^multiply', multiply),

    #Ingresos
    url(r'^ingresarsico$', 'ingresos.views.ingresarSico', name='ingresarSico'),
    url(r'^breferencia', 'ingresos.views.buscarReferencia', name='buscarReferencia'),
    url(r'^bcliente', 'ingresos.views.buscarCliente', name='buscarCliente'),
    url(r'^bmedidor', 'ingresos.views.buscarMedidor', name='buscarMedidor'),
    url(r'^guardaringreso', 'ingresos.views.guardarIngreso', name='guardarIngreso'),
    url(r'^ingreso/(?P<pk>\d+)/$', 'ingresos.views.ingreso', name='ingreso'),

    #Servicios Web
    (r"^hello_world/", 'serviciosWeb.views.hello_world_service'),
    (r'^hello_world/service.wsdl', 'serviciosWeb.views.hello_world_service'),
    (r'^sw/usuarios', 'serviciosWeb.views.sw_usuarios'),
    (r'^sw/usuarios.wsdl', 'serviciosWeb.views.sw_usuarios'),
    (r'^sw/busquedas', 'serviciosWeb.views.sw_busquedas'),
    (r'^sw/busquedas.wsdl', 'serviciosWeb.views.sw_busquedas'),
)