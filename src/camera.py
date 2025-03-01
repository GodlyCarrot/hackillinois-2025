import cv2
import numpy as np
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
    for detection in detections:
        corners = detection.corners
        corners = [(int(c[0]), int(c[1])) for c in corners]
        for i in range(4):
            cv2.line(frame, corners[i], corners[(i + 1) % 4], (0, 255, 0), 2)
            
        print(f"Tag ID: {detection.tag_id}")
        print(f"Center: {detection.center}")

        print(f"Rotation Matrix: {detection.pose_R}")
        print(f"Translation Vector: {detection.pose_t}")
        
    cv2.imshow('video feed', frame)
    if cv2.waitKey(1) >= 0:
        break
        
cap.release()
cv2.destroyAllWindows()