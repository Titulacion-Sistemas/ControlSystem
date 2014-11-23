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
    serie = models.CharField(max_length=9, verbose_name='Numero de Serie')
    marca = models.ForeignKey(marca, verbose_name='Marca')
    tipo = models.CharField(max_length=15, verbose_name='Tipo de Medidor')
    digitos = models.PositiveSmallIntegerField(verbose_name='Dígitos')
    hilos = models.PositiveSmallIntegerField(verbose_name='Hilos')
    fases = models.PositiveSmallIntegerField(verbose_name='Fases')
    voltaje = models.PositiveSmallIntegerField(choices=VOLT)
    est = models.BooleanField(default=True)
    modelo=models.ForeignKey('ingresos.modeloDeMedidor', blank=True, null=True, default='')

    def __unicode__(self):
        return '%s - %s' % (self.fabrica, self.serie)

    class Meta:
        verbose_name_plural='Medidores'





class sello(models.Model):
    UBICACIONES={
        ('Caja', 'Caja'),
        ('Tapa', 'Tapa'),
        ('Bornera', 'Bornera'),
    }
    detalleMaterialContrato=models.ForeignKey('detalleMaterialContrato', verbose_name='Detalle de Material / Contrato')
    numero=models.CharField(max_length=10, verbose_name='Número de Sello')
    color=models.CharField(max_length=20, verbose_name='Color de Sello')
    ubicacion=models.CharField(max_length=10, choices=UBICACIONES, default='Caja')
    estado=models.PositiveSmallIntegerField(default=True)

class subtipoDeMaterial(models.Model):
    tipoDeMaterial=models.ForeignKey('tipoDeMaterial', verbose_name='Tipo de Material')
    descripcion=models.CharField(max_length=25, verbose_name='Subtipo de Material')

    def __unicode__(self):
        return '%s %s %s' % (
            self.tipoDeMaterial.material.descripcion,
            self.tipoDeMaterial.descripcion,
            self.descripcion
        )

    class Meta:
        verbose_name_plural='Subtipos de Material'

class tipoDeMaterial(models.Model):
    material=models.ForeignKey('material', verbose_name='Material')
    descripcion=models.CharField(max_length=25, verbose_name='Tipo de Material')

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

class rangoDeMaterial(models.Model):
    detalleMaterialContrato=models.OneToOneField('detalleMaterialContrato')
    inicio=models.DecimalField(max_digits=10, decimal_places=0)
    final=models.DecimalField(max_digits=10, decimal_places=0)

    def __unicode__(self):
        return '%s => %s' % (str(self.inicio), str(self.final))

    class Meta:
        verbose_name_plural='Rango de Materiales'

class detalleMaterialContrato(models.Model):
    material=models.ForeignKey('subtipoDeMaterial')
    contrato=models.ForeignKey('contrato')
    stock=models.BigIntegerField()
    unidad=models.CharField(max_length=15)
    proporcionado=models.BooleanField(verbose_name='¿Provisto por CNEL EP?', default=True)

    def __unicode__(self):
        return 'Contrato:%s - Material:%s' % (
            self.contrato,
            self.material
        )

    class Meta:
        verbose_name_plural='Materiales para cada Contrato'

class servicio(models.Model):
    descripcion=models.CharField(max_length=25, verbose_name='Servicio')

    def __unicode__(self):
        return self.descripcion

class rubro(models.Model):
    descripcion=models.CharField(max_length=25, verbose_name='Rubro')

    def __unicode__(self):
        return self.descripcion

class detalleRubro(models.Model):
    contrato=models.ForeignKey('contrato')
    servicio=models.ForeignKey('servicio')
    rubro=models.ForeignKey('rubro')
    precioUnitario=models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural='Valores a Facturar de cada Contrato'
