# D-Bus examples

Couple of examples in dbus. How it works:
- service implements logger service for writing to log file some text (logs)
- signal_client waits in loop for signals that are emited when
there is a log added
- logger_client is an example of client communicating bidirectionally with
service logger