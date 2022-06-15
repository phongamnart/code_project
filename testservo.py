from machine import Pin, PWM
import utime

led = Pin(13, Pin.OUT)
sensor = Pin(28, Pin.IN)
doori = PWM(Pin(21))

MIN = 0
MAX = 6000


doori.freq(50)
doori.duty_ns(MIN)

def servo_on():
    doori.duty_ns(MAX)
    utime.sleep(1)

def servo_off():
    doori.duty_ns(MIN)
    utime.sleep(1)

    
while True:
    if sensor.value()==0:
        print("ON")
        servo_on()

    else:
        print("OFF")
        servo_off()
