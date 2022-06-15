from machine import UART, Pin
import machine
import _thread
import time
import utime
from machine import I2C, Pin, SPI
from mfrc522 import MFRC522

red_led = Pin(0, Pin.OUT)
green_led = Pin(1, Pin.OUT)
led = Pin(25, Pin.OUT)

true = Pin(15, Pin.OUT)
false = Pin(14, Pin.OUT)
sck = Pin(6, Pin.OUT)
mosi = Pin(7, Pin.OUT)
miso = Pin(4, Pin.OUT)
sda = Pin(5, Pin.OUT)
rst = Pin(22, Pin.OUT)
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
card1 = "0xe316ec34"
card2 = ""
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
#uart.write('PUB,"/ESP/LED2"')
#time.sleep(1.0)
#_thread.start_new_thread(ESP8266Read(), ()) # starts the webserver in a _thread
def card_open():
    uart.write('PUB,"/ESP/LED1","GATE OPEN"')
    green_led.value(1)
    time.sleep(5)
    print("GATE OPEN")

    

def card_scan():
    led.value(1)
    time.sleep(0.06)
    led.value(0)
    rdr = MFRC522(spi, sda, rst)
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print(uid)
            if uid == card1:
                true.toggle()
                time.sleep(1)
                red_led.value(0)
                green_led.value(1)
                time.sleep(3.0)
                uart.write('PUB,"/ESP/LED1","CARD OPEN"')
                print("OK CARD")
                    
            elif uid == card2:
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
    time.sleep(3)
    print(uart.read())
    time.sleep(3)
    gg = b'MESSAGE,"/ESP/LED1","ON"\r\n'

    if uart.read() == gg:
        green_led.value(1)
        red_led.value(0)
        card_open()
        print(card_open())
        time.sleep(5)
        
    else:
        red_led.value(1)
        green_led.value(0)
        

