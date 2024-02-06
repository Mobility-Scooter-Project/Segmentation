'''
Videos File
-Handles all logic relating to video manipulation
'''
import cv2

class Video:
    def __init__(self, video_src, interval):
        self.video = cv2.VideoCapture(video_src)
        self.total = self.video.get(cv2.CAP_PROP_FRAME_COUNT)
        self.interval = interval
        self.count = interval

    #returns a single frame from the video
    def get_frame(self):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, self.count - 1)
        success, frame = self.video.read()
        if success:
            self.count += self.interval
            self.video.set(cv2.CAP_PROP_POS_FRAMES, self.count - 1)
            return frame
    
    # Retrieves the frames from the inputted video and returns a list of frames based on the given interval.
    # An alternate implementation which does not iterate through every single frame is commented out because
    # the video.set(cv2.CAP_PROP_POS_FRAMES, count - 1) function was found to be slow.
    def get_all_frames(self):
        # 
        success, frame = self.video.read()
        count = 1
        frames = []

        while success:
            if count % self.interval == 0:
                
                scale_percent = 30
                width = int(frame.shape[1] * scale_percent / 100)
                height = int(frame.shape[0] * scale_percent / 100)
                dim = (width, height)
                frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                

                frames.append(frame)
            
            success, frame = self.video.read()
            count += 1


        '''
        total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        count = interval
        video.set(cv2.CAP_PROP_POS_FRAMES, count - 1)
        success, frame = video.read()

        while count <= total_frames and success:
            frames.append(frame)
            print("Frame ", count, "Saved.")
            count += interval
            video.set(cv2.CAP_PROP_POS_FRAMES, count - 1)
            success, frame = video.read()
        '''
        print("Retrieved Frames.")
        return frames

    # Generates a new video with the given frames and bounding box (to do)
    def create_video(frames, masks, box):
        pass
