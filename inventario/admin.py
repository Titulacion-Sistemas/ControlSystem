from django.contrib import admin

# Register your models here.
from inventario.models import *


class detalleMaterialContratoAdmin(admin.ModelAdmin):


    fieldsets = (
        (None, {'fields': (
            'material',
            'contrato',
            'stock',
            'unidad',
            'proporcionado'
        )}),


    )

    def save_model(self, request, obj, form, change):
        print 'SaveModel : '+str(obj)
        pass





admin.site.register(contrato)
admin.site.register(marca)
admin.site.register(medidor)
admin.site.register(sello)
admin.site.register(subtipoDeMaterial)
admin.site.register(tipoDeMaterial)
admin.site.register(material)
admin.site.register(detalleMaterialContrato, detalleMaterialContratoAdmin)
admin.site.register(servicio)
admin.site.register(rubro)
admin.site.register(detalleRubro)
admin.site.register(rangoDeMaterial)
