from machine import Pin, PWM
import utime

sensor = Pin(10, Pin.IN)
buzzer = PWM(Pin(18))

def sound():
    for i in range(2):
        buzzer.duty_u16(900000)
        utime.sleep_ms(100)
        buzzer.duty_u16(0)
        utime.sleep_ms(100)
    
while True:
    if sensor.value() == 0:
        print("ON")
        utime.sleep(2)
    else:
        print("OFF")
        utime.sleep(2)


        
        