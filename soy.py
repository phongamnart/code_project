from machine import Pin
import time

pump = Pin(5, Pin.OUT)

def pump_on():
    pump.value(1)
    time.sleep(0.5)
    print("Pump On")
    
def pump_off():
    pump.value(0)
    time.sleep(0.5)
    print("Pump Off")
    
while True:
    pump_on()
    pump_off()
    
