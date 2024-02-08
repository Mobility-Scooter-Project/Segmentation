'''
YOLOv8 File
-Handles all logic relating to the YOLOv8 Model
'''

from ultralytics import YOLO
import cv2

class YOLOv8:
    def __init__(self):
        # Load pretrained yolov8 model
        # May download model onto computer
        self.model = YOLO('assets/yolov8n.pt')

    # Takes in a video frame and returns a bounding box for the largest subject in frame
    def get_boxes(self, frame):
        # get results from model
        results = self.model(frame)

        # Returns the boxes found in the frame as a 'Boxes' object
        return results[0].boxes
