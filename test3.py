from machine import Pin, PWM
import utime
MIN = 800000
MAX = 2000000
led = Pin(25,Pin.OUT)
sensor = Pin(28,Pin.IN)

pwm = PWM(Pin(21))
led.low()
pwm.freq(50)
pwm.duty_ns(MIN)
while True:
    if sensor.value()==1:
        print("Active")
        pwm.duty_ns(MAX)
        utime.sleep(1)
    else:
        print("Off")
        pwm.duty_ns(MIN)
        utime.sleep(1)