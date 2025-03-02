import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib

GPIO.setmode(GPIO.BCM)
IN1 = 23
IN2 = 24
IN3 = 25
IN4 = 8

RpiMotorLib.A4988Nema(direction_pin, step_pin, step_delay, sleep_pin=None, enable_pin=None)

while True:
    motor.step(100, 1)  # Step 100 steps in one direction
    time.sleep(1)
    motor.step(100, 0)  # Step 100 steps in the opposite direction
    time.sleep(1)

