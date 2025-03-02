from gpiozero import LED
from time import sleep

global distance
ultrasonic = DistanceSensor(echo=1, trigger=2)

def ultrasonic_detector() {
    while True:
        distance = ultrasonic.distance * 100
        if distance < 20:
            print("stop")
            
            ###STOP ROBOT MOTORS HERE###

            while ultrasonic.distance * 100 < 20:
                sleep(0.1)
        
        print("moving")
        ###MOVE ROBOT MOTORS HERE###
}