from machine import Pin
from time import sleep

relay = Pin(26, Pin.OUT)

while True:
    relay.value(0)
    sleep(3)
    relay.value(1)
    sleep(3)