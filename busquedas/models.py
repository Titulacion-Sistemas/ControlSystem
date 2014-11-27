# coding=utf-8
import user
from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm
from ingresos.models import cliente
from inventario.models import medidor


class vitacoraBusquedas(models.Model):
    TIPOSBUSQUEDA = (
        ('1', 'Cuenta'),
        ('2', 'Medidor'),
        ('3', 'Nombre'),
        ('4', 'Geocodigo'),
    )
    tipoBusq = models.CharField(max_length=1, choices=TIPOSBUSQUEDA, default='1', verbose_name='Buscar por ')
    fechaHora = models.DateTimeField(auto_now=True, auto_now_add=True, editable=True)
    consulta = models.CharField(max_length=20, null=False, verbose_name='')
    usuario = models.ForeignKey(User)
    estadoRetorno = models.BooleanField(default=True)

    def __str__(self):
        opciones = {
            '1': 'Cuenta',
            '2': 'Medidor',
            '3': 'Nombre',
            '4': 'Geocodigo'
        }
        return 'Busqueda por %s: %s, (%s)' % (opciones[self.tipoBusq], self.consulta, self.fechaHora)

    class Meta:
        verbose_name_plural="Búsquedas Realizadas"
        verbose_name="Registro de Búsqueda"


#FORMULARIOS
class BusquedaForm(ModelForm):
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    estadoRetorno = forms.BooleanField(widget=forms.HiddenInput())

    class Meta:
        model = vitacoraBusquedas
        fields = ['usuario', 'tipoBusq', 'consulta', 'estadoRetorno']

    def save(self, retorno=True, commit=True):
        vitacoraBusquedas = super(BusquedaForm, self).save(commit=False)
        vitacoraBusquedas.estadoRetorno = retorno
        if commit:
            vitacoraBusquedas.save()
        return vitacoraBusquedas

    def clean(self):
        cleaned_data = super(BusquedaForm, self).clean()
        tb = cleaned_data.get("tipoBusq")
        c = cleaned_data.get("consulta")

        if c and tb:
            # Only do something if both fields are valid so far.
            if tb == '1':
                if not c.isdigit() or len(c) > 8:
                    raise forms.ValidationError("Error, Cuenta ingresada no válida.")

            if tb == '2':
                if not c.isdigit() or len(c) > 11:
                    raise forms.ValidationError("Error, Número de medidor ingresado no válido.")

            if tb == '3':
                if c.isdigit():
                    raise forms.ValidationError("Error, Nombre de ciente no valido.")

            if tb == '4':
                sp = c.split('.')
                if len(sp) != 5 \
                    or (not sp[0].isdigit()) \
                    or (not sp[1].isdigit()) \
                    or (not sp[2].isdigit()) \
                    or (not sp[3].isdigit()) \
                    or (not sp[4].isdigit()):

                    raise forms.ValidationError("Error, Geocódigo incorrecto.")

                elif len(sp[0]) > 2 or len(sp[0]) < 1 \
                    or len(sp[1]) > 2 or len(sp[1]) < 1 \
                    or len(sp[2]) > 2 or len(sp[2]) < 1 \
                    or len(sp[3]) > 3 or len(sp[3]) < 1 \
                    or len(sp[4]) > 7 or len(sp[4]) < 1:

                    raise forms.ValidationError("Error, Geocódigo no válido.")

                # Always return the full collection of cleaned data.
        return cleaned_data


class ClienteBuscado(ModelForm):
    geo = forms.CharField(label='Geocódigo', widget=forms.TextInput(attrs={'readonly': True}))
    provincia=forms.CharField(label='Provincia', widget=forms.TextInput(attrs={'readonly': True}))
    canton=forms.CharField(label='Cantón', widget=forms.TextInput(attrs={'readonly': True}))
    parroquia=forms.CharField(label='Parroquia', widget=forms.TextInput(attrs={'readonly': True}))
    direccion=forms.CharField(label='Dirección', widget=forms.TextInput(attrs={'readonly': True}))
    interseccion=forms.CharField(label='Intersección', widget=forms.TextInput(attrs={'readonly': True}))
    urbanizacion=forms.CharField(label='Urbanización', widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = cliente

        fields = [
            'cuenta',
            'nombre',
            'ci_ruc',
            'geo',
            'provincia',
            'canton',
            'parroquia',
            'direccion',
            'interseccion',
            'urbanizacion',
            'estado',
            'deuda',
            'meses'
        ]

        widgets = {
            'cuenta': forms.TextInput(attrs={'readonly': True}),
            'nombre': forms.TextInput(attrs={'readonly': True}),
            'ci_ruc': forms.TextInput(attrs={'readonly': True}),
            'estado': forms.TextInput(attrs={'readonly': True}),
            'deuda': forms.TextInput(attrs={'readonly': True}),
            'meses': forms.TextInput(attrs={'readonly': True}),
        }

    def __init__(self, geo, ubicacion,  *args, **kwargs):
        super(ClienteBuscado, self).__init__(*args, **kwargs)
        self.fields['geo'].initial = str(geo)
        self.fields['provincia'].initial = str(geo.ruta.sector.canton.provincia.descripcion)
        self.fields['canton'].initial = str(geo.ruta.sector.canton.descripcion)
        self.fields['parroquia'].initial = str(ubicacion.parroquia.descripcion)
        self.fields['direccion'].initial = str(ubicacion.calle.descripcion1)
        self.fields['interseccion'].initial = str(ubicacion.interseccion.descripcion1)
        self.fields['urbanizacion'].initial = str(ubicacion.urbanizacion.descripcion)


class MedidorBuscado(ModelForm):
    marc = forms.CharField(label='Marca', widget=forms.TextInput(attrs={'readonly': True}))
    tecnologia = forms.CharField(label='Tecnología', widget=forms.TextInput(attrs={'readonly': True}))
    tension = forms.CharField(label='Tensión', widget=forms.TextInput(attrs={'readonly': True}))
    amperaje = forms.CharField(label='Amperaje', widget=forms.TextInput(attrs={'readonly': True}))
    fi = forms.CharField(label='Fecha/Inst.', widget=forms.TextInput(attrs={'readonly': True}))
    fd = forms.CharField(label='Fecha/Desinst.', widget=forms.TextInput(attrs={'readonly': True}))
    li = forms.CharField(label='Lectura/Inst.', widget=forms.TextInput(attrs={'readonly': True}))
    ld = forms.CharField(label='Lectura/Desinst.', widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = medidor

        fields = [
            'fabrica',
            'serie',
            'lectura',
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
            'fabrica': forms.TextInput(attrs={'readonly': True}),
            'serie': forms.TextInput(attrs={'readonly': True}),
            'lectura': forms.TextInput(attrs={'readonly': True}),
            'marc': forms.TextInput(attrs={'readonly': True}),
            'tipo': forms.TextInput(attrs={'readonly': True}),
            'tecnologia': forms.TextInput(attrs={'readonly': True}),
            'tension': forms.TextInput(attrs={'readonly': True}),
            'amperaje': forms.TextInput(attrs={'readonly': True}),
            'fases': forms.TextInput(attrs={'readonly': True}),
            'hilos': forms.TextInput(attrs={'readonly': True}),
            'digitos': forms.TextInput(attrs={'readonly': True}),
            'fi': forms.TextInput(attrs={'readonly': True}),
            'li': forms.TextInput(attrs={'readonly': True}),
            'fd': forms.TextInput(attrs={'readonly': True}),
            'ld': forms.TextInput(attrs={'readonly': True}),
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