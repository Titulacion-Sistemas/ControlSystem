import decimal
from django.shortcuts import render_to_response
from ControlSystem.pComm.conexion import manejadorDeConexion
from busquedas.models import BusquedaForm, vitacoraBusquedas, Buscado
from ingresos.models import cliente, secuencia, ruta, sector, canton, provincia


def llenarCliente(sesion, cli):
    if isinstance(cli, cliente):
        cli.ci_ruc = sesion.autECLPS.GetText(4, 10, 13)
        cli.cuenta = sesion.autECLPS.GetText(3, 27, 7)
        cli.nombre = sesion.autECLPS.GetText(3, 35, 30)
        cli.ci_ruc = sesion.autECLPS.GetText(4, 10, 13)
        cli.direccion = sesion.autECLPS.GetText(14, 18, 50)
        cli.estado = sesion.autECLPS.GetText(21, 42, 20)
        cli.geocodigo = secuencia(
            id=1000000000,
            num=int(sesion.autECLPS.GetText(20, 73, 7)),
            ruta=ruta(
                id=1000000000,
                num=int(sesion.autECLPS.GetText(20, 7, 3)),
                descripcion=sesion.autECLPS.GetText(20, 11, 30),
                sector=sector(
                    id=1000000000,
                    num=int(sesion.autECLPS.GetText(19, 13, 2)),
                    descripcion=sesion.autECLPS.GetText(19, 16, 40),
                    canton=canton(
                        id=1000000000,
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
        print(cli.geocodigo)
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


class buscar:
    def __init__(self):
        self.conn = manejadorDeConexion()

    def porCuenta(self, conexion, cuenta):
        self.conn.setActiveSession(conexion)
        sesion = self.conn.activeSession

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

        coincidencias.insert(0, llenarCliente(sesion, coincidencias[0]))

        titulo = sesion.autECLPS.GetText(9, 16, 20)
        while titulo != 'CONSULTA DE CLIENTES':
            print titulo
            sesion.autECLPS.SendKeys('[pf12]')
            sesion.autECLOIA.WaitForAppAvailable()
            sesion.autECLOIA.WaitForInputReady()
            titulo = sesion.autECLPS.GetText(9, 16, 20)

        form = Buscado(instance=coincidencias[0])

        data = {
            'formulario': form,
            'coincidencias': coincidencias,
        }
        return render_to_response('busqueda/porCuenta.html', data)
