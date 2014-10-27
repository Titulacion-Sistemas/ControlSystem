from django.contrib import admin

# Register your models here.
from usuarios.models import contrato

class ContratoAdmin(admin.ModelAdmin):
    pass

admin.site.register(contrato)