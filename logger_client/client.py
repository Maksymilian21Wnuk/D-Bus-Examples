import dbus
import dbus.mainloop
import dbus.mainloop.glib
from pick import pick


def send_log(log_str):
    
    # get dbus method 'AddLog' from 
    method = proxy.get_dbus_method('AddLog', 'org.meks.Logger')
    # res = log.AddLog(log_str)
    # call the method
    res = method(log_str)
    print(res)

def logger(foo):
    def wrapper(*args):
        res = foo(*args)
        log_str = "Function {} called with: {} arguments equal to {}".format(foo.__name__, args, res)
        send_log(log_str)

        return res

    return wrapper

@logger
def adder(a, b):
    return a + b

@logger
def sub(a, b):
    return a - b


def get_count():
    print(proxy.GetLogCount())


def clear_logs():
    proxy.emitClearLogsSignal()


def main():
    title = "Choose action"
    
    actions = ["Call method log", "Get property log_count", "Quit"]

    option, index = pick(actions, title, indicator="=>")
    
    match (index):
        case 0:
            n = int(input("how many times?"))
            for i in range(n):
                adder(i, n)
        case 1:
            get_count()
        
        case _:
            pass

if __name__ == "__main__" :

    # connect to session bus
    bus = dbus.SessionBus()

    # get local proxy for object path /Logger interface com.meks.Logger
    proxy = bus.get_object('org.meks.Logger', '/Logger')

    main()