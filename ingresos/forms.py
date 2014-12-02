# coding=utf-8
import datetime
from django import forms
from django.forms.extras import *
from django.utils.timezone import now
from ingresos.models import *
from ingresos.multiFile import MultiFileField
from inventario.models import detalleMaterialContrato, medidor, sello

__author__ = 'Jhonsson'


class ingresoForm(forms.Form):
    def __init__(self, actividad=None, contrato=None, *args, **kwargs):
        super(ingresoForm, self).__init__(*args, **kwargs)
        if actividad:
            self.rellenarDetalle(actividad)
        elif contrato != None:
            self.fields['material'] = forms.ModelMultipleChoiceField(
                detalleMaterialContrato.objects
                .filter(contrato=contrato)
                .exclude(material__tipoDeMaterial__material__descripcion='KIT '),
                label='Materiales',
                widget=forms.Select()
            )
            # medidores segun contrato...
            self.fields['medidor'] = forms.ModelMultipleChoiceField(
                medidor.objects.filter(contrato__contrato=contrato, est=True), label='En bodega',
                widget=forms.Select()
            )
            # sellos segun contrato...
            self.fields['selloInst'] = forms.ModelMultipleChoiceField(
                sello.objects.filter(detalleMaterialContrato__contrato=contrato, utilizado=None), label='En bodega',
                widget=forms.Select()
            )


    #actividad
    id=forms.CharField(
        required=False, initial=0, label='',
        widget=forms.TextInput(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
    )
    estadoSolicitud = forms.CharField(
        initial=estadoDeSolicitud.__unicode__(estadoDeSolicitud.objects.get(id=0)), label='',
        widget=forms.TextInput(),
        required=False
    )
    numeroDeSolicitud = forms.CharField(
        max_length=8, required=False, label='Número do Solicitud',
        widget=forms.TextInput(attrs={
            'style': 'text-align: center; font-size: 1.35em;',
            'readonly': True,
            'placeholder': 'No. de Solicitud'
        }),
        initial='0'
    )
    tipoDeSolicitud = forms.ModelChoiceField(
        tipoDeSolicitud.objects,
        label='Tipo de Solicitud',
        initial=11
    )
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
        required=True
    )
    cedula = forms.CharField(
        max_length=13, min_length=10, label='Cédula',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    telefono = forms.CharField(
        max_length=11, min_length=7, label='Teléfono',
        widget=forms.TextInput(attrs={'placeholder': 'Teléfono de referencia'}),
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
        max_length=12, label='Serial',
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
        widget=forms.TextInput(attrs={'readonly': True,'placeholder': ''}),
        required=False
    )
    lecturaInst = forms.CharField(
        max_length=11, label='Lectura',
        widget=forms.TextInput(attrs={'placeholder': 'Digite la lectura del medidor'}),
        initial='0',
        required=False
    )


    #Materiales
    material = forms.ModelChoiceField(
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
    tipoDeServicio = forms.ModelChoiceField(
        tipoDeServicio.objects,
        label='Tipo de Servicio',
        #initial='13B'
        required=True
    )


    #Sello
    selloInst = forms.ModelChoiceField(
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
        maximum_file_size=1024 * 1024 * 30,
        required=False
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


    materialesSeleccionados=forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
        label='',
        required=True
    )
    cantMaterialesSeleccionados=forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
        required=True
    )
    sellosSeleccionados=forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
        required=True
    )
    ubiSellosSeleccionados=forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
        label='',
        required=True
    )


    def save(self):
        print self.data['id']
        if self.data['id']==0:
            act = actividad.objects.get(id=self.data['id'])
        else:
            #cliente=
            act=actividad(
                numeroDeSolicitud=self.data['numeroDeSolicitud'],
                #cliente=
            )
        if self.tipoDeSolicitud.empty_values == 13:
            pass
        print self.tipoDeSolicitud


#class actividad(models.Model):
#    numeroDeSolicitud=models.CharField(max_length=10, verbose_name='Número de Solicitud')
#    cliente=models.ForeignKey('cliente')
#    tipoDeConstruccion=models.ForeignKey('tipoDeConstruccion')
#    instalador=models.ForeignKey('instalador')
#    ubicacionDelMedidor=models.ForeignKey('ubicacionDelMedidor')
#    claseRed=models.ForeignKey('claseRed')
#    nivelSocieconomico=models.ForeignKey('nivelSocieconomico', blank=True, null=True, default='')
#    calibreDeLaRed=models.ForeignKey('calibreDeLaRed')
#    estadoDeLaInstalacion=models.ForeignKey('estadoDeUnaInstalacion')
#    tipoDeAcometidaRed=models.ForeignKey('tipoDeAcometidaRed', verbose_name='Tipo de Acometida o Red')
#    fechaDeActividad=models.DateField(verbose_name='Fecha de Actividad', editable=True)
#    horaDeActividad=models.TimeField(verbose_name='Hora de Actividad', editable=True)
#    usoDeEnergia=models.ForeignKey('usoDeEnergia')
#    usoEspecificoDelInmueble=models.ForeignKey('usoEspecificoDelInmueble')
#    formaDeConexion=models.ForeignKey('formaDeConexion')
#    demanda=models.ForeignKey('demanda')
#    motivoDeSolicitud=models.ForeignKey('motivoParaSolicitud')
#    tipoDeSolicitud=models.ForeignKey('tipoDeSolicitud')
#    materialDeLaRed=models.ForeignKey('materialDeLaRed')
#    estadoDeSolicitud=models.ForeignKey('estadoDeSolicitud')



    def rellenarDetalle(self, idActividad):
        try:
            act = actividad.objects.get(id=idActividad)

        except:
            pass




    def is_valid(self):
        # run the parent validation first
        valid = super(ingresoForm, self).is_valid()

        #dicDeErrores = dict(self.errors)
        del self.errors['sellosSeleccionados']
        del self.errors['materialesSeleccionados']
        del self.errors['ubiSellosSeleccionados']
        del self.errors['cantMaterialesSeleccionados']
        print 'Validando...'
        print self.errors
        if len(self.errors)==0:
            return True
        else:
            return False
        #

    def clean(self):
        cleaned_data = super(ingresoForm, self).clean()
        ts = self.data['tipoDeSolicitud']
        print ts
        if ts == '11' or ts == '13':
            if not self.data['codigoDeCliente']:
                self._errors["Cuenta"] = self.error_class([u"Ingrese un número de Cuenta."])
            if not self.data['serieRev']:
                self._errors["Medidor"] = self.error_class([u"El Cliente debe tener un medidor activo."])
            if ts == '13':
                if not str(self.data['lecturaRev']):
                    self._errors["Lectura"] = self.error_class([u"Ingrese una Lectura de Desconección "])
        if ts=='1' or ts=='13':
            if not self.data['tipoDeMedidor']:
                self._errors["Medidor"] = self.error_class([u" Seleccione el medidor a instalar "])
            if ts == '1':
                if not str(self.data['cuentaAnteriror']):
                    self._errors["Referencia"] = self.error_class([u"Ingrese la referencia de instalación del Servicio nuevo "])


        return cleaned_data
