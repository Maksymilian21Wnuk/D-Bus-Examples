from pydbus import SessionBus
from gi.repository import GLib

# connect to session bus
bus = SessionBus()


# two objects instances
OBJ_FST = '/org/meks/Logger/1'
OBJ_SND = '/org/meks/Logger/2'

# names of services and interfaces that are implemented by Logger
SERVICE_NAME = 'org.meks.Logger'
LOGGER_INTERFACE = 'org.meks.Logger'
PROPERTIES_INTERFACE = 'org.freedesktop.DBus.Properties'
INTR_IFACE = 'org.freedesktop.DBus.Introspectable'

# gets proxy of SERVICE_NAME belonging object /org/meks/Logger/1
proxy = bus.get(SERVICE_NAME, '/org/meks/Logger/1')








# get methods of logger iface
res = proxy[LOGGER_INTERFACE]

print(res.AddLog("Some log"))

# iface of properties
properties = proxy[PROPERTIES_INTERFACE]

# get all properties method example
print(properties.GetAll('org.meks.Logger'))

# won't change as LogCount is read only
#properties.Set('org.meks.Logger', 'LogCount', GLib.Variant('i', 1000))

# Upper wil change as it is read-write
#properties.Set('org.meks.Logger', 'Upper', GLib.Variant('b', True))

#print(res.AddLog("Some log"))
