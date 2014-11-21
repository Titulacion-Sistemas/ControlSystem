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

    fabrica = models.CharField(max_length=11, verbose_name='Número de Fábrica')
    serie = models.CharField(max_length=9, verbose_name='Numero de Serie')
    marca = models.ForeignKey(marca, verbose_name='Marca')
    tipo = models.CharField(max_length=15, verbose_name='Tipo de Medidor')
    digitos = models.PositiveSmallIntegerField(verbose_name='Dígitos')
    hilos = models.PositiveSmallIntegerField(verbose_name='Hilos')
    fases = models.PositiveSmallIntegerField(verbose_name='Fases')
    voltaje = models.PositiveSmallIntegerField(choices=VOLT)
    est = models.BooleanField(default=True)

class sello(models.Model):
    pass

class cable(models.Model):
    pass

class subtipoDeMaterial(models.Model):
    pass

class tipoDeMaterial(models.Model):
    pass

class material(models.Model):
    pass