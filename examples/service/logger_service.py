import datetime
import os
from gi.repository import GLib
from pydbus import SessionBus
from pydbus.generic import signal


# Logger service with xml representation
class Logger():
    """
    <node>
        <interface name="org.meks.Logger">
            <method name="AddLog">
                <arg direction="in"  type="s" name="log_str" />
                <arg direction="out" type="s" />
            </method>
            <signal name="CountChange">
                <arg direction="out" type="(ib)" name="count" />
            </signal>
            <property name="Upper" type="b" access="readwrite"/>
            <property name="LogCount" type="i" access="read" />
            <property name="LogFileName" type="s" access="readwrite"/>
        </interface>
    </node>
    """
    
    def __init__(self, logfile_name):
        # set default value of upper on service run
        # read/write
        self.Upper = False
        self.LogFileName = logfile_name
        try:
            with open(self.LogFileName, "r") as file:
                # read count of log file, 
                # that property is read only
                self.LogCount = len(file.readlines())
        except FileNotFoundError:
            self.LogCount = 0
    
    CountChange = signal()
    PropertiesChange = signal()

    def AddLog(self, log_str):
        # date and time to log string
        log_str = "{} at {}".format(log_str, datetime.datetime.now())
        # also if property upper is set, make upper-case log
        # example of property usage
        log_str = log_str.upper() if self.Upper else log_str
        with open(self.LogFileName, "a") as file :
            file.write(log_str + "\n")
            self.LogCount += 1
        # example of signalisation change of count
        self.CountChange((self.LogCount, self.LogCount > 5))
        return "Log saved"
        

def main():
    # connect to bus
    bus = SessionBus()


    bus.publish("org.meks.Logger", 
                ("1", Logger("logfile.txt")),
                ("2", Logger("log2.txt"))                    
                                    )
    loop = GLib.MainLoop()
    loop.run()

if __name__ == "__main__":
    main()