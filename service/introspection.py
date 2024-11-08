import dbus


bus = dbus.SessionBus()

# interfaces and object for logger
interface = 'org.meks.Logger'
object = '/Logger'


# get proxy
proxy = bus.get_object(interface, object)

print(proxy.GetLogCount())