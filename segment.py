'''
Segment File
-Uses the classes in the SAM file to process videos
'''

from sam import SegmentAnything
from videos import Video

def process_file(in_file, out_file, interval, video_output):
    # instantiate the SegmentAnything and Video classes
    pmodel = SegmentAnything()
    cap = Video(in_file)

    
    print("process_file working!")