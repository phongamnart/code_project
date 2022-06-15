from machine import Pin, I2C, SPI
import machine
import _thread
import time
from mfrc522 import MFRC522
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(12), scl=machine.Pin(13), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
true = Pin(15,Pin.OUT)
false = Pin(14,Pin.OUT)
sck = Pin(2, Pin.OUT)
mosi = Pin(3, Pin.OUT)
miso = Pin(4, Pin.OUT)
sda = Pin(1, Pin.OUT)
rst = Pin(5, Pin.OUT)
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
card1 = "0xe316ec34"
card2 = "0xd3ff8c34"
card3 = ""
card4 = ""
card5 = ""
card6 = ""

    
def card_scan():
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
                print("SCAN PASSED")
                lcd.putstr('CARD OK')
                    
            elif uid == card2:
                true.toggle()
                time.sleep(1)
                print("SCAN FAIL")
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
        

