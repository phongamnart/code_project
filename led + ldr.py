from machine import ADC, Pin
from time import sleep

photoPIN = 26
pump = Pin(5, Pin.OUT)
led_red = Pin(2,Pin.OUT)
led_green = Pin(5,Pin.OUT)

def pump_on():
    pump.value(1)
    time.sleep(0.5)
    print("Pump On")
    
def pump_off():
    pump.value(0)
    time.sleep(0.5)
    print("Pump Off")

def readLight(photoGP):
    photoRes = ADC(Pin(26))
    light = photoRes.read_u16()
    light = round(light/65553*100,2)
    return light

while True:
    print("light: " + str(readLight(photoPIN)) +"%")
    sleep(1)
    if (readLight(photoPIN)) >= 20:
        pump_on()
        led_green.high()
        led_red.low()
        
    else:
        print("LED On")
        pump_off()
        led_red.high()
        led_green.low()
