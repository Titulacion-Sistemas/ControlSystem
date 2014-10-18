from django.shortcuts import render_to_response
from ControlSystem.pComm.conexion import manejadorDeConexion
from busquedas.models import BusquedaForm
from ingresos.models import cliente


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
                id=i-9,
                cuenta=sesion.autECLPS.GetText(i, 5, 7),
                nombre=sesion.autECLPS.GetText(i, 13, 23),
                direccion=sesion.autECLPS.GetText(i, 37, 16),
                deuda=sesion.autECLPS.GetText(i, 59, 8),
                meses=sesion.autECLPS.GetText(i, 68, 4)
                )
            )

        #mas busquedas

        titulo = sesion.autECLPS.GetText(9, 16, 20)
        while titulo != 'CONSULTA DE CLIENTES':
            print titulo
            sesion.autECLPS.SendKeys('[pf12]')
            sesion.autECLOIA.WaitForAppAvailable()
            sesion.autECLOIA.WaitForInputReady()
            titulo = sesion.autECLPS.GetText(9, 16, 20)


        form = BusquedaForm()
        data = {
            'formulario': form,
            'coincidencias': coincidencias,
        }
        return render_to_response('busqueda/porCuenta.html', data)
