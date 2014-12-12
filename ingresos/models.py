# coding=utf-8
import os
from django.db import models
from inventario.models import material, sello

# Create your models here.


class provincia(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, max_length=2)
    descripcion = models.CharField(max_length=20, verbose_name='Nombre de Provincia', blank=True, null=True, default='')

    def __unicode__(self):
        return self.descripcion


class canton(models.Model):
    num = models.PositiveSmallIntegerField(max_length=2)
    descripcion = models.CharField(max_length=30, verbose_name='Nombre de Cantón', blank=True, null=True, default='')
    provincia = models.ForeignKey(provincia, verbose_name='Nombre de Provincia')

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Cantones"

class parroquia(models.Model):
    num = models.PositiveSmallIntegerField(max_length=3)
    descripcion = models.CharField(max_length=40, verbose_name='Nombre de Parroquia')
    canton = models.ForeignKey(canton, verbose_name='Nombre de Cantón', blank=True, null=True, default='')

    def __unicode__(self):
        return self.descripcion

class sector(models.Model):
    num = models.PositiveSmallIntegerField(max_length=2)
    descripcion = models.CharField(max_length=40, verbose_name='Nombre de Sector', blank=True, null=True, default='')
    canton = models.ForeignKey(canton, verbose_name='Nombre de Cantón')

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Sectores"


class ruta(models.Model):
    num = models.PositiveSmallIntegerField(max_length=3)
    descripcion = models.CharField(max_length=30, verbose_name='Nombre de Ruta', blank=True, null=True, default='')
    sector = models.ForeignKey(sector, verbose_name='Nombre de Sector')

    def __unicode__(self):
        return self.descripcion


class secuencia(models.Model):
    num = models.IntegerField()
    descripcion = models.CharField(max_length=30, verbose_name='Nombre de Secuencia', blank=True, null=True, default='')
    ruta = models.ForeignKey(ruta, verbose_name='Nombre de Ruta')

    def __unicode__(self):
        return '%02d.%02d.%02d.%03d.%07d' % (
            self.ruta.sector.canton.provincia_id,
            self.ruta.sector.canton.num,
            self.ruta.sector.num,
            self.ruta.num,
            self.num
        )

    class Meta:
        verbose_name_plural="Geocodigos"
        verbose_name='Geocódigo'

