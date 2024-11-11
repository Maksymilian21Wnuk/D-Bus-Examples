import dbus
import dbus.service
import datetime
import os


class Logger(dbus.service.Object):
    LOGFILE = "logfile.txt"
    LIMIT = 100
    
    def __init__(self):
        bus = dbus.SessionBus()
        name = dbus.service.BusName('org.meks.Logger', bus)
        try:
            with open(self.LOGFILE, "r") as file:
                self.log_count = len(file.readlines())
        except FileNotFoundError:
            self.log_count = 0
        super().__init__(name, '/Logger')   

    @dbus.service.method('org.meks.Logger', in_signature='', out_signature='i')
    def GetLogCount(self):
        return self.log_count
    
    # signal emited when there are more logs than 100
    @dbus.service.signal('org.meks.Logger')
    def LogCountLimit(self):
        print("Emiting")
        pass
    
    # Method that appends string to log file,
    # it can emit signal if there are more than LIMIT
    # log lines
    @dbus.service.method('org.meks.Logger', in_signature='s')
    def AddLog(self, log_str):
        log_str = "{} at {}".format(log_str, datetime.datetime.now())
        with open(self.LOGFILE, "a") as file :
            file.write(log_str + "\n")
            self.log_count += 1
        
        # emit signal if count bigger than limit
        if (self.log_count > self.LIMIT) :
            self.LogCountLimit()
            try :
                os.remove(self.LOGFILE)
                self.log_count = 0
            except FileNotFoundError:
                pass
        
        return "Log saved"

