# coding=utf-8
from django.db import models
from inventario.models import material

# Create your models here.


class provincia(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, max_length=2)
    descripcion = models.CharField(max_length=20, verbose_name='Nombre de Provincia', blank=True, null=True, default='')

    def __unicode__(self):
        return self.descirpcion


class canton(models.Model):
    num = models.PositiveSmallIntegerField(max_length=2)
    descripcion = models.CharField(max_length=30, verbose_name='Nombre de Cantón', blank=True, null=True, default='')
    provincia = models.ForeignKey(provincia, verbose_name='Nombre de Provincia')

    def __unicode__(self):
        return self.descirpcion

    class Meta:
        verbose_name_plural="Cantones"

class parroquia(models.Model):
    num = models.PositiveSmallIntegerField(max_length=3)
    descripcion = models.CharField(max_length=40, verbose_name='Nombre de Parroquia')
    canton = models.ForeignKey(canton, verbose_name='Nombre de Cantón', blank=True, null=True, default='')

    def __unicode__(self):
        return self.descirpcion

class sector(models.Model):
    num = models.PositiveSmallIntegerField(max_length=2)
    descripcion = models.CharField(max_length=40, verbose_name='Nombre de Sector', blank=True, null=True, default='')
    canton = models.ForeignKey(canton, verbose_name='Nombre de Cantón')

    def __unicode__(self):
        return self.descirpcion

    class Meta:
        verbose_name_plural="Sectores"


class ruta(models.Model):
    num = models.PositiveSmallIntegerField(max_length=3)
    descripcion = models.CharField(max_length=30, verbose_name='Nombre de Ruta', blank=True, null=True, default='')
    sector = models.ForeignKey(sector, verbose_name='Nombre de Sector')

    def __unicode__(self):
        return self.descirpcion


class secuencia(models.Model):
    num = models.PositiveSmallIntegerField(max_length=2)
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
    cuenta = models.CharField(max_length=7, null=False)
    nombre = models.CharField(max_length=50, verbose_name='Abonado')
    deuda = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Deuda del abonado')
    meses = models.PositiveSmallIntegerField(verbose_name='Meses adeudados')
    geocodigo = models.OneToOneField(secuencia, verbose_name='Geocódigo')
    ubicacionGeografica=models.OneToOneField('ubicacion', verbose_name='Ubicación geográfica')
    #direccion = models.CharField(max_length=50, verbose_name='Dirección')
    #interseccion = models.CharField(max_length=50, verbose_name='Intersección')
    #urbanizacion = models.CharField(max_length=50, verbose_name='Urbanización')
    tipo = models.CharField(max_length=1, choices=PERSONA, default='N')
    estado = models.CharField(max_length=20, verbose_name="Estado")

    def __unicode__(self):
        return self.cuenta


class detalleClienteMedidor(models.Model):
    lectura_instalacion = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Lectura de instalación')
    lectura_desinstalacion = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Lectura de desinstalación')
    fecha_instalacion = models.DateField(verbose_name='Fecha de instalación')
    fecha_desinstalacion = models.DateField(verbose_name='Fecha de desinstalación')
    medidor = models.ForeignKey('inventario.medidor', verbose_name='Medidor')
    cliente = models.ForeignKey(cliente, verbose_name='Cliente')
    observacion=models.CharField(max_length=50, blank=True, null=True, default='')

    def __unicode__(self):
        return '%s - %s' % (self.cliente, self.medidor)

    class Meta:
        verbose_name_plural="Detalles Cliente-Medidor"
        verbose_name='Detalle Cliente-Medidor'


class detalleClienteReferencia(models.Model):
    cliente=models.ForeignKey('cliente', related_name='cliente')
    referencia=models.ForeignKey('cliente', related_name='referencia')
    medidorDeReferencia=models.CharField(max_length=10)
    ubicacion=models.ForeignKey("ubicacion")

    def __unicode__(self):
        return 'C:%s - R:%s' % (self.cliente, self.referencia)

