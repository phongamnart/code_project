from machine import Pin
from time import sleep

led_red = Pin(10,Pin.OUT)

while True:
    led_red.high()
    sleep(1)
    led_red.low()
    sleep(1)