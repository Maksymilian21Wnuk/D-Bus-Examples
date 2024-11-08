import dbus
import dbus.service
import datetime
import os

LOGFILE = "logfile.txt"

class Logger(dbus.service.Object):
    def __init__(self):
        bus = dbus.SessionBus()
        name = dbus.service.BusName('org.meks.Logger', bus)
        try:
            with open(LOGFILE, "r") as file:
                self.log_count = len(file.readlines())
        except FileNotFoundError:
            self.log_count = 0
        super().__init__(name, '/Logger')   

    @dbus.service.method('org.meks.Logger', in_signature='', out_signature='i')
    def GetLogCount(self):
        return self.log_count
        
    @dbus.service.method('org.meks.Logger', in_signature='s')
    def AddLog(self, log_str):
        log_str = "{} at {}".format(log_str, datetime.datetime.now())
        with open(LOGFILE, "a") as file :
            file.write(log_str + "\n")
            self.log_count += 1
        return "Log saved"

