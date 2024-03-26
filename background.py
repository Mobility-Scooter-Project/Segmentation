from nanosam.utils.predictor import Predictor
from videos import Video
from ultralytics import YOLO
from csv_output import CSVOutput
import numpy as np
import time
import PIL.Image
import cv2

def cv2_to_pil(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return PIL.Image.fromarray(image)

yolo_model = YOLO('assets/yolov8n.pt')
nano = Predictor("data/resnet18_image_encoder.engine",
                                    "data/mobile_sam_mask_decoder.engine")

mask = None

cap = cv2.VideoCapture(0)

startTime = 0
while True:
    re, image = cap.read()

    if not re:
        break

    image_pil = cv2_to_pil(image)

    box = yolo_model(image)
    box = box[0].boxes
    if len(box) != 0:    
        box = box.xyxy[0].cpu().numpy()
        points = np.array([[box[0], box[1]], [box[2], box[3]]])

        nano.set_image(image_pil)

        mask, _, _ = nano.predict(
                points,
                np.array([2, 3])
            )
    
        if mask is not None:
            mask = (mask[0, 0] > 0).detach().cpu().numpy()

            h, w = mask.shape[-2:]
            image = image * mask.reshape(h, w, 1)
        
        image = cv2.rectangle(image, (int(box[0].item()), int(box[1].item())), 
                              (int(box[2].item()), int(box[3].item())), (0, 255, 0), 2)
    
    currentTime = time.time()
    fps = 1/(currentTime - startTime)
    #nm = (currentTime - startTime) * 1000
    startTime = currentTime
    cv2.putText(image, "FPS: " + str(fps), (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow("image", image)

    ret = cv2.waitKey(1)

    if ret == ord('q'):
        break

cv2.destroyAllWindows()


    





