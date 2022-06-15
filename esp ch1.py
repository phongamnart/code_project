from machine import UART, Pin
import machine
import _thread
import time
import utime
from machine import I2C, Pin, SPI
from mfrc522 import MFRC522

pump = Pin(26, Pin.OUT)
ledb = Pin(13, Pin.OUT)
ledw = Pin(12, Pin.OUT)
true = Pin(15, Pin.OUT)
false = Pin(14, Pin.OUT)
sck = Pin(6, Pin.OUT)
mosi = Pin(7, Pin.OUT)
miso = Pin(4, Pin.OUT)
sda = Pin(5, Pin.OUT)
rst = Pin(22, Pin.OUT)
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
card1 = "0xe316ec34"
card2 = "0xc373469d"
card3 = ""
card4 = ""
card5 = ""
card6 = ""

def ESP8266Read():
    data=uart.readline()
    if data is not None:
        print(data.decode('UTF8'))
    time.sleep(0.1)
    
uart = UART(0,baudrate=115200, tx=Pin(16), rx=Pin(17))
time.sleep(1.0)
uart.write('SETWIFI,"KUWIN.","0983135681a"')
time.sleep(1.0)


def pump_on():
    pump.value(1)
    time.sleep(1)
    print("Pump On")
    
def pump_off():
    pump.value(0)
    print("Pump Off")  

def card_scan():
    rdr = MFRC522(spi, sda, rst)
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print("OK\n"+uid)
            if uid == card1:
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
                uart.write('PUB,"7/2/225","ON"')
                print("OK CARD 1")
                pump_on()
                ledb.high()
                ledw.low()
            elif uid == card2:
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
                uart.write('PUB,"7/2/225","OFF"')
                print("OK CARD 2")
                pump_off()
                ledw.high()
                ledb.low()
            elif uid == card3:
                true.toggle()
                time.sleep(1)
            else:
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(0.1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(0.1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(1)
                
while True:
    card_scan()
    time.sleep(1)
    print(uart.read())
    time.sleep(3)
    ms = b'MESSAGE,"7/2/225","ON"\r\n'


                

