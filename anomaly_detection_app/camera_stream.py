import cv2
from threading import Thread
from typing import Any


class CameraStream:
    """
    The CameraStream object puts images captured from a camera
    into different threads to gain processing speed and puts
    out a stream of these captured images or a single frame
    which is the latest image captured.

    :stream_id will take an int for an usb-camera or
    a string for an ip- or or rtsp-camera.

    """

    def __init__(self, stream_id=0) -> None:
        self.stream_id = stream_id

        # Open the video capture stream
        self.camera = cv2.VideoCapture(self.stream_id)
        if self.camera.isOpened() is False:
            print("[Exiting]: Error accessing webcam stream.")
            exit(0)

        # Read a single image from camera stream for initializing
        self.success, self.image = self.camera.read()
        if self.success is False:
            print("[Exiting] No more images to read.")
            exit(0)  # Initialize self.stop to False
        self.stopped = True  # Instantiate thread
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True  # Run daemon threads in the background

    def start(self) -> None:
        """
        Start thread. Pass image to the next available
        thread to read next available image.
        """
        self.stopped = False
        self.t.start()

    def update(self) -> None:
        """Call read if not stopped and is possible."""
        while True:
            if self.stopped is True:
                break
            self.success, self.image = self.camera.read()
            if self.success is False:
                print("[Exiting] No more images to read.")
                self.stopped = True
                break
        self.camera.release()

    def read(self) -> Any:
        """Calls the camera to read a single frame."""
        _, self.image = self.camera.read()
        return self.image

    def stop(self) -> None:
        """Stop the update function."""
        self.stopped = True

    def return_image(self) -> Any:
        """Return locally stored image."""
        return self.image
