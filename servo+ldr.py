from machine import Pin, PWM
import utime

pwm = PWM(Pin(27))
photoPIN = 26

MIN = 650000
MID = 1500000
MAX = 3000000

pwm.freq(50)
pwm.duty_ns(MID)

def open_door():
    pwm.duty_ns(MAX)
    utime.sleep(0.1)

def close_door():
    pwm.duty_ns(MID)
    utime.sleep(0.1)
    
def readLight(photoGP):
    photoRes = ADC(Pin(26))
    light = photoRes.read_u16()
    light = round(light/65553*100,2)
    return light

while True:
    print("light: " + str(readLight(photoPIN)) +"%")
    sleep(1)
    if(readLight(photoPIN)) <= 20:
        print("OPEN")
        open_door()
    else:
        print("CLOSE")
        close_door()
        
