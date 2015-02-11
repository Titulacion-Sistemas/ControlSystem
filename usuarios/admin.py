from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from usuarios.models import *



admin.site.register(usuarioSico)
admin.site.register(posicion)
#admin.site.register(User)
#admin.site.register(Group)