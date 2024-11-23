


gen:
	gdbus-codegen --interface-prefix org.meks. --generate-c-code logger logger.xml


compile:
	gcc logger.c -o logger-service `pkg-config --cflags --libs gio-2.0`