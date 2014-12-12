# coding=utf-8
from django.contrib.humanize.tests import now
from ControlSystem.pComm.conexion import manejadorDeConexion
from ingresos.models import *
from inventario.models import *

__author__ = 'Jhonsson'


class ingresarServicioNuevo():
    def __init__(self, conexion, contrato):
        self.conn = manejadorDeConexion()
        self.conn.setActiveSession(conexion)
        self.sesion = self.conn.activeSession
        self.contrato = contrato
        self.ERROR = {
            'estado': None,
            'mensaje': 'Error no se pudo completar la acción requerida......',
            'solicitud': None
        }

    def elegirPunto(self, estado):
        pass

    def pasoUno(self, actividad, contrato):
        sesion = self.sesion
        opcionSico = False
        sesion.autECLPS.SetCursorPos(9, 12)
        for i in range(9, 20):
            if sesion.autECLPS.GetText(i, 16, 18) == 'ATENCION DE SOLICITUDES' \
                or (str(sesion.autECLPS.GetText(i, 52, 3)).strip() == '30'
                    and str(sesion.autECLPS.GetText(i, 63, 2)).strip() == '5'):
                self.cambiosDeMedidor = i
                sesion.autECLPS.SendKeys('5', i, 12)
                opcionSico = True
                break
            else:
                sesion.autECLPS.SendKeys('[down]')
        if opcionSico:

            sesion.autECLPS.SendKeys('[enter]')

            opcionSico = False
            sesion.autECLPS.SetCursorPos(9, 12)
            for i in range(9, 20):
                if sesion.autECLPS.GetText(i, 7, 43) == 'RECEPCION DE SOLICITUDES Y TRAMITES (NUEVO)' \
                    or (str(sesion.autECLPS.GetText(i, 58, 8)).strip() == 'PTRBSOLS'
                        and str(sesion.autECLPS.GetText(i, 62, 2)).strip() == '5'):
                    self.solicitudesNuevo = i
                    sesion.autECLPS.SendKeys('1', i, 3)
                    opcionSico = True
                    break
                else:
                    sesion.autECLPS.SendKeys('[down]')
            if opcionSico:

                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('[pf6]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                sesion.autECLPS.SendKeys('[eraseeof]', 11, 37)
                sesion.autECLPS.SendKeys(str(actividad.tipoDeSolicitud_id), 11, 37)
                sesion.autECLPS.SendKeys('[eraseeof]', 13, 37)
                sesion.autECLPS.SendKeys(str(actividad.motivoDeSolicitud_id), 13, 37)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                sesion.autECLPS.SendKeys(str(actividad.cliente.tipo), 8, 45)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                sesion.autECLPS.SendKeys(str(actividad.cliente.ci_ruc), 7, 39)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                if str(sesion.autECLPS.GetText(9, 7, 25)).strip()=='':
                    nomb = str(actividad.cliente.nombre).split(' ')
                    cant=int(len(nomb)/2)
                    sesion.autECLPS.SendKeys(str(' '.join(nomb[:c])), 9, 7)
                    sesion.autECLPS.SendKeys(str(' '.join(nomb[c:])), 10, 7)
                if str(sesion.autECLPS.GetText(12, 7, 9)).strip()=='':
                    sesion.autECLPS.SendKeys('1',12,7)
                if str(sesion.autECLPS.GetText(12, 64, 9)).strip()=='':
                    sesion.autECLPS.SendKeys('1',12,64)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                ref=list(detalleClienteReferencia.objects.filter(cliente=actividad.cliente))[0].referencia
                prov = '%02d' % ref.geocodigo.ruta.sector.canton.provincia.id
                cant = '%02d' % ref.geocodigo.ruta.sector.canton.num
                parr = '%02d' % ref.ubicacionGeografica.parroquia.num
                sesion.autECLPS.SendKeys(prov,6,28)
                sesion.autECLPS.SendKeys(cant,7,28)
                sesion.autECLPS.SendKeys(parr,8,28)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('C',4,58)
                sesion.autECLPS.SendKeys('CA',10,28)
                sesion.autECLPS.SendKeys('[pf4]',11,28)
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                sesion.autECLPS.SendKeys(ref.ubicacionGeografica.calle.descripcion1,5,36)
                sesion.autECLPS.SendKeys('1',6,4)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                #posiblemente borrar todos los ceros a la izquierda
                sesion.autECLPS.SendKeys(str(ref.geocodigo)[6:16]+'.'+str(ref.geocodigo)[16:], 9, 27)
                med = medidor.objects.get(actividad=actividad, contrato=self.contrato)
                sesion.autECLPS.SendKeys('1', 14, 32)
                if med.voltaje==120:
                    sesion.autECLPS.SendKeys('2', 14, 35)
                else:
                    sesion.autECLPS.SendKeys('3', 14, 35)
                sesion.autECLPS.SendKeys('B', 14, 38)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                modeloMed = str(med.modelo.id).split('-')
                sesion.autECLPS.SendKeys(modeloMed[0],5,30)
                sesion.autECLPS.SendKeys('[eraseeof]', 5, 34)
                sesion.autECLPS.SendKeys(modeloMed[1],5,34)
                sesion.autECLPS.SendKeys('[eraseeof]', 7, 30)
                sesion.autECLPS.SendKeys(actividad.formaDeConexion_id, 7, 30)
                sesion.autECLPS.SendKeys('[eraseeof]', 9, 30)
                sesion.autECLPS.SendKeys('1', 9, 30)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                actividad.numeroDeSolicitud=int(str(sesion.autECLPS.GetText(10, 69, 7)).strip())
                actividad.estadoDeSolicitud = estadoDeSolicitud.objects.get(id=1)
                actividad.save(force_update=True)

                titulo = sesion.autECLPS.GetText(9, 16, 20)
                while titulo != 'CONSULTA DE CLIENTES':
                    sesion.autECLPS.SendKeys('[pf12]')
                    sesion.autECLOIA.WaitForAppAvailable()
                    sesion.autECLOIA.WaitForInputReady()
                    titulo = sesion.autECLPS.GetText(9, 16, 20)

                return {
                    'estado': actividad.estadoDeSolicitud_id,
                    'mensaje': 'Solicitud creada correctamente',
                    'solicitud': actividad.numeroDeSolicitud
                }

            else:
                titulo = sesion.autECLPS.GetText(9, 16, 20)
                while titulo != 'CONSULTA DE CLIENTES':
                    sesion.autECLPS.SendKeys('[pf12]')
                    sesion.autECLOIA.WaitForAppAvailable()
                    sesion.autECLOIA.WaitForInputReady()
                    titulo = sesion.autECLPS.GetText(9, 16, 20)

                return self.ERROR
        else:
            return self.ERROR


    def pasoDos(self, actividad):
        sesion = self.sesion
        opcionSico = False
        sesion.autECLPS.SetCursorPos(9, 12)
        for i in range(9, 20):
            if sesion.autECLPS.GetText(i, 16, 12) == 'INSPECCIONES' \
                or (str(sesion.autECLPS.GetText(i, 52, 3)).strip() == '8'
                    and str(sesion.autECLPS.GetText(i, 63, 2)).strip() == '50'):
                self.cambiosDeMedidor = i
                sesion.autECLPS.SendKeys('5', i, 12)
                opcionSico = True
                break
            else:
                pass
        if opcionSico:

            sesion.autECLPS.SendKeys('[enter]')

            opcionSico = False
            sesion.autECLPS.SetCursorPos(9, 12)
            for i in range(9, 20):
                if sesion.autECLPS.GetText(i, 7, 38) == 'IMPRESION DE FORMULARIOS DE INSPECCION' \
                    or (str(sesion.autECLPS.GetText(i, 58, 8)).strip() == 'PCLCUIMF'
                        and str(sesion.autECLPS.GetText(i, 62, 2)).strip() == '5'):
                    self.solicitudesNuevo = i
                    sesion.autECLPS.SendKeys('1', i, 3)
                    opcionSico = True
                    break
                else:
                    pass
            if opcionSico:

                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('[eraseeof]', 8, 5)
                sesion.autECLPS.SendKeys(str(actividad.numeroDeSolicitud), 8, 5)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('6')
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                actividad.estadoDeSolicitud = estadoDeSolicitud.objects.get(id=6)
                actividad.save(force_update=True)

                titulo = sesion.autECLPS.GetText(9, 16, 20)
                while titulo != 'CONSULTA DE CLIENTES':
                    sesion.autECLPS.SendKeys('[pf12]')
                    sesion.autECLOIA.WaitForAppAvailable()
                    sesion.autECLOIA.WaitForInputReady()
                    titulo = sesion.autECLPS.GetText(9, 16, 20)

                return {
                    'estado': actividad.estadoDeSolicitud_id,
                    'mensaje': 'Solicitud enviada para impresion al servidor',
                    'solicitud': actividad.numeroDeSolicitud
                }
            else:
                titulo = sesion.autECLPS.GetText(9, 16, 20)
                while titulo != 'CONSULTA DE CLIENTES':
                    sesion.autECLPS.SendKeys('[pf12]')
                    sesion.autECLOIA.WaitForAppAvailable()
                    sesion.autECLOIA.WaitForInputReady()
                    titulo = sesion.autECLPS.GetText(9, 16, 20)

                return self.ERROR
        else:
            return self.ERROR


    def pasoTres(self, actividad):
        sesion = self.sesion
        opcionSico = False
        sesion.autECLPS.SetCursorPos(9, 12)
        for i in range(9, 20):
            if sesion.autECLPS.GetText(i, 16, 12) == 'INSPECCIONES' \
                or (str(sesion.autECLPS.GetText(i, 52, 3)).strip() == '8'
                    and str(sesion.autECLPS.GetText(i, 63, 2)).strip() == '50'):
                self.cambiosDeMedidor = i
                sesion.autECLPS.SendKeys('5', i, 12)
                opcionSico = True
                break
            else:
                pass
        if opcionSico:

            sesion.autECLPS.SendKeys('[enter]')

            opcionSico = False
            sesion.autECLPS.SetCursorPos(9, 12)
            for i in range(9, 20):
                if sesion.autECLPS.GetText(i, 7, 38) == 'DIGITAR PRIMERA INSPECCION' \
                    or (str(sesion.autECLPS.GetText(i, 58, 8)).strip() == 'PDIPRIN'
                        and str(sesion.autECLPS.GetText(i, 62, 2)).strip() == '20'):
                    self.solicitudesNuevo = i
                    sesion.autECLPS.SendKeys('1', i, 3)
                    opcionSico = True
                    break
                else:
                    pass
            if opcionSico:

                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                sesion.autECLPS.SendKeys(str(actividad.numeroDeSolicitud), 8, 6)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('1')
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('[eraseeof]')
                sesion.autECLPS.SendKeys(str(contrato.codigoInstalador),8,33)
                sesion.autECLPS.SendKeys('[pf4]', 9, 33)
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                ref=list(detalleClienteReferencia.objects.filter(cliente=actividad.cliente))[0].referencia
                meref=detalleClienteMedidor.objects.filter(
                    cliente=ref,
                    medidor__contrato=None,
                    medidor__actividad=actividad
                )[0].medidor
                sesion.autECLPS.SendKeys(str(meref.febrica), 5, 15)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                if str(sesion.autECLPS.GetText(16, 14, 11)).strip()==str(meref.febrica):
                    sesion.autECLPS.SendKeys('1')
                    sesion.autECLPS.SendKeys('[enter]')
                    sesion.autECLOIA.WaitForAppAvailable()
                    sesion.autECLOIA.WaitForInputReady()
                else:
                    return self.ERROR

                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                sesion.autECLPS.SendKeys('S', 7, 72)
                sesion.autECLPS.SendKeys(str(actividad.materialDeLaRed_id), 8, 30)
                sesion.autECLPS.SendKeys(str(actividad.estadoDeLaInstalacion_id), 9, 30)
                sesion.autECLPS.SendKeys('[eraseeof]', 10, 30)
                sesion.autECLPS.SendKeys(str(actividad.tipoDeConstruccion_id), 10, 30)
                sesion.autECLPS.SendKeys('[eraseeof]', 11, 30)
                sesion.autECLPS.SendKeys(str(actividad.ubicacionDelMedidor_id), 11, 30)
                sesion.autECLPS.SendKeys('[eraseeof]', 12, 30)
                sesion.autECLPS.SendKeys(str(actividad.tipoDeAcometidaRed_id), 12, 30)
                sesion.autECLPS.SendKeys(str(actividad.tipoDeAcometidaRed_id), 13, 30)
                sesion.autECLPS.SendKeys('[eraseeof]', 14, 30)
                sesion.autECLPS.SendKeys(str(actividad.calibreDeLaRed_id), 14, 30)
                sesion.autECLPS.SendKeys(str(actividad.claseRed_id), 15, 30)
                med = medidor.objects.get(actividad=actividad, contrato=self.contrato)
                sesion.autECLPS.SendKeys('1', 16, 30)
                if med.voltaje==120:
                    sesion.autECLPS.SendKeys('2', 16, 34)
                else:
                    sesion.autECLPS.SendKeys('3', 16, 34)
                sesion.autECLPS.SendKeys('B', 16, 38)
                sesion.autECLPS.SendKeys(str(actividad.usoDeEnergia_id), 17, 30)
                sesion.autECLPS.SendKeys('[eraseeof]', 18, 30)
                sesion.autECLPS.SendKeys('[eraseeof]', 18, 34)
                sesion.autECLPS.SendKeys(str(actividad.usoEspecificoDelInmueble_id), 18, 30)
                sesion.autECLPS.SendKeys(str(actividad.usoEspecificoDelInmueble.usoGeneral_id), 18, 34)
                sesion.autECLPS.SendKeys(str(actividad.nivelSocieconomico_id), 19, 30)
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()
                sesion.autECLPS.SendKeys('[enter]')
                sesion.autECLOIA.WaitForAppAvailable()
                sesion.autECLOIA.WaitForInputReady()

                titulo = sesion.autECLPS.GetText(9, 16, 20)
                while titulo != 'CONSULTA DE CLIENTES':
                    sesion.autECLPS.SendKeys('[pf12]')
                    sesion.autECLOIA.WaitForAppAvailable()
                    sesion.autECLOIA.WaitForInputReady()
                    titulo = sesion.autECLPS.GetText(9, 16, 20)

                return {
                    'estado': actividad.estadoDeSolicitud_id,
                    'mensaje': 'Ruta asignada a Servicio Nuevo',
                    'solicitud': actividad.numeroDeSolicitud
                }


            else:
                titulo = sesion.autECLPS.GetText(9, 16, 20)
                while titulo != 'CONSULTA DE CLIENTES':
                    sesion.autECLPS.SendKeys('[pf12]')
                    sesion.autECLOIA.WaitForAppAvailable()
                    sesion.autECLOIA.WaitForInputReady()
                    titulo = sesion.autECLPS.GetText(9, 16, 20)

                return self.ERROR
        else:
            return self.ERROR


    def pasoCuatro(self, actividad, contrato):
        pass
        #32:25