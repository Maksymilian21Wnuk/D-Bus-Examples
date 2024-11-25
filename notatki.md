## IPC
mechanizm do komunikacji dwóch procesów

### Shared memory
- najszybszy
- wymaga semaforów lub mutexów
- dobre dla dużych danych
- trudne do zaimplementowania
- renderowanie grafiki 3d
### Sockety 
- sockety unix domain (dbus zaimplementowany na socketach)
- protokoły zdalne, tcp udp
- sieci
### Pipe & named pipe
- tylko lokalnie
- proste
- ale strumieniowo
- dwukierunkowe
### CORBA
- common object request broker
- neutralność językowa
- skomplikowany standard
- transparentność lokacji obiektu,
obiekty w tej samej przestrzeni adresowej
traktowane jakby były w innym procesie, maszynie
- brak planu przez maintainerow
- wlasciwie to RPC
- systemy rozproszone
- GNOME- bonobo

### DCOP 
- wiadomości
- KDE3, do czasu DBUS w KDE4
- brak mechanizmu autoryzacji
- silnie związany z c++


### freedesktop
- protokół systemu okienek, jako zasępca x-window


## Zalety dbus
- centralizacja - gui łączy się z network managerem, razem korzystają
z dbusa
- abstrakcja polaczenia przez busa


## Folder /usr/share/dbus-1
- system.conf i session.conf, config file dla busy systemowej
i sesyjnej
- 


## komendy:
```bash
busctl --session list
busctl monitor --user org.meks.Logger


dbus-send --session --print-reply --dest=org.meks.Logger /org/meks/Logger/1 org.meks.Logger.AddLog string:"asdf"
dbus-send --session --print-reply --dest=org.meks.Logger /org/meks/Logger/1 org.freedesktop.DBus.Properties.Set string:org.meks.Logger string:Upper variant:boolean:false

busctl call --user org.meks.Logger /org/meks/Logger/1 org.meks.Logger AddLog s "asdf"

busctl --user call org.meks.Logger /org/meks/Logger/1 org.freedesktop.DBus.Properties Set "ssv" org.meks.Logger Upper b false

# busct w skrocie: call, status, monitor, tree, introspect, emit, get-property, set-property

# pokazac: dbus-send, dbus-monitor
# pokazac: busctl monitor, busctl status
# pokazac: call, introspect, set-property, call

busctl call com.meks.Logger /com/meks/Logger/1 com.meks.Logger HelloWorld

dbus-monitor "interface='org.meks.Logger'"
```
## security xml
- user whoopsie - zbiera raport o crashach, error tracker
- user username
- group - grupa userow
- context - default lub root
- own posiadanie nazwy busy
- send_destitnation - permisje do wysylania do busy
- send interface - do interface'u
- receive sender - permisje do odbierania od kogos
- send_path - wiadomosci do object patha
- jezeli nie okreslone deny allow to system bus nie zezwala, session zezwala!

