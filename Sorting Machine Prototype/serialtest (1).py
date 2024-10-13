import serial
import time
from serial.tools.list_ports import comports

for portItem in comports():
	print(portItem)

arduinoSerial = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.5)

arduinoSerial.is_open

arduinoSerial.close()

arduinoSerial.open()

digit = input("What would you like to send? ")

arduinoSerial.write(bytes(digit, 'utf-8'))

time.sleep(1)

readLine = arduinoSerial.readline()

stringLine = readLine.decode("utf-8")

print(stringLine)
arduinoSerial.close()
