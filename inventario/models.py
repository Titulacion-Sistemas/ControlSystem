# coding=utf-8
from django.db import models

# Create your models here.

class contrato(models.Model):
    num = models.CharField(max_length=10, primary_key=True, verbose_name='Número de Contrato')
    descripcion = models.CharField(max_length=150, verbose_name='Descripción')
    zonas = models.CharField(max_length=150, verbose_name='Zona(s)')
    codigoInstalador = models.PositiveSmallIntegerField(verbose_name='Código de Instalador')
    inicioVigencia = models.DateField(verbose_name='Vigente Desde')
    finalVigencia = models.DateField(verbose_name='Vigente Hasta')

    def __unicode__(self):
        return self.num


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

    contrato=models.ForeignKey('detalleMaterialContrato', blank=True, null=True, default='')
    fabrica = models.CharField(max_length=11, verbose_name='Número de Fábrica')
    fabricaFinal=models.CharField(max_length=11, verbose_name='Fin de rango de Medidores', blank=True, null=True, default='')
    serie = models.CharField(max_length=9, verbose_name='Numero de Serie')
    lectura=models.CharField(max_length=10, verbose_name='Lectura', blank=True, null=True, default='0')
    marca = models.ForeignKey(marca, verbose_name='Marca')
    tipo = models.CharField(max_length=15, verbose_name='Tipo de Medidor', blank=True, null=True, default='')
    digitos = models.PositiveSmallIntegerField(verbose_name='Dígitos')
    hilos = models.PositiveSmallIntegerField(verbose_name='Hilos')
    fases = models.PositiveSmallIntegerField(verbose_name='Fases')
    voltaje = models.PositiveSmallIntegerField(choices=VOLT)
    est = models.BooleanField(default=True)
    modelo=models.ForeignKey('ingresos.modeloDeMedidor', blank=True, null=True, default='')

    def __unicode__(self):
        return u'%s - ( %s ) - %s' % (self.fabrica, self.serie, self.marca.id)

    class Meta:
        verbose_name_plural='Medidores'



class colorDeSello(models.Model):
    color=models.CharField(max_length=20, verbose_name='Color de Sello')

    def __unicode__(self):
        return u'%s' % self.color

class sello(models.Model):
    UBICACIONES={
        ('Caja', 'Caja'),
        ('Bornera', 'Bornera'),
        ('Panel', 'Panel'),
        ('N/A', 'N/A'),
    }
    detalleMaterialContrato=models.ForeignKey('detalleMaterialContrato', verbose_name='Detalle de Material / Contrato')
    utilizado=models.ForeignKey('ingresos.actividad', verbose_name='Utilizado en actividad', blank=True, null=True, default=None)
    numero=models.CharField(max_length=10, verbose_name='Número de Sello')
    finalNumero=models.CharField(max_length=10, verbose_name='Fin de rango de Número de Sello', blank=True, null=True, default='')
    color=models.ForeignKey('colorDeSello', verbose_name='Color de Sello')
    ubicacion=models.CharField(max_length=10, choices=UBICACIONES, default='N/A')
    estado=models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return u'%s (%s)' % (
            self.numero,
            self.color.color
        )


class subtipoDeMaterial(models.Model):
    tipoDeMaterial=models.ForeignKey('tipoDeMaterial', verbose_name='Tipo de Material')
    claveEnSico=models.CharField(max_length=9, verbose_name='Clave de Sico', blank=True, null=True, default='')
    descripcion=models.CharField(max_length=35, verbose_name='Subtipo de Material')
    descargableDeSico=models.BooleanField(verbose_name='¿Se descarga para ingreso al Sistema SICO?', default=True)

    def __unicode__(self):
        return '%s%s%s' % (
            self.tipoDeMaterial.material.descripcion,
            self.tipoDeMaterial.descripcion,
            self.descripcion
        )

    class Meta:
        verbose_name_plural='Subtipos de Material'

class tipoDeMaterial(models.Model):
    material=models.ForeignKey('material', verbose_name='Material')
    descripcion=models.CharField(max_length=30, verbose_name='Tipo de Material')

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural='Tipos de Material'

class material(models.Model):

    VOLT = (
        (120, 120),
        (240, 240),
    )

    descripcion=models.CharField(max_length=25, verbose_name='Material')
    voltajeSoportado=models.PositiveSmallIntegerField(choices=VOLT, default=240)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural='Materiales'


class detalleMaterialContrato(models.Model):
    material=models.ForeignKey('subtipoDeMaterial', blank=True, null=True, default=None)
    contrato=models.ForeignKey('contrato')
    stock=models.BigIntegerField()
    unidad=models.CharField(max_length=15)
    proporcionado=models.BooleanField(verbose_name='¿Provisto por CNEL EP?', default=True)

    def __unicode__(self):
        return u'%s' % (
            str(self.material)
        )

    class Meta:
        verbose_name_plural='Materiales para cada Contrato'



class servicio(models.Model):
    descripcion=models.CharField(max_length=100, verbose_name='Servicio')

    def __unicode__(self):
        return self.descripcion

class rubro(models.Model):
    descripcion=models.CharField(max_length=100, verbose_name='Rubro')

    def __unicode__(self):
        return self.descripcion

class detalleRubro(models.Model):
    contrato=models.ForeignKey('contrato')
    servicio=models.ForeignKey('servicio')
    rubro=models.ForeignKey('rubro')
    precioUnitario=models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return u'%s' % self.rubro.descripcion

    class Meta:
        verbose_name_plural='Valores a Facturar de cada Contrato'
