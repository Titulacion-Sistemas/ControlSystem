# coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, model_to_dict
from ingresos.models import cliente, secuencia


class vitacoraBusquedas(models.Model):
    TIPOSBUSQUEDA = (
        ('1', 'Cuenta'),
        ('2', 'Medidor'),
        ('3', 'Nombre'),
        ('4', 'Geocodigo'),
    )

    tipoBusq = models.CharField(max_length=1, choices=TIPOSBUSQUEDA, default='1', verbose_name='Buscar por ')
    fechaHora = models.DateTimeField(auto_now=True)
    consulta = models.CharField(max_length=17, null=False, verbose_name='')
    usuario = models.ForeignKey(User)
    estadoRetorno = models.BooleanField(default=False)

    def __str__(self):
        return 'Busqueda por :{0}, ({1})'.format(self.get_TipoBusq_display(), self.consulta)


#FORMULARIOS
class BusquedaForm(ModelForm):
    class Meta:
        model = vitacoraBusquedas
        fields = ['tipoBusq', 'consulta']

    def __init__(self, usuario, *args, **kwargs):
        super(BusquedaForm, self).__init__(*args, **kwargs)
        self.usuario = usuario

    def save(self, commit=True):
        vitacoraBusquedas = super(BusquedaForm, self).save(commit=False)
        vitacoraBusquedas.usuario = self.usuario
        if commit:
            vitacoraBusquedas.save()
        return vitacoraBusquedas


class Buscado(ModelForm):
    geo = forms.CharField(label='Geocódigo', widget=forms.TextInput(attrs={'title':'Gecódigo'}))

    class Meta:
        model = cliente

        fields = ['cuenta', 'nombre', 'ci_ruc', 'geo', 'direccion', 'estado', 'deuda', 'meses']
        widgets = {
            'deuda': forms.TextInput,
            'meses': forms.TextInput,
        }

    def __init__(self, geo, *args, **kwargs):
        super(Buscado, self).__init__(*args, **kwargs)
        self.fields['geo'].initial = str(geo)
