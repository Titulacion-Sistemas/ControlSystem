# coding=utf-8

import decimal
from django.shortcuts import render_to_response
import pythoncom
from ControlSystem.pComm.conexion import manejadorDeConexion
from busquedas.models import ClienteBuscado, MedidorBuscado
from ingresos.models import cliente, secuencia, ruta, sector, canton, provincia, parroquia, ubicacion, calle, urbanizacion
from inventario.models import medidor


def llenarCliente(sesion, cli):
    if isinstance(cli, cliente):
        cli = cliente()
        cli.ci_ruc = sesion.autECLPS.GetText(4, 10, 13)
        cli.cuenta = sesion.autECLPS.GetText(3, 27, 7)
        cli.nombre = sesion.autECLPS.GetText(3, 35, 30)
        #cli.direccion = sesion.autECLPS.GetText(14, 18, 50)
        #cli.interseccion = sesion.autECLPS.GetText(15, 18, 50)
        #cli.urbanizacion = sesion.autECLPS.GetText(16, 18, 50)
        cli.estado = sesion.autECLPS.GetText(21, 42, 20)
        cli.geocodigo = secuencia(
            num=int(sesion.autECLPS.GetText(20, 73, 7)),
            ruta=ruta(
                num=int(sesion.autECLPS.GetText(20, 7, 3)),
                descripcion=sesion.autECLPS.GetText(20, 11, 30),
                sector=sector(
                    num=int(sesion.autECLPS.GetText(19, 13, 2)),
                    descripcion=sesion.autECLPS.GetText(19, 16, 40),
                    canton=canton(
                        num=int(sesion.autECLPS.GetText(18, 45, 2)),
                        descripcion=sesion.autECLPS.GetText(18, 48, 20),
                        provincia=provincia(
                            id=int(sesion.autECLPS.GetText(18, 13, 2)),
                            descripcion=sesion.autECLPS.GetText(18, 16, 20)
                        )
                    )
                )
            )
        )
        cli.ubicacionGeografica = ubicacion(
            parroquia=parroquia(
                id=int(sesion.autECLPS.GetText(13, 13, 2)),
                descripcion=sesion.autECLPS.GetText(13, 17, 35)
            ),
            calle=calle(
                descripcion=sesion.autECLPS.GetText(14, 18, 50),
            ),
            intercepcion=calle(
                descripcion=sesion.autECLPS.GetText(15, 18, 50),
            ),
            urbanizacion=urbanizacion(
                descripcion=sesion.autECLPS.GetText(16, 18, 50)
            )
        )
        #print(cli.geocodigo)
    sesion.autECLPS.SendKeys('[pf2]')
    sesion.autECLOIA.WaitForAppAvailable()
    sesion.autECLOIA.WaitForInputReady()

    cli.meses = sesion.autECLPS.GetText(12, 45, 3)
    cli.deuda = decimal.Decimal(sesion.autECLPS.GetText(15, 22, 12))

    sesion.autECLPS.SendKeys('[pf12]')
    sesion.autECLOIA.WaitForAppAvailable()
    sesion.autECLOIA.WaitForInputReady()

    for j in range(3):
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()

    sesion.autECLPS.SendKeys('[pf12]')
    sesion.autECLOIA.WaitForAppAvailable()
    sesion.autECLOIA.WaitForInputReady()

    return cli


def llenarMedidores(sesion):
    medidores = []
    it = 9
    fab = sesion.autECLPS.GetText(it, 28, 1)
    while fab != " ":
        sesion.autECLPS.SendKeys("1")
        sesion.autECLPS.SendKeys("[enter]")
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys("[down]")
        medidores.append(
            MedidorBuscado(
                sesion.autECLPS.GetText(6, 29, 20),
                sesion.autECLPS.GetText(16, 29, 18),
                (sesion.autECLPS.GetText(17, 29, 23)).encode('utf-8'),
                sesion.autECLPS.GetText(18, 29, 17),
                sesion.autECLPS.GetText(8, 29, 10),
                sesion.autECLPS.GetText(9, 29, 10),
                sesion.autECLPS.GetText(8, 68, 9),
                sesion.autECLPS.GetText(9, 68, 9),
                instance=medidor(
                    fabrica=sesion.autECLPS.GetText(7, 29, 11),
                    serie=sesion.autECLPS.GetText(10, 29, 11),
                    tipo=sesion.autECLPS.GetText(5, 29, 16),
                    digitos=sesion.autECLPS.GetText(11, 29, 2),
                    fases=sesion.autECLPS.GetText(11, 68, 2),
                    hilos=sesion.autECLPS.GetText(12, 29, 2)
                )
            )
        )
        sesion.autECLPS.SendKeys("[pf12]")
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        #sesion.autECLPS.Wait(900)
        sesion.autECLPS.SendKeys("[down]")
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        it += 1
        fab = sesion.autECLPS.GetText(it, 28, 1)

    return medidores


