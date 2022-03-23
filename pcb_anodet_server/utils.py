from base64 import b64encode, b64decode
import numpy as np
import cv2
from datetime import datetime
from PIL import Image
from io import BytesIO


def take_photo(camera):
    """Take photo with the device given"""
    _, image = camera.read()
    return image


def save_photo(image, path, project_name):
    """Take image and save it as a jpg file in the folder "images" """
    image_path = path
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d-%X")
    file_name = (project_name + date_str + ".jpg")
    image.save(image_path + file_name)
    return file_name


def crop(image, x_1, x_2, y_1, y_2):
    """Crops the image to desired size"""
    if image.shape[0] < 2 or image.shape[1] < 2:
        return image
    return image[y_1:y_2, x_1:x_2]  # Returns images as a sliced lists


def mask(image, x_1, x_2, y_1, y_2, color):
    """Masks out undesired area"""
    if image.shape[0] < 2 or image.shape[1] < 2:
        return image
    image[x_1:x_2, y_1:y_2] = color
    return image


def ndarray_to_b64(numpy_array):
    """Turns array into base64"""
    _, buff = cv2.imencode('.jpg', numpy_array)
    jpg_as_text = b64encode(buff)
    b64_image_string = "data:image/" + "JPEG" + ";base64," \
        + str(jpg_as_text.decode("utf-8"))

    return b64_image_string


def b64_to_ndarray(b64_image_string):
    """Turns base64 into array"""
    b64 = b64_image_string[b64_image_string.find(','):]
    img = Image.open(BytesIO(b64decode(b64)))
    numpy_array = np.array(img)
    return numpy_array
