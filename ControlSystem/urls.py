# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from usuarios.views import multiply
from ingresos.views import ListaDeIngreso
from serviciosWeb.views import *

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
    url(r'^eliminaringreso/(?P<pk>\d+)/$', 'ingresos.views.eliminarIngreso', name='eliminaringreso'),
    url(r'^listadeingresos$', ListaDeIngreso.as_view(), name='listadeingresos'),
    url(r'^fotos/(?P<pk>\d+)/$', 'ingresos.views.fotos', name='fotos'),
    url(r'^borrarfoto/(?P<pk>\d+)/$', 'ingresos.views.borrarFoto', name='borrarfoto'),

    #Servicios Web
    (r"^hello_world/", 'serviciosWeb.views.hello_world_service'),
    (r'^hello_world/service.wsdl', 'serviciosWeb.views.hello_world_service'),
    (r'^sw/usuarios', 'serviciosWeb.views.sw_usuarios'),
    (r'^sw/usuarios.wsdl', 'serviciosWeb.views.sw_usuarios'),
    (r'^sw/busquedas', 'serviciosWeb.views.sw_busquedas'),
    (r'^sw/busquedas.wsdl', 'serviciosWeb.views.sw_busquedas'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)