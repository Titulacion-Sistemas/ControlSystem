# coding=utf-8
import datetime
from django import forms

__author__ = 'Jhonsson'



class cambioDeMaterialForm(forms.Form):

    tempo=forms.DateTimeField(initial=datetime.date.today(), label='Fecha y hora de Actividad')

    #Cliente
    codigoDeCliente=forms.CharField(max_length=7, min_length=5, label='Código')
    nombreDeCliente = forms.CharField(max_length=50, min_length=6, label='Nombre del Abonado')
    cedula = forms.CharField(max_length=13, min_length=10, label='Cédula o Ruc')
    parroquia=forms.ModelChoiceField('parroquia')
    direccion=forms.ModelChoiceField('calle')
    urbanizacion=forms.ModelChoiceField('urbanizacion')


    #



