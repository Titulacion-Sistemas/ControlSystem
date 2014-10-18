from django.contrib import admin

# Register your models here.
from ingresos.models import *

admin.site.register(medidor)
admin.site.register(cliente)
admin.site.register(detalleClienteMedidor)
admin.site.register(provincia)
admin.site.register(canton)
admin.site.register(sector)
admin.site.register(ruta)
admin.site.register(secuencia)