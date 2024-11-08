# D-Bus
Mechanism for making linux's programs communication (Inter-process communication)
easy and relatively fast. Examples use python's binding, pydbus.

# Some requirements
pip install dbus-python
linux based os

# Useful commands and programs
1. d-feet - D-Bus debugger and inspector. Easily introspect  
dbus services, their interfaces and methods.
```bash
# debian
sudo apt install d-feet
# red-hat
sudo dnf install d-feet
```

# Connecting to bus

```python
import dbus
bus = dbus.SessionBus()
```

# Proxy
Proxy is an object used to represent remote object from another process.
Using proxy you can call methods or emit signals.
```python
interface_name = 'org.freedesktop.DBus'
object_name = '/org/freedesktop/DBus'
proxy = bus.get_object(interface, object_name)
```

# Calling method

```python
# first option
names = proxy.ListNames()
# second option
method = proxy.get_dbus_method('ListNames', 'org.freedesktop.DBus')
names = method()
```