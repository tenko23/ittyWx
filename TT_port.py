import serial, time

SERIALPORT = "/dev/ttyACM0"  #This is your Volpe board address... this is usually the default address if you have only one.
BAUDRATE = 19200

ser = serial.Serial(SERIALPORT, BAUDRATE)
ser.bytesize = serial.EIGHTBITS

def print_data(data, num):
    bells = []
    for i in range(num):
        bells.append(0x07)
    if not ser.isOpen():
        ser.open()
    if ser.isOpen():
        try:
            ser.flushInput()
            ser.flushOutput()
            ser.write(serial.to_bytes(bells))
            ser.write(str.encode(data))
            ser.close()
        except Exception as e:
            print("Error communicating...: ", str(e))
    else:
        print("Cannot open serial port. ")