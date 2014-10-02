from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth import logout
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
    url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),
    url(r'^home$', 'usuarios.views.home', name='home'),
    url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),
    url(r'^multiply', multiply),
)