class cliente(models.Model):
    PERSONA = (
        ('N', 'Persona Natural'),
        ('J', 'Persona Jurídica'),
    )
    ci_ruc = models.CharField(max_length=13, verbose_name='Ruc / Cédula')
    cuenta = models.CharField(max_length=7, null=False, blank=True, default='S/N')
    nombre = models.CharField(max_length=50, verbose_name='Abonado')
    deuda = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Deuda del abonado', blank=True, null=True, default=0)
    meses = models.PositiveSmallIntegerField(verbose_name='Meses adeudados', blank=True, null=True, default=0)
    geocodigo = models.OneToOneField(secuencia, verbose_name='Geocódigo', blank=True, null=True, default=None)
    ubicacionGeografica=models.ForeignKey('ubicacion', verbose_name='Ubicación geográfica', blank=True, null=True, default=None)
    telefono = models.CharField(max_length=10, verbose_name='Teléfono o Celular', blank=True, null=True, default='N/A')
    tipo = models.CharField(max_length=1, choices=PERSONA, default='N')
    estado = models.CharField(max_length=20, verbose_name="Estado", default='S/N')

    def __unicode__(self):
        return self.cuenta

    def save(self, *args, **kwargs):
        if self.geocodigo is not None:
            try:
                p = provincia.objects.get(
                    id=self.geocodigo.ruta.sector.canton.provincia.id,
                    descripcion=self.geocodigo.ruta.sector.canton.provincia.descripcion
                )
            except Exception as e:
                print e.message
                p = provincia(
                    id=self.geocodigo.ruta.sector.canton.provincia.id,
                    descripcion=self.geocodigo.ruta.sector.canton.provincia.descripcion
                )
                print 'BD : Guardando Provincia...'
                p.save()
            try:
                c = canton.objects.get(
                    num=self.geocodigo.ruta.sector.canton.num,
                    descripcion=self.geocodigo.ruta.sector.canton.descripcion,
                )
            except Exception as e:
                print e.message
                c = canton(
                    num=self.geocodigo.ruta.sector.canton.num,
                    descripcion=self.geocodigo.ruta.sector.canton.descripcion,
                    provincia=p
                )
                print 'BD : Guardando Canton...'
                c.save()
            try:
                sec=sector.objects.get(
                    num=self.geocodigo.ruta.sector.num,
                    descripcion=self.geocodigo.ruta.sector.descripcion,
                )
            except Exception as e:
                print e.message
                sec=sector(
                    num=self.geocodigo.ruta.sector.num,
                    descripcion=self.geocodigo.ruta.sector.descripcion,
                    canton=c
                )
                print 'BD : Guardando Sector...'
                sec.save()
            try:
                rut = ruta.objects.get(
                    num=self.geocodigo.ruta.num,
                    descripcion=self.geocodigo.ruta.descripcion,
                )
            except Exception as e:
                print e.message
                rut = ruta(
                    num=self.geocodigo.ruta.num,
                    descripcion=self.geocodigo.ruta.descripcion,
                    sector=sec
                )
                print 'BD : Guardando Ruta...'
                rut.save()
            print self.geocodigo.num
            try:
                geo = secuencia.objects.get(
                    num=self.geocodigo.num,
                    ruta=rut
                )
            except Exception as e:
                print e.message
                geo = secuencia(
                    num=self.geocodigo.num,
                    ruta=rut
                )
                print 'BD : Guardando Secuencia...'
                geo.save()

            self.geocodigo=geo

        if self.ubicacionGeografica is not None:

            try:
                parr=parroquia.objects.get(
                    num=self.ubicacionGeografica.parroquia.num,
                    descripcion=self.ubicacionGeografica.parroquia.descripcion,
                )
            except Exception as e:
                print e.message
                parr = parroquia(
                    num=self.ubicacionGeografica.parroquia.num,
                    descripcion=self.ubicacionGeografica.parroquia.descripcion,
                    canton=c
                )
                print 'BD : Guardando Parroquia...'
                parr.save()

            tipCall=None
            if self.ubicacionGeografica.calle.descripcion1[2]==' ':
                try:
                    tipCall=tipoCalle.objects.get(
                        id=self.ubicacionGeografica.calle.descripcion1[:2]
                    )
                    print 'BD : Asignada Tipo de Calle'
                except Exception as e:
                    print e.message
                    tipCall=tipoCalle(
                        id=self.ubicacionGeografica.calle.descripcion1[:2],
                        descripcion=self.ubicacionGeografica.calle.descripcion1[3:]
                    )
                    self.ubicacionGeografica.calle.descripcion1=self.ubicacionGeografica.calle.descripcion1[3:]
                    print 'BD : Guardando Tipo de Calle (Calle)...'
                    tipCall.save()
                    self.ubicacionGeografica.calle.descripcion1=tipCall.descripcion

            try:
                call=calle.objects.get(
                    tipoDeCalle=tipCall,
                    descripcion1=self.ubicacionGeografica.calle.descripcion1
                )
                print 'BD : Asignada Calle'
            except Exception as e:
                print e.message
                call=calle(
                    tipoDeCalle=tipCall,
                    descripcion1=self.ubicacionGeografica.calle.descripcion1
                )
                print 'BD : Guardando Calle...'
                call.save()

            tipCall=None
            if len(self.ubicacionGeografica.interseccion.descripcion1)>0 and self.ubicacionGeografica.interseccion.descripcion1[2]==' ':
                try:
                    tipCall=tipoCalle.objects.get(
                        id=self.ubicacionGeografica.interseccion.descripcion1[:2]
                    )
                    print 'BD : Asignada Tipo de Calle(I)'
                except Exception as e:
                    print e.message
                    tipCall=tipoCalle(
                        id=self.ubicacionGeografica.interseccion.descripcion1[:2],
                        descripcion=
                        self.ubicacionGeografica.interseccion.descripcion1[3:len(self.ubicacionGeografica.interseccion.descripcion1)]
                    )
                    print 'BD : Guardando Tipo de Calle (Interseccion)...'
                    tipCall.save()
                    self.ubicacionGeografica.interseccion.descripcion1=tipCall.descripcion
            try:
                inter=calle.objects.get(
                    tipoDeCalle=tipCall,
                    descripcion1=self.ubicacionGeografica.interseccion.descripcion1
                )
                print 'BD : Asignada Calle(I)'
            except Exception as e:
                print e.message
                inter=calle(
                    tipoDeCalle=tipCall,
                    descripcion1=self.ubicacionGeografica.interseccion.descripcion1
                )
                print 'BD : Guardando Interseccion...'
                inter.save()

            urb=None
            if self.ubicacionGeografica.urbanizacion is not None:
                print '='+str(self.ubicacionGeografica.urbanizacion.descripcion.strip())+'='
                if self.ubicacionGeografica.urbanizacion:
                    if len(self.ubicacionGeografica.urbanizacion.descripcion.strip())>0:
                        try:
                            urb=urbanizacion.objects.get(descripcion=self.ubicacionGeografica.urbanizacion.descripcion)
                            print 'BD : Asignada Urbanizacion'
                        except Exception as e:
                            print e.message
                            urb = urbanizacion(descripcion=self.ubicacionGeografica.urbanizacion.descripcion)
                            print 'BD : Guardando Urbanizacion...'
                            urb.save()

            try:
                ubi=ubicacion.objects.get(
                    parroquia=parr, calle=call,
                    interseccion=inter, urbanizacion=urb
                )
            except Exception as e:
                print e.message
                ubi=ubicacion(
                    parroquia=parr, calle=call,
                    interseccion=inter, urbanizacion=urb
                )
            print 'BD : Guardando Ubicacion...'
            ubi.save()

            self.ubicacionGeografica=ubi
            print self.geocodigo

        try:
            self.id = cliente.objects.get(id=self.id).id
            print 'Actualizar por ID'
            super(cliente, self).save(force_update=True, *args, **kwargs)
        except Exception as e:
            print e.message
            try:
                self.id = cliente.objects.get(cuenta=str(self.cuenta)).id
                print 'Actualizar por CTA'
                super(cliente, self).save(force_update=True, *args, **kwargs)
            except Exception as e:
                print e.message
                print 'Gurdar Cliente'
                super(cliente, self).save(*args, **kwargs)

        print 'BD : Guardado Completo...'


