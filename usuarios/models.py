# coding=utf-8
# Create your models here.
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models

class contrato(models.Model):
    num = models.CharField(max_length=10, primary_key=True, verbose_name='Número de Contrato')
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')
    codigoInstalador=models.PositiveSmallIntegerField(verbose_name='Código de Instalador')

#EDICION DE MODELO USER
User.add_to_class('usuario_sico', models.CharField(max_length=10, null=False, blank=False))
User.add_to_class('contrasenia_sico', models.CharField(max_length=10, null=False, blank=False))
User.add_to_class('sesion_sico', models.CharField(max_length=2, null=True, blank=True))
#User.add_to_class('amigos', models.ManyToManyField('self', symmetrical=True,  blank=True))

#FORMULARIOS
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'usuario_sico', 'contrasenia_sico']
        widgets = {
            'password': forms.PasswordInput(),
            'contrasenia_sico': forms.PasswordInput(),
        }
