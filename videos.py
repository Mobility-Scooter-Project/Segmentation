'''
Videos File
-Handles all logic relating to video manipulation
'''

# Retrieves the frames from the inputted video and returns a list of frames based on the given interval.
# An alternate implementation which does not iterate through every single frame is commented out because
# the video.set(cv2.CAP_PROP_POS_FRAMES, count - 1) function was found to be slow.
def get_frames(video, interval):
    # 
    success, frame = video.read()
    count = 1
    frames = []

    while success:
        if count % interval == 0:
            frames.append(frame)
        
        success, frame = video.read()
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

# Generates a new video with the given frames and bounding box that 
def create_video(frames, masks, box):
    pass