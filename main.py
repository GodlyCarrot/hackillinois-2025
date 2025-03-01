import cv2
from pupil_apriltags import Detector 

img_path = 'test.png'
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

at_detector = Detector(
   families="tag36h11",
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

detections = at_detector.detect(img)
if detections:
    print("Detected tags:", detections)
