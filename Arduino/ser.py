# to read from the serial port

import serial
with serial.Serial('/dev/ttyACM0', 115200, timeout=10) as ser:  # open serial port
    while True:
        print(ser.readline())
