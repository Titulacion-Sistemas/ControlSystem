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
    def __init__(self, idActividad=0, contrato=None, *args, **kwargs):
        super(cambioDeMaterialForm, self).__init__(*args, **kwargs)
        if contrato!=None:
            self.fields['material'] = forms.ModelMultipleChoiceField(
                detalleMaterialContrato.objects
                    #.filter(contrato=contrato)
                    .exclude(material__tipoDeMaterial__material__descripcion='KIT '),
                label='Materiales',
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

        if idActividad>0:
            self.rellenarDetalle(idActividad)

            #uso de inmueble
            #self.fields['usoEspecificoDelInmueble'].initial = 1 #usoEspecificoDelInmueble.objects.filter(descripcion=' ')[0].id

    #actividad
    fecha = forms.DateField(
        initial=datetime.date.today(), label='Fecha',
        widget=SelectDateWidget(), required=True
    )
    hora = forms.TimeField(
        initial=now().time(), label='Hora',
        widget=forms.TimeInput(), required=True
    )

    #Cliente
    codigoDeCliente = forms.CharField(
        max_length=7, min_length=5, label='Código',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por Cta.'}),
        required=False
    )
    nombreDeCliente = forms.CharField(
        max_length=50, min_length=6, label='Nombre',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por Nombre'}),
        required=False
    )
    cedula = forms.CharField(
        max_length=13, min_length=10, label='Cédula',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=True
    )
    telefono = forms.CharField(
        max_length=11, min_length=7, label='Teléfono',
        widget=forms.TextInput(attrs={'placeholder': 'Escriba un teléfono de referencia'}),
        required=False
    )
    lugar = forms.CharField(
        max_length=50, label='Lugar',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    calle = forms.CharField(
        max_length=50, label='Calle',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    geocodigo = forms.CharField(
        max_length=20, label='Geocódigo',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por Geocodigo'}),
        required=False
    )


    #Medidor(Revisado)
    fabricaRev = forms.CharField(
        max_length=11, label='Fabrica',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por Merdidor'}),
        required=False
    )
    serieRev = forms.CharField(
        max_length=10, label='Serial',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    marcaRev = forms.CharField(
        max_length=25, label='Marca',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    lecturaRev = forms.CharField(
        max_length=11, label='Lectura',
        widget=forms.TextInput(attrs={'placeholder': 'Digite la lectura del medidor'}),
        required=False
    )


    #Medidor(Instalado)
    medidor = forms.ModelChoiceField(
        medidor.objects, label='En Bodega',
        required=False
    )
    fabricaInst = forms.CharField(
        max_length=11, label='Fabrica',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    serieInst = forms.CharField(
        max_length=10, label='Serial',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    marcaInst = forms.CharField(
        max_length=25, label='Marca',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    tipoDeMedidor = forms.CharField(
        max_length=25, label='Tipo',
        widget=forms.TextInput(attrs={'placeholder': 'Cambiar Tipo de Medidor'}),
        required=False
    )
    lecturaInst = forms.CharField(
        max_length=11, label='Lectura',
        widget=forms.TextInput(attrs={'placeholder': 'Digite la lectura del medidor'}),
        initial='0',
        required=False
    )


    #Materiales
    material = forms.ModelMultipleChoiceField(
        detalleMaterialContrato.objects, label='Materiales',
        widget=forms.Select(),
        required=False
    )
    cantidad = forms.IntegerField(
        max_value=99, min_value=1, label='Cantidad',
        initial=1,
        required=False
    )


    #Detalles de Instalación
    usoEspecificoDelInmueble = forms.ModelChoiceField(
        usoEspecificoDelInmueble.objects,
        label='Uso del Inmueble',
        initial=1, #usoEspecificoDelInmueble.objects.filter(descripcion=' ')[0].id,
        required=True
    )
    usoDeEnergia = forms.ModelChoiceField(
        usoDeEnergia.objects,
        label='Uso de Energía',
        initial='RD',
        required=True
    )
    materialDeLaRed = forms.ModelChoiceField(
        materialDeLaRed.objects,
        label='Material de la Red',
        initial='AL',
        required=True
    )
    tipoDeConstruccion = forms.ModelChoiceField(
        tipoDeConstruccion.objects,
        label='Tipo de Construcción',
        initial=4,
        required=True
    )
    ubicacionDelMedidor = forms.ModelChoiceField(
        ubicacionDelMedidor.objects,
        label='Ubicación del Medidor',
        initial=1,
        required=True
    )
    tipoDeAcometidaRed = forms.ModelChoiceField(
        tipoDeAcometidaRed.objects,
        label='Tipo de Acometida',
        initial='AE',
        required=True
    )
    calibreDeLaRed = forms.ModelChoiceField(
        calibreDeLaRed.objects,
        label='Calibre de Red',
        initial=17,
        required=True
    )
    claseRed = forms.ModelChoiceField(
        claseRed.objects,
        label='Clase de Red',
        initial='D',
        required=True
    )
    nivelSocieconomico = forms.ModelChoiceField(
        nivelSocieconomico.objects,
        label='Nivel Socioeconómico',
        initial='BA',
        required=False
    )
    estadoDeUnaInstalacion = forms.ModelChoiceField(
        estadoDeUnaInstalacion.objects,
        label='Estado de Instalación',
        initial=1
    )
    formaDeConexion = forms.ModelChoiceField(
        formaDeConexion.objects,
        label='Forma de Conexión',
        required=True
        #initial=4
    )
    demanda = forms.ModelChoiceField(
        demanda.objects,
        label='Demanda',
        initial=1
    )
    motivoParaSolicitud = forms.ModelChoiceField(
        motivoParaSolicitud.objects,
        label='Motivo de Solicitud',
        initial=2
    )
    tipoDeSolicitud = forms.ModelChoiceField(
        tipoDeSolicitud.objects,
        label='Tipo de Solicitud',
        initial=11
    )
    tipoDeServicio = forms.ModelChoiceField(
        tipoDeServicio.objects,
        label='Tipo de Servicio',
        #initial='13B'
    )


    #Sello
    selloInst = forms.ModelMultipleChoiceField(
        sello.objects, label='En Bodega',
        widget=forms.Select(),
        required=False
    )
    ubicacionDeSello = forms.ChoiceField(
        choices=sello.UBICACIONES,
        label='Ubicacion',
        initial='Caja',
        required=False
    )


    #Referencia
    anterior = forms.CharField(
        max_length=11, label='Fábrica',
        widget=forms.TextInput(attrs={'placeholder': 'Nro. de Medidor de Ref.'}),
        required=False
    )
    serieAnteriror = forms.CharField(
        max_length=11, label='Serie',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    marcaAnteriror = forms.CharField(
        max_length=11, label='Marca',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    cuentaAnteriror = forms.CharField(
        max_length=11, label='Cuenta',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )


    #Instalador
    instalador = forms.ModelChoiceField(
        empleado.objects,
        label='Instalador',
        required=True
    )
    cuadrilla = forms.ModelChoiceField(
        cuadrilla.objects,
        label='Cuadrilla',
        required=True
    )


    #Fotos
    fotos = MultiFileField(
        max_num=10, min_num=1, maximum_file_size=1024 * 1024 * 5,
        required=True
    )


    #Observaciones
    observaciones = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Observaciones de la actividad realizada',
                'rows': "2",
                'cols': "50"
            }
        )
    )


    def save(self):
        pass

    def rellenarDetalle(self, idActividad):
        act = actividad.objects.get(id=idActividad)
