__author__ = 'Jhonsson'
from time import sleep
import win32com
import win32com.client

__author__ = 'JC'

class ConnectionManager:
  def __init__(self):
    """

    :rtype : object
    """
    self.PCommConnMgr = win32com.client.Dispatch('PCOMM.autECLConnMgr')
    self.connList = self.PCommConnMgr.autECLConnList
    self.activeSession = None
    self.sessions = {}
    self.connection = ''
    self.estado = False

  def setActiveSession(self, connectionName):
    self.activeSession = self.sessions[connectionName]

  # return value from screen at position (row, col)
  def getText(self, row, col, length= None, session= None):
    result = None
    tempSession= self.activeSession
    if session is not None:
      tempSession= self.sessions[session]

    if length is None:
      tempSession.autECLPS.autECLFieldList.Refresh()
      field = tempSession.autECLPS.autECLFieldList.FindFieldByRowCol(row, col)
      length = field.Length
    result = tempSession.autECLPS.GetText(row, col, length)
    return result

  def sendKeys(self, count, key, row= None, col= None, session= None):
    n = 0
    while n< count:
        tempSession= self.activeSession
        if session is not None:
            tempSession= self.sessions[session]
        if row is None or col is None:
            tempSession.autECLPS.SendKeys("%s" % key)
        else:
            tempSession.autECLPS.SendKeys("%s" % key, row, col)
        tempSession.autECLOIA.WaitForAppAvailable()
        tempSession.autECLOIA.WaitForInputReady()
        n+= 1

  def getAvailableConnection(self):
    self.connList.Refresh()
    self.connection= chr(self.connList.Count+65)
    self.openProgram()
    self.connList.Refresh()
    return self.connection

  def openSession(self, session, usuario="Gronquillo", contrasenia="jcesar1"):
    _session= win32com.client.Dispatch("PCOMM.autECLSession")
    #_ecloia= win32com.client.Dispatch("PCOMM.autECLOIA")
    _session.SetConnectionByName(session)
    #_ecloia.SetConnectionByName(session)
    self.sessions[session] = _session
    segundos = 5
    while not _session.Ready and segundos >= 0:
        print "la session no esta lista aun ..."
        #return False
        sleep(1)
        segundos = segundos - 1

    if segundos>=0:
        _session.autECLOIA.WaitForAppAvailable()
        _session.autECLOIA.WaitForInputReady()
        print self.getText( 22, 50, length= 8, session= session)
        print self.getText( 21, 50, length= 12, session= session)
        if str(self.getText( 21, 50, length= 12, session= session))=='USUARIO    :' and str(self.getText( 22, 50, length= 8, session= session))=='CONTRASE':
            self.sendKeys(1, usuario, row= 21, col= 63, session= session)
            self.sendKeys(1, contrasenia, row= 22, col= 63, session= session)
            self.sendKeys(6, '[enter]', session= session)
            self.estado = True

  def openProgram(self):
      print "Abriendo el Programa, Sesion: {0}".format(self.connection)
      self.PCommConnMgr.StartConnection("PROFILE=.\usuarios\iSeries\sico\CNEL.WS CONNNAME={0} WINSTATE=MIN".format(self.connection))
      # shell = win32com.client.Dispatch('WScript.Shell')
      # sleep(3)
      # shell.SendKeys(usuario, 0)
      # shell.SendKeys("{tab}", 0)
      # shell.SendKeys(contrasenia, 0)
      # shell.SendKeys("{enter}", 0)
      # sleep(15)