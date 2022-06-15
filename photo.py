from machine import ADC, Pin
from time import sleep

photoPIN = 26

def readLight(photoGP):
    photoRes = ADC(Pin(26))
    light = photoRes.read_u16()
    light = round(light/65535*10000,2)
    return light

while True:
    print("light: " + str(readLight(photoPIN)) +"%")
    sleep(1)
