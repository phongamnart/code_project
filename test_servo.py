from machine import Pin,PWM
from time import sleep

pwm = PWM(Pin(27))
pwm.freq(50)

def setServoCycle(position):
    pwm.duty_u16(position)
    sleep(0.1)
    
while True:
    for pos in range(800, 8000, 50):
        setServoCycle(pos)
    for pos in range(8000, 800, 50):
        setServoCycle(pos)