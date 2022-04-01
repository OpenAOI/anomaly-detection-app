import cv2
from threading import Thread


class CameraStream:
    def __init__(self, stream_id=0):
        self.stream_id = stream_id

        # opening video capture stream
        self.camera = cv2.VideoCapture(self.stream_id)
        if self.camera.isOpened() is False:
            print("[Exiting]: Error accessing webcam stream.")
            exit(0)
        fps_input_stream = int(self.camera.get(5))  # hardware fps
        print("FPS of input stream: {}".format(fps_input_stream))

        # reading a single image from camera stream for initializing
        self.success, self.image = self.camera.read()
        if self.success is False:
            print('[Exiting] No more images to read')
            exit(0)        # self.stopped is initialized to False
        self.stopped = True  # thread instantiation
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True  # daemon threads run in background

    # method to start thread
    def start(self):
        self.stopped = False
        self.t.start()    # method passed to thread to read next available image

    def update(self):
        while True:
            if self.stopped is True:
                break
            self.success, self.image = self.camera.read()
            if self.success is False:
                print('[Exiting] No more images to read')
                self.stopped = True
                break
        self.camera.release()    # method to return latest read image

    def read(self):
        _, self.image = self.camera.read()
        return self.image    # method to stop reading images

    def stop(self):
        self.stopped = True

    def return_image(self):
        return self.image
