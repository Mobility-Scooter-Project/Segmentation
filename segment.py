'''
Segment File
-Uses the classes in the SAM file to process videos
'''

from sam import SegmentAnything
from videos import Video
from yolov8 import YOLOv8
from csv_output import CSVOutput
import numpy as np

def process_file(in_file, out_file, interval, video_output):
    # instantiate the SegmentAnything, YOLOv8, and Video classes
    sammodel = SegmentAnything()
    yolomodel = YOLOv8()
    cap = Video(in_file, interval)
    data_writer = CSVOutput(out_file, None)

    count = 1

    # gets all frames from video and saves it into a list
    result = cap.get_all_frames()

    for frame in result:
        # get input box from yolov8
        input_box = yolomodel.get_box(frame)
        print(f"Frame shape: {frame.shape}")

        # input box into SAM predictor
        mask = sammodel.process(frame, input_box)
        print(f"Mask shape: {mask.shape}")
        print(f"the sparsity of the mask is: {1.0 - (np.count_nonzero(mask) / mask.size)}")

        # write mask onto csv file
        data_writer.process(mask)
        print(f'saved first row of mask {count}')
        count += 1
