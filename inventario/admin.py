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

    def crearMateriales(self, MATERIALES, obj):
        stok = int(obj.stock)
        for t in MATERIALES:
            print 'Agregando material ' + str(t[1]) + ' ' + t[0] + ' de Kit...'
            dmc = detalleMaterialContrato.objects.filter(
                material=subtipoDeMaterial.objects.filter(claveEnSico=t[0])[0],
                contrato=obj.contrato,
                proporcionado=obj.proporcionado
            )
            if len(dmc) > 0:
                dmc = dmc[0]
                dmc.stock = dmc.stock + (t[1] * stok)
            else:
                dmc = detalleMaterialContrato(
                    material=subtipoDeMaterial.objects.filter(claveEnSico=t[0])[0],
                    contrato=obj.contrato,
                    stock=t[1] * stok,
                    unidad='Unidade(s)',
                    proporcionado=obj.proporcionado
                )
            dmc.save()

    def save_model(self, request, obj, form, change):
        print obj.material
        d = '%s%s%s' % (
            obj.material.tipoDeMaterial.material.descripcion,
            obj.material.tipoDeMaterial.descripcion,
            obj.material.descripcion
        )
        if d == 'KIT DE ACOMETIDA 120':
            print 'Agregando materiales de Kit de 120...'
            MATERIALES = (
                ('037012150', 2),
                ('037015100', 1),
                ('023520630', 1),
                ('037027500', 1),
                ('037009100', 2),
                ('031018100', 2),
                ('037018500', 2),
                ('037021120', 8)
            )
            self.crearMateriales(MATERIALES, obj)
        elif d == 'KIT DE ACOMETIDA 240':
            print 'Agregando materiales de Kit de 240...'
            MATERIALES = (
                ('037012150', 3),
                ('037015100', 1),
                ('023520630', 2),
                ('037027500', 2),
                ('037009100', 2),
                ('037018100', 1),
                ('037018500', 1),
                ('037021120', 8)
            )
            self.crearMateriales(MATERIALES, obj)

        dmc = detalleMaterialContrato.objects.filter(
            material=obj.material,
            contrato=obj.contrato,
            proporcionado=obj.proporcionado
        )
        if len(dmc) > 0:
            dmc = dmc[0]
            dmc.stock = dmc.stock + obj.stock
            obj = dmc
        obj.save()


class medidorAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        ini = int(obj.fabrica)
        fin = int(obj.fabricaFinal)
        material = obj.contrato

        if fin > ini:
            tmp = obj.serie
            print 'Guardando rango ...'
            for i in range(ini+1, fin + 1):
                if not medidor.objects.filter(fabrica=str(i), contrato=obj.contrato):
                    print 'Guardando rango id:' + str(obj.id) + ' medidor: ' + str(i) + ' => ' + str(obj.fabricaFinal)

                    medtmp = medidor(
                        fabrica=str(i),
                        contrato=obj.contrato,
                        fabricaFinal=obj.fabricaFinal,
                        serie=tmp,
                        marca=obj.marca,
                        tipo=obj.tipo,
                        digitos=obj.digitos,
                        hilos=obj.hilos,
                        fases=obj.fases,
                        voltaje=obj.voltaje,
                        est=obj.est,
                        modelo=obj.modelo
                    )
                    material.stock = int(material.stock) + 1
                    medtmp.save()

                    try:
                        tmp = tmp.split('-')
                        tmp = '%s-%s' % (str(tmp[0]), str(int(tmp[1]) + 1))
                        print tmp
                    except:
                        pass

                else:
                    print 'Medidor  ' + str(i) + ' ya existe... '

        if not medidor.objects.filter(fabrica=obj.fabrica, contrato=obj.contrato):
            material.stock = int(material.stock) + 1
        material.save()
        obj.save()


class selloAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        ini = int(obj.numero)
        fin = int(obj.finalNumero)
        material = obj.detalleMaterialContrato

        if fin > ini:

            print 'Guardando rango ...'
            for i in range(ini+1, fin+1):
                if not sello.objects.filter(numero=str(i), utilizado=obj.utilizado):
                    print 'Guardando rango sello: ' + str(i) + ' => ' + str(fin)

                    setmp = sello(
                        detalleMaterialContrato=obj.detalleMaterialContrato,
                        utilizado=obj.utilizado,
                        numero=str(i),
                        finalNumero=fin,
                        color=obj.color,
                        ubicacion=obj.ubicacion,
                        estado=obj.estado
                    )
                    material.stock = int(material.stock) + 1
                    setmp.save()

                else:
                    print 'Medidor  ' + str(i) + ' ya existe... '

        if not sello.objects.filter(numero=obj.numero, utilizado=obj.utilizado):
            material.stock = int(material.stock) + 1
        material.save()
        obj.save()


admin.site.register(contrato)
admin.site.register(marca)
admin.site.register(medidor, medidorAdmin)
admin.site.register(sello, selloAdmin)
admin.site.register(subtipoDeMaterial)
admin.site.register(tipoDeMaterial)
admin.site.register(material)
admin.site.register(detalleMaterialContrato, detalleMaterialContratoAdmin)
admin.site.register(servicio)
admin.site.register(rubro)
admin.site.register(detalleRubro)
admin.site.register(colorDeSello)