class detalleClienteMedidor(models.Model):
    lectura_instalacion = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Lectura de instalación', null=True)
    lectura_desinstalacion = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Lectura de desinstalación', null=True)
    fecha_instalacion = models.DateField(verbose_name='Fecha de instalación', null=True)
    fecha_desinstalacion = models.DateField(verbose_name='Fecha de desinstalación', null=True)
    medidor = models.ForeignKey('inventario.medidor', verbose_name='Medidor')
    cliente = models.ForeignKey(cliente, verbose_name='Cliente')
    observacion=models.CharField(max_length=50, blank=True, null=True, default='')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.id = detalleClienteMedidor.objects.get(medidor=self.medidor, cliente=self.cliente).id
            super(detalleClienteMedidor, self).save(force_update=True)
            print 'Se Actualiza la relación Cliente - Medidor...'
        except Exception as e:
            print e.message
            super(detalleClienteMedidor, self).save()
            print 'Se Guarda la relación Cliente - Medidor...'

    def __unicode__(self):
        return '%s - %s' % (self.cliente, self.medidor)

    class Meta:
        verbose_name_plural="Detalles Cliente-Medidor"
        verbose_name='Detalle Cliente-Medidor'


class detalleClienteReferencia(models.Model):
    cliente=models.ForeignKey('cliente', related_name='cliente')
    referencia=models.ForeignKey('cliente', related_name='referencia')
    medidorDeReferencia=models.CharField(max_length=15)
    ubicacion=models.ForeignKey("ubicacion")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.id = detalleClienteReferencia.objects.get(cliente=self.cliente, referencia=self.referencia).id
            super(detalleClienteReferencia, self).save(force_update=True)
            print 'Se Actualiza la relación Cliente - Referencia...'
        except Exception as e:
            print e.message
            super(detalleClienteReferencia, self).save()
            print 'Se Guarda la relación Cliente - Referencia...'


    def __unicode__(self):
        return 'C:%s - R:%s' % (self.cliente, self.referencia)

