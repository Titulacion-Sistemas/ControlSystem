from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.views import logout
from busqueda.views import busqueda
from usuarios.views import multiply

from django.contrib.auth.views import login

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ControlSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'usuarios.views.main', name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', "usuarios.views.ingreso", name='login'),
    url(r'^logout$', 'usuarios.views.salir', name="logout"),
    url(r'^signup$', 'usuarios.views.signup', name='signup'),
    url(r'^buscar/1$', 'busqueda.views.cuenta', name='buscarCuenta'),
    url(r'^buscar/2$', 'busqueda.views.medidor', name='buscarMedidor'),
    url(r'^buscar/3$', 'busqueda.views.nombre', name='buscarNombre'),
    url(r'^buscar/4$', 'busqueda.views.geocodigo', name='buscarGeocodigo'),
    url(r'^busqueda$', 'busqueda.views.busqueda', name='busqueda'),
    url(r'^home$', 'usuarios.views.home', name='home'),
    url(r'^multiply', multiply),
)