from machine import Pin,PWM
import utime

pwm = PWM(Pin(27))

MIN = 0
MAX = 2000000

pwm.freq(50)
pwm.duty_ns(MIN)

def servo_on():
    pwm.duty_ns(MAX)

def servo_off():
    pwm.duty_ns(MIN)

while True:
    servo_on()
    utime.sleep(1)
    servo_off()