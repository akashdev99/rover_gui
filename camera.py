from time import time

class Camera(object):
    def __init__(self):
        self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
        #https://stackoverflow.com/questions/49939859/flask-video-stream-using-opencv-images
    def get_frame(self):
        return self.frames[int(time()) % 3]