# coding=utf-8
import datetime
from django import forms
from django.forms.extras import *
import time
from django.utils.timezone import now
from ingresos.models import *
from ingresos.multiFile import MultiFileField
from inventario.models import detalleMaterialContrato, medidor, sello, detalleRubro

__author__ = 'Jhonsson'


class ingresoForm(forms.Form):
    def __init__(self, actividad=None, contrato=None, *args, **kwargs):
        super(ingresoForm, self).__init__(*args, **kwargs)

        if contrato is not None:
            self.fields['material'] = forms.ModelMultipleChoiceField(
                detalleMaterialContrato.objects
                .filter(contrato=contrato)
                .exclude(material__tipoDeMaterial__material__descripcion='KIT '),
                label='Materiales',
                widget=forms.Select(),
                required=False
            )
            # medidores segun contrato...
            self.fields['medidor'] = forms.ModelMultipleChoiceField(
                medidor.objects.filter(contrato__contrato=contrato, est=True), label='En bodega',
                widget=forms.Select(),
                required=False

            )
            # sellos segun contrato...
            self.fields['selloInst'] = forms.ModelMultipleChoiceField(
                sello.objects.filter(detalleMaterialContrato__contrato=contrato, utilizado=None), label='En bodega',
                widget=forms.Select(),
                required=False
            )
        if actividad is not None and contrato is not None:
            self.rellenarDetalle(actividad, contrato)


    #actividad
    id = forms.CharField(
        required=False, initial=0, label='',
        widget=forms.TextInput(attrs={'style': 'height: 0px; padding: 0; margin: 0; border: 0;'}),
    )
    estadoSolicitud = forms.ModelChoiceField(
        estadoDeSolicitud.objects,
        initial=0, label=estadoDeSolicitud.objects.get(id=0).descripcion,
        widget=forms.TextInput(
            attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}
        ),
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
        initial=time.localtime(), label='Hora',
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
    estadoCli = forms.CharField(
        max_length=30, min_length=1, label='Estado',
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
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
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
        max_length=15, label='Serie',
        widget=forms.TextInput(attrs={'readonly': True, 'placeholder': ''}),
        required=False
    )
    marcaAnteriror = forms.CharField(
        max_length=25, label='Marca',
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

    #Adicionales
    contrastacion = forms.BooleanField(initial=False, label=u'Contrastación', required=False)
    reubicacion = forms.BooleanField(initial=False, label=u'Reubicación', required=False)
    directo = forms.BooleanField(initial=False, label=u'Directo', required=False)

    materialesSeleccionados = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
        label='',
        required=True,
    )
    cantMaterialesSeleccionados = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
        required=True
    )
    sellosSeleccionados = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
        required=True
    )
    ubiSellosSeleccionados = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
        label='',
        required=True
    )


    def save(self, contrato, cliente=None):
        print self.data['id']

        act = actividad()
        if cliente is not None:
            act.cliente = cliente

        act.tipoDeConstruccion = tipoDeConstruccion.objects.get(id=int(self.data['tipoDeConstruccion']))
        try:
            inst = instalador.objects.get(
                nombre=empleado.objects.get(id=int(self.data['instalador'])),
                cuadrilla=cuadrilla.objects.get(id=int(self.data['cuadrilla']))
            )
        except:
            inst = instalador(
                nombre=empleado.objects.get(id=int(self.data['instalador'])),
                cuadrilla=cuadrilla.objects.get(id=int(self.data['cuadrilla']))
            )
            inst.save()
        act.instalador = inst
        act.ubicacionDelMedidor = ubicacionDelMedidor.objects.get(id=int(self.data['ubicacionDelMedidor']))
        act.claseRed = claseRed.objects.get(id=self.data['claseRed'])
        act.nivelSocieconomico = nivelSocieconomico.objects.get(id=self.data['nivelSocieconomico'])
        act.calibreDeLaRed = calibreDeLaRed.objects.get(id=int(self.data['calibreDeLaRed']))
        act.estadoDeLaInstalacion = estadoDeUnaInstalacion.objects.get(id=int(self.data['estadoDeUnaInstalacion']))
        act.tipoDeAcometidaRed = tipoDeAcometidaRed.objects.get(id=self.data['tipoDeAcometidaRed'])
        act.tipoDeServicio = tipoDeServicio.objects.get(id=self.data['tipoDeServicio'])
        act.fechaDeActividad = datetime.date(
            int(self.data['fecha_year']),
            int(self.data['fecha_month']),
            int(self.data['fecha_day'])
        )
        try:
            act.horaDeActividad = datetime.datetime.strptime(self.data['hora'], '%H:%M:%S')
        except:
            act.horaDeActividad = datetime.time(hour=10, minute=30, second=0)

        act.usoDeEnergia = usoDeEnergia.objects.get(id=self.data['usoDeEnergia'])
        act.usoEspecificoDelInmueble = usoEspecificoDelInmueble.objects.get(id=self.data['usoEspecificoDelInmueble'])
        act.formaDeConexion = formaDeConexion.objects.get(id=int(self.data['formaDeConexion']))
        act.demanda = demanda.objects.get(id=int(self.data['demanda']))
        act.motivoDeSolicitud = motivoParaSolicitud.objects.get(id=int(self.data['motivoParaSolicitud']))
        act.tipoDeSolicitud = tipoDeSolicitud.objects.get(id=int(self.data['tipoDeSolicitud']))
        act.materialDeLaRed = materialDeLaRed.objects.get(id=self.data['materialDeLaRed'])
        act.observaciones = self.data['observaciones']

        if self.data['id'] != '0':
            act.id = self.data['id']
            act.numeroDeSolicitud = self.data['numeroDeSolicitud']
            act.estadoDeSolicitud = estadoDeSolicitud.objects.get(id=int(self.data['estadoSolicitud']))
            act.save(force_update=True)
        else:
            act.save()


        #borrando detalles de existir
            #de medidores...
        for m in list(medidor.objects.filter(actividad=act)):
            try:
                m.actividad=None
                m.save(force_update=True)
            except: pass


            #de sellos
        for s in list(sello.objects.filter(utilizado=act)):
            try:
                s.utilizado=None
                s.ubicacion='N/A'
                s.save(force_update=True)
            except: pass


            #de rubros
        for r in list(detalleDeActividad.objects.filter(actividad=act)):
            try:
                r.delete()
            except: pass


            #de materiales
        for m in list(materialDeActividad.objects.filter(actividad=act)):
            mat = detalleMaterialContrato.objects.get(id=m.material.id)
            mat.stock += m.cantidad
            mat.save(force_update=True)
            m.delete()



        #hay que generar detalles...
            #empezando con medidores
        try:
            medDeActividad = medidor.objects.get(
                fabrica=str(self.data['fabricaRev']),
                serie=str(self.data['serieRev'])
            )
            medDeActividad.actividad=act
            medDeActividad.save(force_update=True)
        except: pass
        try:
            medDeActividad = medidor.objects.get(
                fabrica=str(self.data['fabricaInst']),
                serie=str(self.data['serieInst'])
            )
            medDeActividad.actividad=act
            medDeActividad.save(force_update=True)
        except: pass


            #luego con sellos
        sellosInstalados = list(self.data.pop('sellosSeleccionados'))
        ubiSellosInstalados = list(self.data.pop('ubiSellosSeleccionados'))
        print sellosInstalados
        for sell in range(len(sellosInstalados)):
            si = sello.objects.get(id=int(sellosInstalados[sell]))
            si.ubicacion = ubiSellosInstalados[sell]
            si.utilizado = act
            si.save(force_update=True)

            #continuando con detalle de materiales para actividad
        materialInstalado = list(self.data.pop('materialesSeleccionados'))
        cantMaterialInstado = list(self.data.pop('cantMaterialesSeleccionados'))
        print materialInstalado
        for m in range(len(cantMaterialInstado)):

            mat = detalleMaterialContrato.objects.get(id=int(materialInstalado[m]))
            print int(materialInstalado[m])
            actMat = materialDeActividad(
                material=mat,
                actividad=act,
                cantidad=long(cantMaterialInstado[m])
            )
            actMat.save()
            mat.stock -= actMat.cantidad


        #actividades realizadas para desgloce de valores a facturar
        realizadas=[[5,6], [5,8]]
        if act.tipoDeSolicitud_id==1:
            realizadas.append([1,1])
            realizadas.append([5,7])
            print 'servicio nuevo...'
        elif act.tipoDeSolicitud_id==11 or act.tipoDeSolicitud_id==13:
            try:
                if self.data['contrastacion']:
                    realizadas.append([4,4])
                    print 'Contrastacion...'
            except: pass
            try:
                if self.data['reubicacion']:
                    realizadas.append([3,1])
                    print 'Reubicacion...'
            except: pass
            try:
                if materialDeActividad.objects.get(
                    actividad=act,
                    material=detalleMaterialContrato.objects.get(
                        contrato=contrato,
                        material__tipoDeMaterial__material__id=6#cable
                    )
                ):
                    try:
                        if realizadas.index([3,1])>=0:
                            realizadas.append([5,7])
                            print 'Reubicacion y desgloce para cable...'
                    except ValueError:
                        realizadas.append([4,3])
                        realizadas.append([5,7])
                        print 'Hay Solo Acometida...'
            except: pass

            if act.tipoDeSolicitud_id==11:
                try:
                    if materialDeActividad.objects.get(
                        actividad=act,
                        material=detalleMaterialContrato.objects.get(
                            contrato=contrato,
                            material__tipoDeMaterial__material__id=4#caja
                        )
                    ):
                        realizadas.append([4,2])
                        print u'Se realizó cambio de caja...'
                except:
                    try:
                        if materialDeActividad.objects.get(
                            actividad=act,
                            material=detalleMaterialContrato.objects.get(
                                contrato=contrato,
                                material__tipoDeMaterial__material__id=16#sello
                            )
                        ) and len(cantMaterialInstado)==1:
                            realizadas.append([4,5])
                            print u'Se realizó revision que no incluye material...'
                    except: pass
            elif act.tipoDeSolicitud_id==13:
                try:
                    if self.data['directo']:
                        realizadas.append([6,2])
                        print 'Directo...'
                except:
                    realizadas.append([2,2])
                    print 'Cambio de Medidor...'
                try:
                    if realizadas.index([5,7])>=0:
                        print 'desgloce de Gis...'
                except:
                    realizadas.append([5,7])
                    print 'se agregó desgloce de Gis...'


        for a in realizadas:
            try:
                actDeta = detalleDeActividad(
                    rubro=detalleRubro.objects.get(
                        servicio__id=a[0],
                        rubro__id=a[1],
                        contrato=contrato
                    ),
                    actividad=act
                )
                actDeta.save()
            except:
                print 'nose pudo guardar :' + str(a)



        print 'Guardado completo de Actividad...id : %s ' % act.id
        return act





    def rellenarDetalle(self, actividad, contrato):
        #try:
        self.fields['codigoDeCliente'].initial=actividad.cliente.cuenta
        self.fields['nombreDeCliente'].initial=actividad.cliente.nombre
        self.fields['cedula'].initial=actividad.cliente.ci_ruc
        self.fields['estadoCli'].initial=actividad.cliente.estado
        self.fields['telefono'].initial=actividad.cliente.telefono

        if actividad.tipoDeSolicitud_id!=1:
            self.fields['lugar'].initial=actividad.cliente.ubicacionGeografica.parroquia
            self.fields['calle'].initial=actividad.cliente.ubicacionGeografica.calle.descripcion1
            self.fields['geocodigo'].initial=actividad.cliente.geocodigo
        else:
            ref = list(detalleClienteReferencia.objects.filter(
                cliente=actividad.cliente
            ))[0]
            m = list(detalleClienteMedidor.objects.filter(
                cliente=ref.referencia,
                #medidor=ref.medidorDeReferencia
            ))[0].medidor
            self.fields['anterior'].initial=ref.medidorDeReferencia
            self.fields['serieAnteriror'].initial=m.serie
            self.fields['marcaAnteriror'].initial=m.marca
            self.fields['cuentaAnteriror'].initial=ref.referencia.cuenta

        miMed = list(medidor.objects.filter(actividad=actividad, contrato=None))
        if miMed:
            self.fields['fabricaRev'].initial=miMed[0].fabrica
            self.fields['serieRev'].initial=miMed[0].serie
            self.fields['marcaRev'].initial=miMed[0].marca
            self.fields['lecturaRev'].initial=miMed[0].lectura
        miMed = list(medidor.objects.filter(actividad=actividad, contrato__contrato=contrato))
        if miMed:
            self.fields['medidor'].initial=miMed[0]
            self.fields['fabricaInst'].initial=miMed[0].fabrica
            self.fields['serieInst'].initial=miMed[0].serie
            self.fields['marcaInst'].initial=miMed[0].marca
            self.fields['tipoDeMedidor'].initial=miMed[0].tipo
            self.fields['lecturaInst'].initial=miMed[0].lectura

        self.fields['tipoDeSolicitud'].initial=actividad.tipoDeSolicitud
        self.fields['motivoParaSolicitud'].initial=actividad.motivoDeSolicitud
        self.fields['fecha'].initial=actividad.fechaDeActividad
        self.fields['hora'].initial=actividad.horaDeActividad
        self.fields['instalador'].initial=actividad.instalador.nombre
        self.fields['cuadrilla'].initial=actividad.instalador.cuadrilla
        self.fields['materialDeLaRed'].initial=actividad.materialDeLaRed
        self.fields['formaDeConexion'].initial=actividad.formaDeConexion
        self.fields['estadoDeUnaInstalacion'].initial=actividad.estadoDeLaInstalacion
        self.fields['tipoDeConstruccion'].initial=actividad.tipoDeConstruccion
        self.fields['ubicacionDelMedidor'].initial=actividad.ubicacionDelMedidor
        self.fields['tipoDeAcometidaRed'].initial=actividad.tipoDeAcometidaRed
        self.fields['calibreDeLaRed'].initial=actividad.calibreDeLaRed
        self.fields['usoDeEnergia'].initial=actividad.usoDeEnergia
        self.fields['claseRed'].initial=actividad.claseRed
        self.fields['tipoDeServicio'].initial=actividad.tipoDeServicio
        self.fields['usoEspecificoDelInmueble'].initial=actividad.usoEspecificoDelInmueble
        self.fields['demanda'].initial=actividad.demanda
        self.fields['nivelSocieconomico'].initial=actividad.nivelSocieconomico
        self.fields['observaciones'].initial=actividad.observaciones
        try:
            if len(list(detalleDeActividad.objects.filter(
                actividad=actividad,
                rubro=detalleRubro.objects.get(
                    contrato=contrato,
                    servicio__id=3,
                    rubro__id=1
                ))))>0:
                self.fields['reubicacion'].initial=True
        except: pass
        try:
            if len(list(detalleDeActividad.objects.filter(
                actividad=actividad,
                rubro=detalleRubro.objects.get(
                    contrato=contrato,
                    servicio__id=4,
                    rubro__id=4
                ))))>0:

                self.fields['contrastacion'].initial=True
        except: pass
        try:
            if len(list(detalleDeActividad.objects.filter(
                actividad=actividad,
                rubro=detalleRubro.objects.get(
                    contrato=contrato,
                    servicio__id=6,
                    rubro__id=2
            ))))>0:
                self.fields['directo'].initial=True
        except: pass

        #sellos de actividad...
        s = list(sello.objects.filter(utilizado__id=actividad.id))
        ubi = ((i.ubicacion, i.ubicacion) for i in s)
        se = ((i.id, i) for i in s)

        self.fields['sellosSeleccionados'] = forms.MultipleChoiceField(
            choices=se,
            widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
            label='',
            required=True,
        )
        self.fields['ubiSellosSeleccionados'] = forms.MultipleChoiceField(
            choices=ubi,
            widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
            label='',
            required=True,
        )

        #materiales de actividad...
        s = list(materialDeActividad.objects.filter(actividad__id=actividad.id))
        cant = ((i.cantidad, i.cantidad) for i in s)
        mate = ((i.id, i.material) for i in s)

        self.fields['materialesSeleccionados'] = forms.MultipleChoiceField(
            choices=mate,
            widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
            label='',
            required=True,
        )
        self.fields['cantMaterialesSeleccionados'] = forms.MultipleChoiceField(
            choices=cant,
            widget=forms.SelectMultiple(attrs={'style': 'height: 1px; padding: 0; margin: 0; border: 0;'}),
            label='',
            required=True,
        )

        self.fields['id'].initial = actividad.id




    def clean(self):
        cleaned_data = super(ingresoForm, self).clean()

        try:
            del self.errors['sellosSeleccionados']
            del self.errors['materialesSeleccionados']
            del self.errors['ubiSellosSeleccionados']
            del self.errors['cantMaterialesSeleccionados']
        except:
            pass

        ts = self.data['tipoDeSolicitud']
        if ts == '11' or ts == '13':
            if not self.data['codigoDeCliente'].strip():
                self._errors["Cuenta"] = self.error_class([u"Ingrese un número de Cuenta."])
            if not self.data['serieRev'].strip():
                self._errors["Medidor"] = self.error_class([u"El Cliente debe tener un medidor activo."])
            if ts == '13':
                if not str(self.data['lecturaRev']).strip():
                    self._errors["Lectura"] = self.error_class([u"Ingrese una Lectura de Desconección "])
        if ts == '1' or ts == '13':
            if not self.data['tipoDeMedidor']:
                self._errors["Medidor"] = self.error_class([u" Seleccione el medidor a instalar "])
            if ts == '1':
                if not str(self.data['cuentaAnteriror']):
                    self._errors["Referencia"] = self.error_class(
                        [u"Ingrese la referencia de instalación del Servicio nuevo "])

        return cleaned_data



class BuscarActividad(forms.Form):
    criterio = forms.ChoiceField(choices=(('1','Cuenta'),('2','Medidor'),('3', 'Instalador')),
        label=' Criterio :  ',
        required=True
    )
    dato = forms.CharField(
        max_length=20, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Escriba dato a buscar'}),
        required=True
    )


class FotoForm(forms.Form):
    foto = forms.FileField(
        label='Seleccione una Foto...'
    )