class buscar:
    def __init__(self, conexion):
        self.conn = manejadorDeConexion()
        self.conn.setActiveSession(conexion)
        self.sesion = self.conn.activeSession


    #busqueda por cuenta
    def porCuenta(self, cuenta):
        sesion = self.sesion
        sesion.autECLPS.SendKeys('5', 9, 12)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('1', 9, 3)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('[eraseeof]', 9, 5)
        sesion.autECLPS.SendKeys(str(cuenta), 9, 5)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        coincidencias = []

        for i in range(10, 21):
            if sesion.autECLPS.GetText(i, 5, 7).strip() != "":
                coincidencias.append(
                    cliente(
                        id=i - 9,
                        cuenta=sesion.autECLPS.GetText(i, 5, 7),
                        nombre=sesion.autECLPS.GetText(i, 13, 23),
                        direccion=sesion.autECLPS.GetText(i, 37, 16),
                        deuda=sesion.autECLPS.GetText(i, 59, 8),
                        meses=sesion.autECLPS.GetText(i, 68, 4)
                    )
                )

        sesion.autECLPS.SendKeys('1', 10, 3)
        for j in range(4):
            sesion.autECLPS.SendKeys('[enter]')
            sesion.autECLOIA.WaitForAppAvailable()
            sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('[pf2]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()

        coincidencias[0] = llenarCliente(sesion, coincidencias[0])

        sesion.autECLPS.SendKeys('9')
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()

        medidores = llenarMedidores(sesion)

        titulo = sesion.autECLPS.GetText(9, 16, 20)
        while titulo != 'CONSULTA DE CLIENTES':
            sesion.autECLPS.SendKeys('[pf12]')
            sesion.autECLOIA.WaitForAppAvailable()
            sesion.autECLOIA.WaitForInputReady()
            titulo = sesion.autECLPS.GetText(9, 16, 20)

        formC = ClienteBuscado(coincidencias[0].geocodigo, instance=coincidencias[0])

        data = {
            'cClientes': coincidencias,
            'formCliente': formC,
            'cMedidores': medidores,
        }

        return data

    #busqueda por medidor
    def porMedidor(self, medidor):
        sesion = self.sesion
        sesion.autECLPS.SendKeys('5', 9, 12)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('1', 9, 3)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('[pf9]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        for h in range(3):
            sesion.autECLPS.SendKeys("[up]")
        sesion.autECLPS.SendKeys('[tab]')
        sesion.autECLPS.SendKeys(str(medidor), 4, 43)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        coincidencias = []

        for i in range(7, 18):
            if sesion.autECLPS.GetText(i, 8, 11).strip() != "":
                coincidencias.append(
                    cliente(
                        id=i - 9,
                        urbanizacion=sesion.autECLPS.GetText(i, 8, 11),
                        estado=sesion.autECLPS.GetText(i, 20, 3),
                        cuenta=sesion.autECLPS.GetText(i, 24, 7),
                        nombre=sesion.autECLPS.GetText(i, 32, 25),
                        direccion=sesion.autECLPS.GetText(i, 58, 20)

                    )
                )

        sesion.autECLPS.SendKeys('2', 7, 4)
        #print 'se pulsoel 2'
        for j in range(4):
            sesion.autECLPS.SendKeys('[enter]')
            sesion.autECLOIA.WaitForAppAvailable()
            sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('[pf2]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()

        coincidencias.insert(0, llenarCliente(sesion, coincidencias[0]))

        sesion.autECLPS.SendKeys('1')
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('9')
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()

        medidores = llenarMedidores(sesion)

        titulo = sesion.autECLPS.GetText(9, 16, 20)
        while titulo != 'CONSULTA DE CLIENTES':
            sesion.autECLPS.SendKeys('[pf12]')
            sesion.autECLOIA.WaitForAppAvailable()
            sesion.autECLOIA.WaitForInputReady()
            titulo = sesion.autECLPS.GetText(9, 16, 20)

        formC = ClienteBuscado(coincidencias[0].geocodigo, instance=coincidencias[0])

        data = {
            'cClientes': coincidencias,
            'formCliente': formC,
            'cMedidores': medidores,
        }

        return data


    #busqueda por nombre
    def porNombre(self, nombre):
        sesion = self.sesion
        sesion.autECLPS.SendKeys('5', 9, 12)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('1', 9, 3)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('[pf8]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys(str(nombre)[:17], 8, 5)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        coincidencias = []

        for i in range(9, 21):
            if sesion.autECLPS.GetText(i, 5, 22).strip() != "":
                coincidencias.append(
                    cliente(
                        id=i - 9,
                        nombre=sesion.autECLPS.GetText(i, 5, 22),
                        direccion=sesion.autECLPS.GetText(i, 28, 17),
                        cuenta=sesion.autECLPS.GetText(i, 46, 7),
                        deuda=sesion.autECLPS.GetText(i, 59, 8),
                        meses=sesion.autECLPS.GetText(i, 68, 3)
                    )
                )

        sesion.autECLPS.SendKeys('1', 9, 3)
        for j in range(4):
            sesion.autECLPS.SendKeys('[enter]')
            sesion.autECLOIA.WaitForAppAvailable()
            sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('[pf2]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()

        coincidencias[0] = llenarCliente(sesion, coincidencias[0])

        sesion.autECLPS.SendKeys('9')
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()

        medidores = llenarMedidores(sesion)

        titulo = sesion.autECLPS.GetText(9, 16, 20)
        while titulo != 'CONSULTA DE CLIENTES':
            sesion.autECLPS.SendKeys('[pf12]')
            sesion.autECLOIA.WaitForAppAvailable()
            sesion.autECLOIA.WaitForInputReady()
            titulo = sesion.autECLPS.GetText(9, 16, 20)

        formC = ClienteBuscado(coincidencias[0].geocodigo, instance=coincidencias[0])

        data = {
            'cClientes': coincidencias,
            'formCliente': formC,
            'cMedidores': medidores,
        }

        return data


    #busqueda por ruta de lectura
    def porGeocodigo(self, geocodigo):
        sesion = self.sesion
        sesion.autECLPS.SendKeys('5', 9, 12)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('1', 12, 3)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('[pf8]', 9, 5)
        geocodigo=geocodigo.split(".")
        sesion.autECLPS.SendKeys('[up]')
        sesion.autECLPS.SendKeys('[tab]')
        sesion.autECLPS.SendKeys(str('%02d' % (int(geocodigo[0]))), 8, 6)
        sesion.autECLPS.SendKeys('[tab]')
        sesion.autECLPS.SendKeys(str('%02d' % (int(geocodigo[1]))), 8, 11)
        sesion.autECLPS.SendKeys('[tab]')
        sesion.autECLPS.SendKeys(str('%02d' % (int(geocodigo[2]))), 8, 18)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('7', 9, 3)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('[up]')
        sesion.autECLPS.SendKeys('[tab]')
        sesion.autECLPS.SendKeys('[eraseeof]')
        sesion.autECLPS.SendKeys(str('%03d' % (int(geocodigo[3]))), 8, 6)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('8', 9, 2)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('[up]')
        sesion.autECLPS.SendKeys('[tab]')
        sesion.autECLPS.SendKeys('[eraseeof]', 8, 5)
        sesion.autECLPS.SendKeys(str('%07d' % (int(geocodigo[4]))), 8, 5)
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()
        ruta = str(sesion.autECLPS.GetText(4, 16, 13)).strip()
        coincidencias = []

        for i in range(9, 21):
            if sesion.autECLPS.GetText(i, 5, 7).strip() != "":
                coincidencias.append(
                    cliente(
                        id=i - 9,
                        interseccion=ruta+'.'+str(sesion.autECLPS.GetText(i, 5, 7)).strip(),
                        cuenta=sesion.autECLPS.GetText(i, 13, 7),
                        nombre=sesion.autECLPS.GetText(i, 21, 16),
                        direccion=sesion.autECLPS.GetText(i, 38, 14),
                        urbanizacion=sesion.autECLPS.GetText(i, 53, 10),
                        deuda=sesion.autECLPS.GetText(i, 68, 8)
                    )
                )

        sesion.autECLPS.SendKeys('1', 9, 3)
        for j in range(4):
            sesion.autECLPS.SendKeys('[enter]')
            sesion.autECLOIA.WaitForAppAvailable()
            sesion.autECLOIA.WaitForInputReady()
        sesion.autECLPS.SendKeys('[pf2]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()

        coincidencias.insert(0, llenarCliente(sesion, coincidencias[0]))

        sesion.autECLPS.SendKeys('9')
        sesion.autECLPS.SendKeys('[enter]')
        sesion.autECLOIA.WaitForAppAvailable()
        sesion.autECLOIA.WaitForInputReady()

        medidores = llenarMedidores(sesion)

        titulo = sesion.autECLPS.GetText(9, 16, 20)
        while titulo != 'CONSULTA DE CLIENTES':
            sesion.autECLPS.SendKeys('[pf12]')
            sesion.autECLOIA.WaitForAppAvailable()
            sesion.autECLOIA.WaitForInputReady()
            titulo = sesion.autECLPS.GetText(9, 16, 20)

        formC = ClienteBuscado(coincidencias[0].geocodigo, instance=coincidencias[0])

        data = {
            'cClientes': coincidencias,
            'formCliente': formC,
            'cMedidores': medidores,
        }

        return data

    def renderBusqueda(self, tipo, data):
        operaciones = {
            '1': self.porCuenta,
            '2': self.porMedidor,
            '3': self.porNombre,
            '4': self.porGeocodigo
        }

        data = operaciones[str(tipo)](data)
        data['tipo'] = tipo

        return render_to_response('busqueda/renderBusqueda.html', data)