class ubicacion(models.Model):
    parroquia=models.ForeignKey('parroquia')
    calle=models.ForeignKey('calle', verbose_name='Dirección o Calle', related_name='calle', blank=True, null=True, default='')
    interseccion=models.ForeignKey("calle", related_name='interseccion', blank=True, null=True, default='')
    urbanizacion=models.ForeignKey("urbanizacion", blank=True, null=True, default=None)
    caserio=models.ForeignKey("caserio", blank=True, null=True, default='')

    def __unicode__(self):
        return '%s; %s y %s; Urb: %s, Cas: %s' \
               % (self.parroquia,
                  self.calle,
                  self.interseccion,
                  self.urbanizacion,
                  self.caserio
        )

    class Meta:
        verbose_name_plural="Ubicaciones"
        verbose_name='Ubicación'


class caserio(models.Model):
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return self.descripcion

class urbanizacion(models.Model):
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Urbanizaciones"
        verbose_name='Urbanización'

class calle(models.Model):
    codigoDeCalle=models.CharField(max_length=6, blank=True, null=True, default='')
    descripcion1 = models.CharField(max_length=80)
    descripcion2 = models.CharField(max_length=80, blank=True, null=True, default='')
    tipoDeCalle = models.ForeignKey("tipoCalle", blank=True, null=True, default='')

    def __unicode__(self):
        return u'%s %s' % (self.descripcion1, self.descripcion2)

class tipoCalle(models.Model):
    id=models.CharField(max_length=2, primary_key=True, editable=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True, default='')

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Tipos de Calle"
        verbose_name='Tipo de Calle'



class actividad(models.Model):
    numeroDeSolicitud=models.CharField(max_length=10, verbose_name='Número de Solicitud', blank=True, null=True, default='')
    cliente=models.ForeignKey('cliente')
    tipoDeConstruccion=models.ForeignKey('tipoDeConstruccion')
    instalador=models.ForeignKey('instalador')
    ubicacionDelMedidor=models.ForeignKey('ubicacionDelMedidor')
    claseRed=models.ForeignKey('claseRed')
    nivelSocieconomico=models.ForeignKey('nivelSocieconomico', blank=True, null=True, default='')
    calibreDeLaRed=models.ForeignKey('calibreDeLaRed')
    estadoDeLaInstalacion=models.ForeignKey('estadoDeUnaInstalacion')
    tipoDeAcometidaRed=models.ForeignKey('tipoDeAcometidaRed', verbose_name='Tipo de Acometida o Red')
    fechaDeActividad=models.DateField(verbose_name='Fecha de Actividad', editable=True)
    horaDeActividad=models.TimeField(verbose_name='Hora de Actividad', editable=True)
    usoDeEnergia=models.ForeignKey('usoDeEnergia')
    usoEspecificoDelInmueble=models.ForeignKey('usoEspecificoDelInmueble')
    formaDeConexion=models.ForeignKey('formaDeConexion')
    demanda=models.ForeignKey('demanda')
    motivoDeSolicitud=models.ForeignKey('motivoParaSolicitud')
    tipoDeSolicitud=models.ForeignKey('tipoDeSolicitud')
    materialDeLaRed=models.ForeignKey('materialDeLaRed')
    estadoDeSolicitud=models.ForeignKey('estadoDeSolicitud', default=0)
    tipoDeServicio=models.ForeignKey('tipoDeServicio')
    observaciones=models.CharField(max_length=200, blank=True, null=True, default='')

    def __unicode__(self):
        return self.numeroDeSolicitud

    class Meta:
        verbose_name_plural="Actividades Realizadas"
        verbose_name='Actividad'





