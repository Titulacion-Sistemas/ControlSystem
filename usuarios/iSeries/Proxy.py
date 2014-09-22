from usuarios import iSeries

__author__ = 'JC'

conn = iSeries.ConnectionManager()
availableConnections = conn.getAvailableConnections()

selected = 0
# ask user to select a connection if there are more than one available
if len(availableConnections) > 1:
    selected = 1
elif len(availableConnections) == 1:
    selected = 0

# open and set active session
print availableConnections
conn.openSession(availableConnections[selected])
conn.setActiveSession(availableConnections[selected])




