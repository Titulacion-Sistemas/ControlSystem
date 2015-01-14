# coding=utf-8

from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from usuarios.views import *
from serviciosWeb.views import *
from ingresos.views import ListaDeIngreso
from ingresos.views import ListaDeFotos

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ControlSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Pruebas
    url(r'^signup$', 'usuarios.views.signup', name='signup'),
    url(r'^multiply', multiply),

    #Administración
    url(r'^admin/', include(admin.site.urls)),

    #Usuarios
    url(r'^$', 'usuarios.views.main', name='main'),
    url(r'^login$', "usuarios.views.ingreso", name='login'),
    url(r'^logout$', 'usuarios.views.salir', name="logout"),
    url(r'^home$', 'usuarios.views.home', name='home'),
    url(r'^perfil$', 'usuarios.views.perfil', name='perfil'),
    url(r'^password', 'usuarios.views.password', name='password'),
    url(r'^change_done', 'usuarios.views.my_password_change_done', name='change_done'),
    url(r'^acercade$', 'usuarios.views.acercade', name='acercade'),


    #Búsquedas
    url(r'^buscar/1$', 'busquedas.views.cuenta', name='buscarCuenta'),
    url(r'^buscar/2$', 'busquedas.views.medidor', name='buscarMedidor'),
    url(r'^buscar/3$', 'busquedas.views.nombre', name='buscarNombre'),
    url(r'^buscar/4$', 'busquedas.views.geocodigo', name='buscarGeocodigo'),
    url(r'^busqueda$', 'busquedas.views.busqueda', name='busqueda'),

    #Fotos
    url(r'^listadefotos$', ListaDeFotos.as_view(), name='listadefotos'),
    url(r'^fotos/(?P<pk>\d+)/$', 'ingresos.views.fotos', name='fotos'),
    url(r'^borrarfoto/(?P<pk>\d+)/$', 'ingresos.views.borrarFoto', name='borrarfoto'),

    #Mapas
    url(r'^cuadrillas$', 'usuarios.views.cuadrillas', name='cuadrillas'),
    url(r'^mascuadrillas$', 'usuarios.views.masCuadrillas', name='mascuadrillas'),

    #Reportes
    url(r'^reportes$', 'usuarios.views.reportes', name='reportes'),
    url(r'^reportesmateriales$', 'usuarios.views.reporteMateriales', name='reportesmateriales'),
    url(r'^reportesactividades$', 'usuarios.views.reporteActividades', name='reportesactividades'),

    #Ingresos
    url(r'^ingresarsico$', 'ingresos.views.ingresarSico', name='ingresarSico'),
    url(r'^breferencia', 'ingresos.views.buscarReferencia', name='buscarReferencia'),
    url(r'^bcliente', 'ingresos.views.buscarCliente', name='buscarClienteIngreso'),
    url(r'^bmedidor', 'ingresos.views.buscarMedidor', name='buscarMedidorIngreso'),
    url(r'^guardaringreso', 'ingresos.views.guardarIngreso', name='guardarIngreso'),
    url(r'^ingreso/(?P<pk>\d+)/$', 'ingresos.views.ingreso', name='ingreso'),
    url(r'^eliminaringreso/(?P<pk>\d+)/$', 'ingresos.views.eliminarIngreso', name='eliminaringreso'),
    url(r'^listadeingresos$', ListaDeIngreso.as_view(), name='listadeingresos'),

    #Avance de Obra
    url(r'^avance$', 'ingresos.views.avance', name='avance'),

    #Estados de ingreso
    url(r'^continuaringreso/(?P<pk>\d+)/(?P<estado>\d+)/$', 'ingresos.views.continuar', name='continuaringreso'),

    #Servicios Web
    (r"^hello_world/", 'serviciosWeb.views.hello_world_service'),
    (r'^hello_world/service.wsdl', 'serviciosWeb.views.hello_world_service'),
    (r'^sw/usuarios', 'serviciosWeb.views.sw_usuarios'),
    (r'^sw/usuarios.wsdl', 'serviciosWeb.views.sw_usuarios'),
    (r'^sw/busquedas', 'serviciosWeb.views.sw_busquedas'),
    (r'^sw/busquedas.wsdl', 'serviciosWeb.views.sw_busquedas'),
    (r'^sw/ingresos', 'serviciosWeb.views.sw_ingresos'),
    (r'^sw/ingresos.wsdl', 'serviciosWeb.views.sw_ingresos'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)