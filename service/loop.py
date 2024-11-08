from service import Logger
import dbus.mainloop.glib
from gi.repository import GLib



def main() :
    dbus.mainloop.glib.DBusGMainLoop(set_as_default = True)

    loop = GLib.MainLoop()
    obj = Logger()
    loop.run()


if __name__ == "__main__" :
    main()