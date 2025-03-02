import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GpioPins = [14, 15, 18, 23]
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
mymotortest.motor_run(GpioPins, .01, 17000, True, False, "full", .05)
