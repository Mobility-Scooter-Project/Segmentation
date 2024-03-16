'''
Segment File
-Uses the classes in the SAM file to process videos
'''

from sam import SegmentAnything
from nano import NanoSam
from videos import Video
from yolov8 import YOLOv8
from csv_output import CSVOutput
import numpy as np
import time
from PIL import Image
import matplotlib.pyplot as plt

# with mobileSAM, 1800 frames took 318.052 seconds, or 5.66 frames per second

def process_file(in_file, out_file, interval, video_output):
    # instantiate the SegmentAnything, YOLOv8, and Video classes
    sammodel = NanoSam()
    yolomodel = YOLOv8()
    cap = Video(in_file, interval)
    data_writer = CSVOutput(out_file, None)

    count = 1

    # gets all frames from video and saves it into a list
    result = cap.get_all_frames()

    if video_output != None:
        cap.make_video(result[0], video_output)

    start_time = time.time()
    for frame in result:
        # get input box from yolov8
        input_box = yolomodel.get_boxes(frame)
        points = np.empty([2, 2])

        if len(input_box) == 0:
            # if no detections, continue to next frame
            print('NO DETECTION')
            continue
        else:
            # if there is/are detections, get the largest bounding box from the results in (xyxy) format
            input_box = input_box.xyxy[0].cpu().numpy()
            points = np.array([[input_box[0], input_box[1]], [input_box[2], input_box[3]]])

        print(f"Frame shape: {frame.shape}")

        # input box into SAM predictor

        # convert to PIL
        frame_pil = Image.fromarray(frame)

        mask = sammodel.process(frame_pil, points)

        mask = (mask[0, 0] > 0).detach().cpu().numpy()

        print(f"Mask shape: {mask.shape}")
        print(f"the sparsity of the mask is: {1.0 - (np.count_nonzero(mask) / mask.size)}")

        # write mask onto csv file
        data_writer.process(mask)
        print(f"Wrote frame: {count}")
        count += 1

        # append processed frame to new video
        if video_output != None:
            cap.append_frame(frame, mask, input_box)
    
    if video_output != None:
        cap.release_video()
        
    print(f"Program took: {time.time() - start_time}")