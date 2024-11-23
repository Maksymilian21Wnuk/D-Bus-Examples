import dbus
import dbus.mainloop.glib
from gi.repository import GLib


def signal_handler(*args):
    print("{} lines".format(args))

def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SessionBus()

    service = bus.get_object('org.meks.Logger', '/Logger')

    service.connect_to_signal('LogCountLimit', signal_handler, dbus_interface='org.meks.Logger')

    loop = GLib.MainLoop()
    loop.run()

if __name__ == "__main__" :
    main()