class ubicacion(models.Model):
    parroquia=models.ForeignKey('parroquia')
    calle=models.ForeignKey("calle", verbose_name='Dirección o Calle', related_name='calle', blank=True, null=True, default='')
    interseccion=models.ForeignKey("calle", related_name='interseccion', blank=True, null=True, default='')
    urbanizacion=models.ForeignKey("urbanizacion", blank=True, null=True, default='')
    caserio=models.ForeignKey("caserio", blank=True, null=True, default='')

    def __unicode__(self):
        return '%s; %s y %s; Urb: %s, Cas: %s' \
               % (self.parroquia,
                  self.calle,
                  self.intersepcion,
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
    descripcion = models.CharField(max_length=50)
    tipoDeCalle = models.ForeignKey("tipoCalle")

    def __unicode__(self):
        return self.descripcion

class tipoCalle(models.Model):
    descripcion = models.CharField(max_length=50, blank=True, null=True, default='')

    def __unicode__(self):
        return self.descripcion





class actividad(models.Model):
    numeroDeSolicitud=models.CharField(max_length=10, verbose_name='Número de Solicitud')
    cliente=models.ForeignKey('cliente')
    tipoDeConstruccion=models.ForeignKey('tipoDeConstruccion')
    materialDeRed=models.CharField(max_length=5, blank=True, null=True, default='')
    instalador=models.ForeignKey('instalador')
    ubicacionDelMedidor=models.ForeignKey('ubicacionDelMedidor')
    claseRed=models.ForeignKey('claseRed')
    nivelSocieconomico=models.ForeignKey('nivelSocieconomico', blank=True, null=True, default='')
    calibreDeLaRed=models.ForeignKey('calibreDeLaRed')
    estadoDeLaInstalacion=models.ForeignKey('estadoDeUnaInstalacion')
    tipoDeAcometidaRed=models.ForeignKey('tipoDeAcometidaRed', verbose_name='Tipo de Acometida o Red')
    fechaDeActividad=models.DateTimeField(verbose_name='Fecha y Hora de la Actividad', auto_now=True, auto_now_add=True)
    usoDeEnergia=models.ForeignKey('usoDeEnergia')
    usoEspecificoDelInmueble=models.ForeignKey('usoEspecificoDelInmueble')
    formaDeConexion=models.ForeignKey('formaDeConexion')
    demanda=models.ForeignKey('demanda')
    motivoDeSolicitud=models.ForeignKey('motivoParaSolicitud')
    tipoDeSolicitud=models.ForeignKey('tipoDeSolicitud')


    def __unicode__(self):
        return self.numeroDeSolicitud

    class Meta:
        verbose_name_plural="Actividades Realizadas"
        verbose_name='Actividad'



class tipoDeConstruccion(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=50)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Tipos de Construcción"
        verbose_name='Tipo de Construcción'

class claseRed(models.Model):
    id=models.CharField(max_length=1, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Clases de Red"
        verbose_name='Clase de Red'

class calibreDeLaRed(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Calibres de Red"
        verbose_name='Calibre de Red'

class estadoDeUnaInstalacion(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Estados posibles de una Instalación"
        verbose_name='Estado de una Instalación'

class tipoDeAcometidaRed(models.Model):
    id=models.CharField(max_length=2, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Tipos de Acometida o Red"
        verbose_name='Tipo de Acometida o Red'

class usoDeEnergia(models.Model):
    id=models.CharField(max_length=2, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

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
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Usos Específicos del Inmueble"
        verbose_name='Uso Específico del Inmueble'

class modeloDeMedidor(models.Model):
    id=models.CharField(max_length=6, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Modelos de Medidores"
        verbose_name='Modelo de Medidor'

class formaDeConexion(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=50)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Formas de Conexión"
        verbose_name='Forma de Conexión'

class demanda(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

class motivoParaSolicitud(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Motivos para Solicitud"
        verbose_name='Motivo para Solicitud'

class tipoDeSolicitud(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Tipos de Solicitud"
        verbose_name='Tipo de Solicitud'

class tipoDeServicio(models.Model):
    id=models.CharField(max_length=3, primary_key=True, verbose_name='Codigo')
    tension=models.CharField(max_length=15)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Tipos de Servicio"
        verbose_name='Tipo de Servicio'

class ubicacionDelMedidor(models.Model):
    id=models.PositiveSmallIntegerField(verbose_name='codigo', editable=True, primary_key=True)
    descripcion=models.CharField(max_length=25)

    def __unicode__(self):
        return self.descripcion

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
    telefono=models.CharField(max_length=10)
    correo=models.CharField(max_length=20)
    observacion=models.CharField(max_length=50)

    def __unicode__(self):
        return '%s %s' % 8(
            self.nombre,
            self.apellido
        )

class instalador(models.Model):
    nombre=models.ForeignKey('empleado')
    cuadrilla=models.ForeignKey('cuadrilla',blank=True, null=True, default='')
    observacion=models.CharField(max_length=50)

    def __unicode__(self):
        return '%s %s' % (self.nombre, self.apellido)

    class Meta:
        verbose_name_plural='Instaladores'

class materialDeActividad(models.Model):
    material=models.ForeignKey('inventario.detalleMaterialContrato')
    actividad=models.ForeignKey('actividad')
    cantidad=models.DecimalField(max_digits=4, decimal_places=2, default=1.00)
    observacion=models.CharField(max_length=50, blank=True, null=True, default='')

    def __unicode__(self):
        return self.material

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

class foto(models.Model):
    actividad=models.ForeignKey(actividad, blank=True, null=True)
    observacion=models.CharField(max_length=50, blank=True, null=True)
    ruta=models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.ruta

    class Meta:
        verbose_name_plural="Fotos de Actividad"
        verbose_name='Foto'

class nivelSocieconomico(models.Model):
    id=models.CharField(max_length=2, primary_key=True, verbose_name='Codigo')
    descripcion=models.CharField(max_length=15)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural="Niveles Socioeconómicos"
        verbose_name='Nivel Socioeconómico'

#class sistemaDeMedicion(models.Model):
#    pass
#
#    def __unicode__(self):
#        return None
#
#    class Meta:
#        verbose_name_plural=''