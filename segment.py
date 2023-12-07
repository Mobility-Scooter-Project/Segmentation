'''
Segment File
-Uses the classes in the SAM file to process videos
'''

from sam import SegmentAnything
from videos import Video
from yolov8 import YOLOv8
from csv_output import CSVOutput

def process_file(in_file, out_file, interval, video_output):
    # instantiate the SegmentAnything, YOLOv8, and Video classes
    sammodel = SegmentAnything()
    yolomodel = YOLOv8()
    cap = Video(in_file, interval)
    data_writer = CSVOutput(out_file, 'test')

    count = 1

    # gets all frames from video and saves it into a list
    result = cap.get_all_frames()

    for frame in result:
        # get input box from yolov8
        input_box = yolomodel.get_box(frame)

        # input box into SAM predictor
        mask = sammodel.process(frame, input_box)
        data_writer.process(mask[0])
        print(f'saved first row of mask {count}')
        count += 1

    print("process_file working!")