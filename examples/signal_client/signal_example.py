from pydbus import SessionBus
from gi.repository import GLib


def signal_handler(payload):
    print("{} lines".format(payload))

def main():

    # connect to session bus
    bus = SessionBus()

    # listen to signals of object 1
    proxy = bus.get('org.meks.Logger', '/org/meks/Logger/1')

    # listen to CountChange signal emit with handler signal_handler
    proxy.CountChange.connect(signal_handler)
    
    loop = GLib.MainLoop()
    loop.run()

if __name__ == "__main__" :
    main()
