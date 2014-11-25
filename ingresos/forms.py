# coding=utf-8
import datetime
from django import forms
from django.forms.extras import *
from django.utils.timezone import now
from ingresos.models import *

__author__ = 'Jhonsson'



class cambioDeMaterialForm(forms.Form):

    fecha=forms.DateField(initial=datetime.date.today(), label='Fecha de Actividad', widget=SelectDateWidget())
    hora=forms.TimeField(initial=now(), label='Hora de Actividad', widget=forms.TimeInput())

    #Cliente
    codigoDeCliente=forms.CharField(
        max_length=7, min_length=5, label='Código : ',
        widget=forms.TextInput(attrs={'placeholder': 'Escriba la Cuenta'})
    )
    nombreDeCliente = forms.CharField(
        max_length=50, min_length=6, label='Nombre : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    cedula = forms.CharField(
        max_length=13, min_length=10, label='Cédula o Ruc : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    telefono = forms.CharField(
        max_length=11, min_length=7, label='Teléfono : ',
        widget=forms.TextInput(attrs={'placeholder': 'Escriba un teléfono de referencia'})
    )
    lugar = forms.CharField(
        max_length=50, label='Lugar : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    calle = forms.CharField(
        max_length=50, label='Calle : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    parroquia = forms.CharField(
        max_length=50,  label='Parroquia : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )

    #canton=forms.ModelChoiceField(canton.objects, label='Cantón : ')
    #parroquia=forms.ModelChoiceField(parroquia.objects.filter(canton=canton.initial), label='Parroquia : ')
    #direccion=forms.ModelChoiceField(calle.objects.filter(descripcion1='sin descripcion'), label='Direccion : ')
    #urbanizacion=forms.ModelChoiceField(urbanizacion.objects)

    #Medidor(Revisado)
    fabrica = forms.CharField(
        max_length=11,  label='Fabrica : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    serie = forms.CharField(
        max_length=10,  label='Serial : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    marca = forms.CharField(
        max_length=25,  label='Marca : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    voltaje = forms.CharField(
        max_length=4,  label='Voltaje : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    lectura = forms.CharField(
        max_length=11,  label='Lectura : ',
        widget=forms.TextInput(attrs={'placeholder': 'Digite la lectura del medidor'})
    )
    amp = forms.CharField(
        max_length=15,  label='Amp : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    fases = forms.CharField(
        max_length=2,  label='Fases : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    hilos = forms.CharField(
        max_length=2,  label='Hilos : ',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )


    #Materiales
    material=forms.ModelChoiceField(canton.objects, label='Cantón : ')



