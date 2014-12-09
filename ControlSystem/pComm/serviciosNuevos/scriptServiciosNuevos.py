from ControlSystem.pComm.conexion import manejadorDeConexion

__author__ = 'Jhonsson'



class ingresarServicioNuevo():
    def __init__(self, conexion):
        self.conn = manejadorDeConexion()
        self.conn.setActiveSession(conexion)
        self.sesion = self.conn.activeSession