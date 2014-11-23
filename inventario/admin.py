from django.contrib import admin

# Register your models here.
from inventario.models import *


admin.site.register(contrato)
admin.site.register(marca)
admin.site.register(medidor)
admin.site.register(sello)
admin.site.register(subtipoDeMaterial)
admin.site.register(tipoDeMaterial)
admin.site.register(material)
admin.site.register(detalleMaterialContrato)
admin.site.register(servicio)
admin.site.register(rubro)
admin.site.register(detalleRubro)
