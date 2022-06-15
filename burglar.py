from machine import Pin, PWM
import utime

sensor_ir = Pin(10, Pin.IN)
ledr = Pin(2, Pin.OUT)
ledg = Pin(3, Pin.OUT)
buzzer = PWM(Pin(18))

def ir_handler(pin):
    for i in range(20):
        ledr.toggle()
        ledg.toggle()
        utime.sleep_ms(100)
        buzzer.duty_u16(900000)
        time.sleep(0.9)
        buzzer.duty_u16(0)
        time.sleep(0.7)
        buzzer.duty_u16(1)
        time.sleep(0.2)
        
        
sensor_ir.irq(trigger=Pin.IRQ_RISING, handler=ir_handler)

while True:
    ledr.toggle()
    ledg.toggle()
    utime.sleep(5)