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

    def make_video(self, frame, out):
        size = list(frame.shape)
        del size[2]
        size.reverse()
        self.writer = cv2.VideoWriter(out, cv2.VideoWriter_fourcc(*'mp4v'), 30, size)

    def append_frame(self, frame, mask, box):
        h, w = mask.shape[-2:]
        new_image = frame * mask.reshape(h, w, 1)
        new_image = cv2.rectangle(new_image, (int(box[0].item()), int(box[1].item())), 
                              (int(box[2].item()), int(box[3].item())), (0, 255, 0), 2)
        self.writer.write(new_image)

    def release_video(self):
        self.writer.release()