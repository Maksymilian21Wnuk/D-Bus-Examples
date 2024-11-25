# D-Bus Tutorial Examples
Mechanism for making linux's programs communication (Inter-process communication). 

# Table of contents
1. [Examples](#examples)
    1. [Service](#service)
    2. [Signal Client](#signal-client)
    3. [Client](#client)
2. [Requirements](#requirements)
3. [Tools & Commands](#tools--commands)
4. [Basics](#basics)

## Examples <a name='examples'></a>
Examples use python's binding, pydbus. It's strongly advised to learn 
by looking at hands-on files in examples folder. There is implemented:
### Service <a name="service"> </a>
- implementing signal when log is added
- method for adding log
- properties, such as:
    - Upper - making new logs upper-case, read/write
    - LogCount - count of log lines number, readOnly
    - LogFileName - name of file in which logs are written, read/write

### Signal Client <a name="signal-client"> </a>
Signal listening client, that handles
the signal emitted by logger service

### Client <a name="client"> </a>
Couple of client-side examples,
exchanging information with logger service
with saving logs, getting properties and 
setting them.

## Requirements <a name="requirements"> </a>
- dbus_python==1.2.18
- PyGObject==3.42.1
- linux os based system

You may install requirements using
```bash
make requirements
```
in project's root
## Tools & Commands <a name="tools--commands"> </a>
1. **d-feet** - D-Bus debugger and inspector. Easily introspect  
dbus services, their interfaces and methods.
```bash
# debian based
sudo apt install d-feet
d-feet
```
```bash
# red-hat based
sudo dnf install d-feet
d-feet
```
2. **dbus-monitor** - monitor D-Bus communication's bus messages either from
systembus or sessionbus.

System bus
```bash
dbus-monitor --system
```
Session bus
```bash
dbus-monitor --session
```
**System bus** - not user-specific bus, mostly used
in communication on os level, where root priveleges are needed. Examples:
- Networks
- Devices like disks, keyboard
- Hardware (you may shutdown pc using dbus message)
- Power (controlling battery with dbus)

**Session bus** -
Examples:
- Desktop applications (Firefox, Spotify)
- User written programs (like those in examples)
- Graphical environment, GNOME or KDE

3. **dbus-send** - sending a message to a service

Sends a message to object /org/freedesktop/DBus
of interface org.freedesktop.DBus with method ListNames, this should print reply of listing available dbus services
```bash
dbus-send --session --print-reply --dest=org.freedesktop.DBus /org/freedesktop/DBus org.freedesktop.DBus.ListNames
```

4. **busctl**

```bash
busctl list
busctl tree <service>
busctl introspect <service> <object>
busctl introspect org.freedesktop.PolicyKit1 /org/freedesktop/PolicyKit1/Authority
```


5. Examples:
```bash
dbus-send --session --print-reply --dest=org.meks.Logger /org/meks/Logger/1 org.meks.Logger.AddLog string:"asdf"
#
dbus-monitor "interface='org.meks.Logger'"
#
dbus-send --session --print-reply --dest=org.meks.Logger /org/meks/Logger/1 org.freedesktop.DBus.Properties.Set string:org.meks.Logger string:Upper variant:boolean:false
#
dbus-send --session --print-reply --dest=org.meks.Logger /org/meks/Logger/1 org.freedesktop.DBus.Introspectable.Introspect


```


## Basics <a name="basics"> </a>
### Connecting to bus

```python
from pydbus import SessionBus
bus = SessionBus()
```

### Proxy
Proxy is an object used to represent remote object from another process.
Using proxy you can call methods or emit signals.
```python
bus_name = 'org.freedesktop.DBus'
object_name = '/org/freedesktop/DBus'
proxy = bus.get_object(bus_name, object_name)
```

### Calling method

```python
from pydbus import SessionBus

# connects to bus
bus = SessionBus()
# gets proxy of SERVICE_NAME and OBJECT_PATH 
proxy = bus.get(SERVICE_NAME, OBJECT_PATH)
# calls method implemented by IFACE_NAME interface
res = proxy[IFACE_NAME].MethodCall(arg1, arg2)
```

