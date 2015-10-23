# -----------------------------------------------------------
# basic implementation to read from serial interface
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

import serial

port = serial.Serial("/dev/ttyUSB0", 9600, timeout = None)

port.open()

while true:
    daten = port.readline()
    print daten
