import cv2
from threading import Thread
from typing import Any


class CameraStream:
    def __init__(self, stream_id=0) -> None:
        self.stream_id = stream_id  # Will take an int for USB-camera
        # or str for ip- or rtsp-camera

        # opening video capture stream
        self.camera = cv2.VideoCapture(self.stream_id)
        if self.camera.isOpened() is False:
            print("[Exiting]: Error accessing webcam stream.")
            exit(0)

        # reading a single image from camera stream for initializing
        self.success, self.image = self.camera.read()
        if self.success is False:
            print("[Exiting] No more images to read")
            exit(0)  # self.stopped is initialized to False
        self.stopped = True  # thread instantiation
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True  # daemon threads run in background

    # method to start thread
    def start(self) -> None:
        self.stopped = False
        self.t.start()  # method passed to thread to read next available image

    def update(self) -> None:
        while True:
            if self.stopped is True:
                break
            self.success, self.image = self.camera.read()
            if self.success is False:
                print("[Exiting] No more images to read")
                self.stopped = True
                break
        self.camera.release()  # method to return latest read image

    def read(self) -> Any:
        _, self.image = self.camera.read()
        return self.image  # method to read images

    def stop(self) -> None:
        self.stopped = True

    def return_image(self) -> Any:
        return self.image
