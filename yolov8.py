'''
YOLOv8 File
-Handles all logic relating to the YOLOv8 Model
'''

from ultralytics import YOLO
import cv2

# Takes in a video frame and returns a bounding box for the largest subject in frame
def get_box(frame):
    # Load pretrained yolov8 model
    # May download model onto computer
    model = YOLO('yolov8.pt')

    # get results from model
    results = model(frame)

    # Returns bounding box in (xyxy) format as a numpy array
    return results[0].boxes.xyxy[0].cpu().numpy()
