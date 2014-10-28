from django.contrib import admin

# Register your models here.
from usuarios.models import *


class ContratoAdmin(admin.ModelAdmin):
    pass

admin.site.register(contrato)
admin.site.register(usuarioSico)