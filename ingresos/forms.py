# coding=utf-8
import datetime
from django import forms
from django.forms.extras import *
from django.utils.timezone import now
from ingresos.models import *
from ingresos.multiFile import MultiFileField
from inventario.models import detalleMaterialContrato, medidor, sello

__author__ = 'Jhonsson'


class cambioDeMaterialForm(forms.Form):
    def __init__(self, contrato, *args, **kwargs):
        super(cambioDeMaterialForm, self).__init__(*args, **kwargs)
        self.fields['material'] = forms.ModelMultipleChoiceField(
            detalleMaterialContrato.objects.filter(contrato=contrato), label='Materiales',
            widget=forms.Select()
        )
        # medidores segun contrato...
        self.fields['medidor'] = forms.ModelMultipleChoiceField(
            medidor.objects.filter(contrato__contrato=contrato), label='En bodega',
            widget=forms.Select()
        )
        # sellos segun contrato...
        self.fields['selloInst'] = forms.ModelMultipleChoiceField(
            sello.objects.filter(detalleMaterialContrato__contrato=contrato), label='En bodega',
            widget=forms.Select()
        )

    #actividad
    fecha = forms.DateField(
        initial=datetime.date.today(), label='Fecha',
        widget=SelectDateWidget()
    )
    hora = forms.TimeField(
        initial=now().time(), label='Hora',
        widget=forms.TimeInput()
    )
    tipoDeActividad = forms.ChoiceField(
        choices=(
            ('1', 'Cambio de Materiales'),
            ('2', 'Cambio de Medidor'),
            ('3', 'Servicio Nuevo')
        ),
        label='Actividad Realizada',
        #initial='1'
    )


    #Cliente
    codigoDeCliente = forms.CharField(
        max_length=7, min_length=5, label='Código',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por Cta.'})
    )
    nombreDeCliente = forms.CharField(
        max_length=50, min_length=6, label='Nombre',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por Nombre'})
    )
    cedula = forms.CharField(
        max_length=13, min_length=10, label='Cédula',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    telefono = forms.CharField(
        max_length=11, min_length=7, label='Teléfono',
        widget=forms.TextInput(attrs={'placeholder': 'Escriba un teléfono de referencia'})
    )
    lugar = forms.CharField(
        max_length=50, label='Lugar',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    calle = forms.CharField(
        max_length=50, label='Calle',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    geocodigo = forms.CharField(
        max_length=20, label='Geocódigo',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por Geocodigo'})
    )


    #Medidor(Revisado)
    fabricaRev = forms.CharField(
        max_length=11, label='Fabrica',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por Merdidor'})
    )
    serieRev = forms.CharField(
        max_length=10, label='Serial',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    marcaRev = forms.CharField(
        max_length=25, label='Marca',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    lecturaRev = forms.CharField(
        max_length=11, label='Lectura',
        widget=forms.TextInput(attrs={'placeholder': 'Digite la lectura del medidor'})
    )


    #Medidor(Instalado)
    medidor = forms.ModelChoiceField(
        medidor.objects, label='En Bodega',
    )
    fabricaInst = forms.CharField(
        max_length=11, label='Fabrica',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    serieInst = forms.CharField(
        max_length=10, label='Serial',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    marcaInst = forms.CharField(
        max_length=25, label='Marca',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''})
    )
    lecturaInst = forms.CharField(
        max_length=11, label='Lectura',
        widget=forms.TextInput(attrs={'placeholder': 'Digite la lectura del medidor'}),
        initial='0'
    )


    #Materiales
    material = forms.ModelMultipleChoiceField(
        detalleMaterialContrato.objects, label='Materiales',
        widget=forms.Select()
    )
    cantidad = forms.IntegerField(
        max_value=99, min_value=1, label='Cantidad',
        initial=1
    )


    #Detalles de Instalación
    usoEspecificoDelInmueble = forms.ModelChoiceField(
        usoEspecificoDelInmueble.objects,
        label='Uso del Inmueble'

    )
    usoDeEnergia = forms.ModelChoiceField(
        usoDeEnergia.objects,
        label='Uso de Energía'
    )
    materialDeLaRed = forms.ModelChoiceField(
        materialDeLaRed.objects,
        label='Material de la Red'
    )
    tipoDeConstruccion = forms.ModelChoiceField(
        tipoDeConstruccion.objects,
        label='Tipo de Construcción'
    )
    ubicacionDelMedidor = forms.ModelChoiceField(
        ubicacionDelMedidor.objects,
        label='Ubicación del Medidor'
    )
    tipoDeAcometidaRed = forms.ModelChoiceField(
        tipoDeAcometidaRed.objects,
        label='Tipo de Acometida'
    )
    calibreDeLaRed = forms.ModelChoiceField(
        calibreDeLaRed.objects,
        label='Calibre de Red'
    )
    claseRed = forms.ModelChoiceField(
        claseRed.objects,
        label='Clase de Red'
    )
    nivelSocieconomico = forms.ModelChoiceField(
        nivelSocieconomico.objects,
        label='Nivel Socioeconómico'
    )
    estadoDeUnaInstalacion = forms.ModelChoiceField(
        estadoDeUnaInstalacion.objects,
        label='Estado de Instalación'
    )
    formaDeConexion = forms.ModelChoiceField(
        formaDeConexion.objects,
        label='Forma de Conexión'
    )
    demanda = forms.ModelChoiceField(
        demanda.objects,
        label='Demanda'
    )
    motivoParaSolicitud = forms.ModelChoiceField(
        motivoParaSolicitud.objects,
        label='Motivo de Solicitud'
    )
    tipoDeSolicitud = forms.ModelChoiceField(
        tipoDeSolicitud.objects,
        label='Tipo de Solicitud'
    )
    tipoDeServicio = forms.ModelChoiceField(
        tipoDeServicio.objects,
        label='Tipo de Servicio',
    )


    #Sello
    selloInst = forms.ModelMultipleChoiceField(
        sello.objects, label='En Bodega',
        widget=forms.Select()
    )
    ubicacionDeSello = forms.ChoiceField(
        choices=sello.UBICACIONES,
        label='Ubicacion',
        initial='Caja'
    )


    #Referencia
    anterior = forms.CharField(
        max_length=11, label='Anterior',
        widget=forms.TextInput(attrs={'placeholder': '# de Medidor'})
    )
    posterior = forms.CharField(
        max_length=11, label='Posterior',
        widget=forms.TextInput(attrs={'placeholder': '# de Medidor'})
    )


    #Instalador
    instalador = forms.ModelChoiceField(
        empleado.objects,
        label='Instalador'
    )
    cuadrilla = forms.ModelChoiceField(
        cuadrilla.objects,
        label='Cuadrilla'
    )


    #Fotos
    fotos = MultiFileField(max_num=10, min_num=1, maximum_file_size=1024 * 1024 * 5)


    #Observaciones
    observaciones = forms.CharField(
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Observaciones de la actividad realizada',
                'rows': "4",
                'cols': "50"
            }
        )
    )

