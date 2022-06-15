from machine import Pin, PWM
import time
from servo import Servo

servo = Servo(26)

servo.test()
servo.setServo90()
time.sleep(3)
servo.setServo0()
time.sleep(3)
servo.setServo180()
time.sleep(3)
servo.setServo0()
time.sleep(3)