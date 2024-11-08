import dbus


bus = dbus.SessionBus()


services = bus.list_names()

for s in services:
    print(s)

# OR

proxy = bus.get_object('org.freedesktop.DBus', '/org/freedesktop/DBus')
method = proxy.get_dbus_method('ListNames', 'org.freedesktop.DBus')

print(method())

# OR 

method = proxy.ListNames()