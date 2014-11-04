# coding=utf-8
# Create your models here.
import datetime
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models
from django.utils.timezone import now


class contrato(models.Model):
    num = models.CharField(max_length=10, primary_key=True, verbose_name='Número de Contrato')
    descripcion = models.CharField(max_length=150, verbose_name='Descripción')
    zonas = models.CharField(max_length=150, verbose_name='Zona(s)')
    codigoInstalador = models.PositiveSmallIntegerField(verbose_name='Código de Instalador')
    inicioVigencia = models.DateField(verbose_name='Vigente Desde')
    finalVigencia = models.DateField(verbose_name='Vigente Hasta')

    def __unicode__(self):
        return self.num


class usuarioSico(models.Model):
    nombre = models.CharField(max_length=10, verbose_name='Nombre de Usuario en Sico')
    clave = models.CharField(max_length=10, verbose_name='Contraseña en Sico')
    contrato = models.ForeignKey(contrato)

    def __unicode__(self):
        return '%s - %s' % (self.nombre, self.contrato.num)

    class Meta:
        verbose_name='Usuario en Sico'
        verbose_name_plural='Usuarios en Sico'


#EDICION DE MODELO USER
User.add_to_class('sesion_sico', models.CharField(max_length=2, null=True, blank=True))
User.add_to_class('usuario_sico', models.ManyToManyField(usuarioSico, blank=True, null=True))
#User.add_to_class('amigos', models.ManyToManyField('self', symmetrical=True,  ))




#FORMULARIOS
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name',
                  #'usuario_sico', 'contrasenia_sico'
        ]
        widgets = {
            'password': forms.PasswordInput(),
            #'contrasenia_sico': forms.PasswordInput(),
        }


class LogIn(forms.Form):
    usuario = forms.CharField(
        max_length=10,
        required=True,
        label='Nombre de Usuario',
        widget=forms.TextInput(attrs={'placeholder': 'Escriba su nombre de usuario'})
    )
    clave = forms.CharField(
        max_length=10,
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': ''})
    )
    sico = forms.ModelChoiceField(
        queryset=contrato.objects.filter(finalVigencia__gte=datetime.date.today()),
        #initial=contrato.objects.first().num,
        label='Contrato Nro.'
    )