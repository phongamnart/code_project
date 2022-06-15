from machine import Pin, PWM
import utime

led = Pin(2, Pin.OUT)
sensor = Pin(10, Pin.IN)
buzzer = PWM(Pin(18))
pwm = PWM(Pin(9))
pwm.freq(50)

def stop():
    pwm.duty_u16(5000)
    utime.sleep(1)
    
def opendoor():
    pwm.duty_u16(4500)
    utime.sleep(1)
    
def openclose():
    pwm.duty_u16(5800)
    utime.sleep(1)
    
while True:
    if sensor.value()==0:
        pwm.duty_u16(4580)
        utime.sleep(1)
    else:
        pwm.duty_u16(5000)
        utime.sleep(1)


        
        