import cv2
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

    detections = at_detector.detect(gray)
    if detections:
        print("Detected tags:", detections)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) >= 0:
        break