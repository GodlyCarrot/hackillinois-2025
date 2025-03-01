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
    fx = 600
    fy = 600
    cx = 320
    cy = 240

    detections = at_detector.detect(gray, 
                                    estimate_tag_pose=True, 
                                    camera_params=(fx, fy, cx, cy), 
                                    tag_size=0.05)
    for detection in detections:
        print(f"Tag ID: {detection.tag_id}")
        print(f"Center: {detection.center}")

        print(f"Rotation Matrix: {detection.pose_R}")
        print(f"Translation Vector: {detection.pose_t}")
       
        if cv2.imwrite('tag-detected.png', frame):
            print("captured image - saved as tag-detected.png")
        else:
            print("failed to save the image")

    if cv2.waitKey(1) >= 0:
        break
        
cap.release()
cv2.destroyAllWindows()
