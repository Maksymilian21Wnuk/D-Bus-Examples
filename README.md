# D-Bus WORK IN PROGRESS may contain errors
Mechanism for making linux's programs communication (Inter-process communication)
easy and relatively fast. Examples use python's binding, pydbus.

## Some requirements
- dbus_python==1.2.18
- pick==2.4.0
- PyGObject==3.42.1
- linux os based system

You may install python's requirements using
```bash
pip install -r requirements.txt
```
in project's root
## Useful commands and programs
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



## Connecting to bus

```python
import dbus
bus = dbus.SessionBus()
```

## Proxy
Proxy is an object used to represent remote object from another process.
Using proxy you can call methods or emit signals.
```python
bus_name = 'org.freedesktop.DBus'
object_name = '/org/freedesktop/DBus'
proxy = bus.get_object(bus_name, object_name)
```

## Calling method

```python
# first option
names = proxy.ListNames()
# second option
interface = 'org.freedesktop.DBus'
method = proxy.get_dbus_method('ListNames', interface)
names = method()
```


