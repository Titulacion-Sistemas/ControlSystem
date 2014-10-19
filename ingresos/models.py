# coding=utf-8
from django.db import models

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


class sector(models.Model):
    num = models.PositiveSmallIntegerField(max_length=2)
    descripcion = models.CharField(max_length=40, verbose_name='Nombre de Sector', blank=True, null=True, default='')
    canton = models.ForeignKey(canton, verbose_name='Nombre de Cantón')

    def __unicode__(self):
        return self.descirpcion


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


class marca(models.Model):
    id = models.CharField(max_length=3, primary_key=True, verbose_name='Abreviatura')
    descripcion = models.CharField(max_length=25, verbose_name="Nombre")

    def __unicode__(self):
        return self.descripcion


class medidor(models.Model):

    VOLT = (
        (120, 120),
        (240, 240),
    )

    fabrica = models.CharField(max_length=11, verbose_name='Número de fábrica')
    serie = models.CharField(max_length=9, verbose_name='Numero de serie')
    marca = models.ForeignKey(marca, verbose_name='Marca')
    voltaje = models.PositiveSmallIntegerField(choices=VOLT)
    est = models.BooleanField(default=True)

    def __unicode__(self):
        return self.fabrica

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
    direccion = models.CharField(max_length=50, verbose_name='Dirección')
    tipo = models.CharField(max_length=1, choices=PERSONA, default='N')
    estado = models.CharField(max_length=20, verbose_name="Estado")

    def __unicode__(self):
        return self.cuenta


class detalleClienteMedidor(models.Model):
    lectura_instalacion = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Lectura de instalación')
    lectura_desinstalacion = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Lectura de desinstalación')
    fecha_instalacion = models.DateField(verbose_name='Fecha de instalación')
    fecha_desinstalacion = models.DateField(verbose_name='Fecha de desinstalación')
    medidor = models.ForeignKey(medidor, verbose_name='Medidor')
    cliente = models.ForeignKey(cliente, verbose_name='Cliente')

    def __unicode__(self):
        return '%s - %s' % (self.cliente, self.medidor)