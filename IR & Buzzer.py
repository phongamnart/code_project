from machine import Pin, PWM, UART
import utime
import machine
import _thread
import time


sensor = Pin(15, Pin.IN)
buzzer = PWM(Pin(18))
trigger = Pin(12, Pin.OUT)
echo = Pin(13, Pin.IN)

def ESP8266Read():
    data=uart.readline()
    if data is not None:
        print(data.decode('UTF8'))
    time.sleep(0.1)
    
uart = UART(0,baudrate=115200, tx=Pin(16), rx=Pin(17))
time.sleep(1.0)
uart.write('SETWIFI,"KUWIN.","0983135681a"')
time.sleep(1.0)

def ir_off():
    buzzer.duty_u16(0)
    
def ir_on():
    for i in range(3):
        buzzer.duty_u16(900000)
        utime.sleep_ms(500)
        buzzer.duty_u16(0)
        utime.sleep_ms(500)
        
def sound():
    for i in range(10):
        buzzer.duty_u16(900000)
        utime.sleep_ms(100)
        buzzer.duty_u16(0)
        utime.sleep_ms(100)
        
while True:
    trigger.low()
    utime.sleep_us(1)
    trigger.high()
    utime.sleep_us(3)
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed*0.03) / 2
    print("The distance from object is ",distance,"cm")
    utime.sleep(1)
    if (distance)<10:
        ir_off()
        sound()
        uart.write('PUB,"G5","stop"')
        
    elif sensor.value()==0:
        ir_on()
        uart.write('PUB,"G5","warning"')
        
        

    
        