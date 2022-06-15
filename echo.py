from machine import Pin, PWM
import utime
from time import sleep

trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
led_red = Pin(0,Pin.OUT)
led_green = Pin(1,Pin.OUT)
buzzer = PWM(Pin(18))

def warning():
    for i in range(5):
        buzzer.duty_u16(900000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)
        led_red.high()
        sleep(0.1)
        led_red.low()
        sleep(0.1)

while True:
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed*0.0343) / 2
    print("The distance from object is ",distance,"cm")
    utime.sleep(1)
    if(distance < 10):
        led_red.high()
        led_green.low()
        warning()
    
    else:
        led_red.low()
        led_green.high()
        