class estadoDeSolicitud(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=60)

    def __unicode__(self):
        return u'Estado %s : %s' % (str(self.id), self.descripcion)

    class Meta:
        verbose_name_plural="Estados de Solicitud"
        verbose_name='Estado de Solicitud'

class tipoDeConstruccion(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (str(self.id), self.descripcion)

    class Meta:
        verbose_name_plural="Tipos de Construcción"
        verbose_name='Tipo de Construcción'

class claseRed(models.Model):
    id=models.CharField(max_length=1, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return u'%s %s' % (str(self.id), self.descripcion)

    class Meta:
        verbose_name_plural="Clases de Red"
        verbose_name='Clase de Red'

class calibreDeLaRed(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return u'%d %s' % (self.id, self.descripcion)

    class Meta:
        verbose_name_plural="Calibres de Red"
        verbose_name='Calibre de Red'

class estadoDeUnaInstalacion(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return u'%d %s' % (self.id, self.descripcion)

    class Meta:
        verbose_name_plural="Estados posibles de una Instalación"
        verbose_name='Estado de una Instalación'

class tipoDeAcometidaRed(models.Model):
    id=models.CharField(max_length=2, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.descripcion)

    class Meta:
        verbose_name_plural="Tipos de Acometida o Red"
        verbose_name='Tipo de Acometida o Red'

class usoDeEnergia(models.Model):
    id=models.CharField(max_length=2, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.descripcion)

    class Meta:
        verbose_name_plural="Usos de Energía"
        verbose_name='Uso de Energía'

class usoGeneralDelInmueble(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Usos Generales del Inmueble"
        verbose_name='Uso General del Inmueble'

class usoEspecificoDelInmueble(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    usoGeneral=models.ForeignKey('usoGeneralDelInmueble', verbose_name='Uso General del Inmueble')
    descripcion=models.CharField(max_length=50)

    def __unicode__(self):
        return u'%d %s %s' % (self.id, self.usoGeneral.descripcion, self.descripcion)

    class Meta:
        verbose_name_plural="Usos Específicos del Inmueble"
        verbose_name='Uso Específico del Inmueble'

class modeloDeMedidor(models.Model):
    id=models.CharField(max_length=7, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=50)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Modelos de Medidores"
        verbose_name='Modelo de Medidor'

class formaDeConexion(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=50)

    def __unicode__(self):
        return u'%d %s' % (self.id, self.descripcion)

    class Meta:
        verbose_name_plural="Formas de Conexión"
        verbose_name='Forma de Conexión'

class demanda(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=40)

    def __unicode__(self):
        return u'%s %s' % (str(self.id), self.descripcion)

class motivoParaSolicitud(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return u'%d %s' % (self.id, self.descripcion)

    class Meta:
        verbose_name_plural="Motivos para Solicitud"
        verbose_name='Motivo para Solicitud'

class tipoDeSolicitud(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return u'%d %s' % (self.id, self.descripcion)

    class Meta:
        verbose_name_plural="Tipos de Solicitud"
        verbose_name='Tipo de Solicitud'

class tipoDeServicio(models.Model):
    id=models.CharField(max_length=3, primary_key=True, verbose_name='Codigo')
    tension=models.CharField(max_length=15)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return u'%s %s' % (self.id, self.descripcion)

    class Meta:
        verbose_name_plural="Tipos de Servicio"
        verbose_name='Tipo de Servicio'

class ubicacionDelMedidor(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return u'%s %s' % (str(self.id), self.descripcion)

    class Meta:
        verbose_name_plural="Ubicaciones posibles de Medidor"
        verbose_name='Ubicación del Medidor'

class cuadrilla(models.Model):
    nombre=models.CharField(max_length=50)
    observacion=models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.nombre

class empleado(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    telefono=models.CharField(max_length=10, blank=True, null=True)
    correo=models.CharField(max_length=20, blank=True, null=True)
    observacion=models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (
            self.nombre,
            self.apellido
        )

class instalador(models.Model):
    nombre=models.ForeignKey('empleado')
    cuadrilla=models.ForeignKey('cuadrilla',blank=True, null=True, default='')
    observacion=models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name_plural='Instaladores'

class materialDeActividad(models.Model):
    material=models.ForeignKey('inventario.detalleMaterialContrato')
    actividad=models.ForeignKey('actividad')
    cantidad=models.BigIntegerField(default=1)
    observacion=models.CharField(max_length=50, blank=True, null=True, default='')

    def __unicode__(self):
        return u'%s' % self.material

    class Meta:
        verbose_name_plural='Materiales de cada Actividad'

class detalleDeActividad(models.Model):
    rubro=models.ForeignKey('inventario.detalleRubro')
    actividad=models.ForeignKey('actividad')

    def __unicode__(self):
        return '%s - %s' % (
            self.actividad,
            self.rubro
        )

    class Meta:
        verbose_name_plural='Rubros de la Actividad'
        verbose_name='Rubro de Actividad'


def destino(instance, filename):
    act=actividad.objects.get(id=instance.actividad.id)
    if len(act.cliente.cuenta)>4:
        dos= str(act.cliente.cuenta)
    else:
        dos= str(act.cliente.ci_ruc)
    return os.path.join('/%s/%s/' % (str(act.tipoDeSolicitud.descripcion), dos), filename)

class foto(models.Model):

    upload_to = '%s/%s/%s/%s'

    def _get_upload_to(self, filename):
        try:
            contrato = sello.objects.filter(utilizado=actividad)[0].detalleMaterialContrato.contrato.id
        except:
            contrato = 'Sin contrato'
        act=actividad.objects.get(id=self.actividad.id)
        if len(act.cliente.cuenta)>4:
            identificador= str(act.cliente.cuenta)
        else:
            identificador= str(act.cliente.ci_ruc)
        #return os.path.join('%s/%s' % (str(act.tipoDeSolicitud.descripcion), dos), filename)
        return self.upload_to % (str(contrato), str(act.tipoDeSolicitud.descripcion), identificador, filename)

    actividad=models.ForeignKey(actividad, blank=True, null=True)
    foto=models.FileField(upload_to=_get_upload_to)



    def __unicode__(self):
        return self.actividad

    class Meta:
        verbose_name_plural="Fotos de Actividad"
        verbose_name='Foto'

class nivelSocieconomico(models.Model):
    id=models.CharField(max_length=2, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=15)

    def __unicode__(self):
        return u'%s %s' % (str(self.id), self.descripcion)

    class Meta:
        verbose_name_plural="Niveles Socioeconómicos"
        verbose_name='Nivel Socioeconómico'

class materialDeLaRed(models.Model):
    id=models.CharField(max_length=2, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=15)

    def __unicode__(self):
        return u'%s %s' % (str(self.id), str(self.descripcion))

    class Meta:
        verbose_name_plural="Materiales de la Red"
        verbose_name='Material de la Red'


#class sistemaDeMedicion(models.Model):
#    pass
#
#    def __unicode__(self):
#        return None
#
#    class Meta:
#        verbose_name_plural=''


