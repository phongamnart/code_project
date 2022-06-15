from machine import Pin, PWM
import utime

led = Pin(13, Pin.OUT)
sensor = Pin(22, Pin.IN)
buzzer = PWM(Pin(14))
trigger = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)

def ir_off():
    buzzer.duty_u16(1)
    
def ir_on():
    for i in range(3):
        buzzer.duty_u16(900000)
        utime.sleep_ms(500)
        buzzer.duty_u16(0)
        utime.sleep_ms(500)
        
def sound():
    for i in range(10):
        buzzer.duty_u16(900000)
        utime.sleep_ms(100)
        buzzer.duty_u16(0)
        utime.sleep_ms(100)
        
while True:
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed*0.03) / 2
    print("The distance from object is ",distance,"cm")
    utime.sleep(0.5)
    if (distance)<10:
        ir_off()
        sound()
    elif sensor.value()==0:
        ir_on()
        


    

    
        


