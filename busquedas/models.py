# coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm
from ingresos.models import cliente, medidor


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


class ClienteBuscado(ModelForm):
    geo = forms.CharField(label='Geocódigo', widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = cliente

        fields = [
            'cuenta',
            'nombre',
            'ci_ruc',
            'geo',
            'direccion',
            'interseccion',
            'urbanizacion',
            'estado',
            'deuda',
            'meses'
        ]

        widgets = {
            'cuenta':       forms.TextInput(attrs={'readonly': True}),
            'nombre':       forms.TextInput(attrs={'readonly': True}),
            'ci_ruc':       forms.TextInput(attrs={'readonly': True}),
            'direccion':    forms.TextInput(attrs={'readonly': True}),
            'interseccion': forms.TextInput(attrs={'readonly': True}),
            'urbanizacion': forms.TextInput(attrs={'readonly': True}),
            'estado':       forms.TextInput(attrs={'readonly': True}),
            'deuda':        forms.TextInput(attrs={'readonly': True}),
            'meses':        forms.TextInput(attrs={'readonly': True}),
        }

    def __init__(self, geo, *args, **kwargs):
        super(ClienteBuscado, self).__init__(*args, **kwargs)
        self.fields['geo'].initial = str(geo)

class MedidorBuscado(ModelForm):
    marc = forms.CharField(label='Marca', widget=forms.TextInput(attrs={'readonly': True}))
    tecnologia = forms.CharField(label='Tecnología', widget=forms.TextInput(attrs={'readonly': True}))
    tension = forms.CharField(label='Tensión', widget=forms.TextInput(attrs={'readonly': True}))
    amperaje = forms.CharField(label='Amperaje', widget=forms.TextInput(attrs={'readonly': True}))
    fi = forms.CharField(label='Fecha de Instalación', widget=forms.TextInput(attrs={'readonly': True}))
    fd = forms.CharField(label='Fecha de Desinstalación', widget=forms.TextInput(attrs={'readonly': True}))
    li = forms.CharField(label='Lectura de Instalación', widget=forms.TextInput(attrs={'readonly': True}))
    ld = forms.CharField(label='Lectura de Desinstalación', widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = medidor

        fields = [
            'fabrica',
            'serie',
            'marc',
            'tipo',
            'tecnologia',
            'tension',
            'amperaje',
            'fases',
            'hilos',
            'digitos',
            'fi', 'li',
            'fd', 'ld'
        ]

        widgets = {
            'fabrica':      forms.TextInput(attrs={'readonly': True}),
            'serie':        forms.TextInput(attrs={'readonly': True}),
            'marc':         forms.TextInput(attrs={'readonly': True}),
            'tipo':         forms.TextInput(attrs={'readonly': True}),
            'tecnologia':   forms.TextInput(attrs={'readonly': True}),
            'tension':      forms.TextInput(attrs={'readonly': True}),
            'amperaje':     forms.TextInput(attrs={'readonly': True}),
            'fases':        forms.TextInput(attrs={'readonly': True}),
            'hilos':        forms.TextInput(attrs={'readonly': True}),
            'digitos':      forms.TextInput(attrs={'readonly': True}),
            'fi':           forms.TextInput(attrs={'readonly': True}),
            'li':           forms.TextInput(attrs={'readonly': True}),
            'fd':           forms.TextInput(attrs={'readonly': True}),
            'ld':           forms.TextInput(attrs={'readonly': True}),
        }

    def __init__(self, marc, tecnologia, tension, amperaje, fi, fd, li, ld, *args, **kwargs):
        super(MedidorBuscado, self).__init__(*args, **kwargs)
        self.fields['marc'].initial = str(marc)
        self.fields['tecnologia'].initial = str(tecnologia)
        self.fields['tension'].initial = str(tension)
        self.fields['amperaje'].initial = str(amperaje)
        self.fields['fi'].initial = str(fi)
        self.fields['fd'].initial = str(fd)
        self.fields['li'].initial = str(li)
        self.fields['ld'].initial = str(ld)