import cv2
import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from pupil_apriltags import Detector

cap = cv2.VideoCapture(0)

at_detector = Detector(
    families="tag36h11",
    nthreads=1,
    quad_decimate=1.0,
    quad_sigma=0.0,
    refine_edges=1,
    decode_sharpening=0.25,
    debug=0
)

gpio_pins = [18, 23, 24, 25]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fx = 600
    fy = 600
    cx = 320
    cy = 240

    detections = at_detector.detect(gray, 
                                    estimate_tag_pose=True, 
                                    camera_params=(fx, fy, cx, cy), 
                                    tag_size=0.05)

    step_motor = RpiMotorLib.BYJMotor("Step Motor", "28BYJ")

    if detections:
        for detection in detections: 
            print(f"Tag ID: {detection.tag_id}")
            print(f"Center: {detection.center}")

            print(f"Rotation Matrix: {detection.pose_R}")
            print(f"Translation Vector: {detection.pose_t}")
       
            if cv2.imwrite('tag-detected.png', frame):
                print("captured image - saved as tag-detected.png")
            else:
                print("failed to save the image")

        step_motor.motor_run(gpio_pins, .01, 100, False, False, "half", .05)
    else:
        print("No AprilTag detected. Motor stopped")
cap.release()
cv2.destroyAllWindows()
