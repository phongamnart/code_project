from machine import Pin
import time

ir1 = Pin(27,Pin.IN)
ir2 = Pin(26,Pin.IN)
led = Pin(10,Pin.OUT)

while True:
    if ir1.value() == 0:
        led.high()
    else:
        led.low()
        