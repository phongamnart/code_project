from machine import UART, Pin
import machine
import _thread
import time
def ESP8266Read():
    data=uart.readline()
    if data is not None:
        print(data.decode('UTF8'))
    time.sleep(0.1)
    
uart = UART(0,baudrate=115200, tx=Pin(16), rx=Pin(17))
time.sleep(1.0)
uart.write('SETWIFI,"Comeonb_th","tawipha44669900"')
time.sleep(1.0)
