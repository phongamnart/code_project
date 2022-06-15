from machine import Pin, PWM, UART, SPI, I2C
from mfrc522 import MFRC522
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime
import machine
import _thread
import time

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

pwm = PWM(Pin(21))
pwm1 = PWM(Pin(9))
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
ledg_in = Pin(3, Pin.OUT)
ledr_in = Pin(19, Pin.OUT)
ledg_out = Pin(20, Pin.OUT)
ledr_out = Pin(8, Pin.OUT)
buzzer = PWM(Pin(18))
ir1 = Pin(10, Pin.IN)
ir2 = Pin(11, Pin.IN)
ir3 = Pin(27, Pin.IN)
ir4 = Pin(1, Pin.IN)
true = Pin(15, Pin.OUT)
false = Pin(14, Pin.OUT)
sck = Pin(6, Pin.OUT)
mosi = Pin(7, Pin.OUT)
miso = Pin(4, Pin.OUT)
sda = Pin(5, Pin.OUT)
rst = Pin(22, Pin.OUT)
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
card1 = "0xd3ff8c34"
card2 = "0xe316ec34"
card3 = "0xe3a48a34"
card4 = "0xbb2ffd2d"
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

def stop_in():
    pwm.duty_u16(5000)
    utime.sleep(1)
    
def stop_out():
    pwm1.duty_u16(5000)
    utime.sleep(1)
    
def open_in():
    pwm.duty_u16(4580)
    utime.sleep(1)
    
def close_in():
    pwm.duty_u16(5150)
    utime.sleep(1)
    
def open_out():
    pwm1.duty_u16(4580)
    utime.sleep(1)
    
def close_out():
    pwm1.duty_u16(5150)
    utime.sleep(1)

def lcd_open():
    lcd.putstr("Open Door")
    utime.sleep(2)
    lcd.clear()
    
def lcd_close():
    lcd.putstr("Close Door")
    utime.sleep(2)
    lcd.clear()
    
def scan_pass():
    for i in range(2):
        buzzer.duty_u16(900000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)

def scan_fail():
    for i in range(5):
        ledr_in.toggle()
        buzzer.duty_u16(900000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)
        
        
def b_close():
    buzzer.duty_u16(900000)
    utime.sleep_ms(80)
    buzzer.duty_u16(0)
    utime.sleep_ms(80)
    
def scan_card():
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
                uart.write('PUB,"Group5CPE_2021","Open Door"')
                print("Open")
                scan_pass()
                ledg_in.high()
                ledr_in.low()
                lcd_open()
                open_in()
                stop_in()
            elif uid == card2:
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
                uart.write('PUB,"Group5CPE_2021","Open Door"')
                print("Open")
                scan_pass()
                ledg_in.high()
                ledr_in.low()
                lcd_open()
                open_in()
                stop_in()
            elif uid == card3:
                true.toggle()
                time.sleep(1)
                scan_fail()
                uart.write('PUB,"Group5CPE_2021","Fail"')
                print("Fail")
                lcd.putstr("FAIL")
                utime.sleep(2)
                lcd.clear()
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
    if ir1.value()==0:
        print("Sensor I")
        ledr_in.high()
        ledg_in.low()
        scan_card()
        ir2.value(1)
    elif ir2.value()==0:
        print("Sensor II")
        b_close()
        ledr_in.low()
        ledg_in.low()
        print("Close")
        uart.write('PUB,"Group5CPE_2021","Close Door"')
        lcd_close()
        close_in()
        stop_in()
    elif ir3.value()==0:
        print("Sensor III")
        scan_pass()
        ledg_out.high()
        ledr_out.low()
        print("Open")
        uart.write('PUB,"Group5CPE_2021","Out"')
        open_out()
        stop_out()
    elif ir4.value()==0:
        print("Sensor IV")
        b_close()
        print("Close")
        close_out()
        stop_out()
        ledg_out.low()
        ledr_out.high()