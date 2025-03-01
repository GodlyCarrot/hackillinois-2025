import RPi.GPIO as GPIO

from RpiMotorLib import RpiMotorLib

GpioPins = [21, 22, 23, 24]

mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

mymotortest.motor_run(GpioPins, .01, 100, False, False, "half", .05)
