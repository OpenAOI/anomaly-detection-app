import gen_projects
import utils
import cv2
import os
from PIL import Image
import predict
import get_projects
import update_projects
import training
from numpy import asarray
from camera_stream import CameraStream

PRED_IMAGE = None
CAMERA = CameraStream()


def return_latest_image_array():
    """Returns the latest array from camera class without claming the camera feed"""
    return CAMERA.return_image()


def return_latest_photo():
    """Returns the latest array as an image from camera class without claming the camera feed"""
    CAMERA.read()
    array = CAMERA.return_image()
    image_b64 = utils.ndarray_to_b64(array)
    return image_b64


def init_project(new_project_name):
    """Generate folders and config-files for a new project"""
    success = gen_projects.create_project(new_project_name)

    return success


def crop_project_photo(project_name, image):
    """Crops the image to the size specified in projects config json"""

    crop_conf = get_projects.get_crop_config(project_name)
    x_1 = crop_conf["x_1"]  # X start value
    y_1 = crop_conf["y_1"]  # Y start value
    x_2 = crop_conf["x_2"]  # X end value
    y_2 = crop_conf["y_2"]  # Y end value
    cropped_image = utils.crop(image, x_1, x_2, y_1, y_2)
    return cropped_image


'''
def mask_project_photo(project_name, image):
    """Mask out unwanted area of project image"""
    mask_conf = get_projects.get_mask_config(project_name)
    x_1 = mask_conf["mask_parameters"]["x_1"]
    x_2 = mask_conf["mask_parameters"]["x_2"]
    y_1 = mask_conf["mask_parameters"]["y_1"]
    y_2 = mask_conf["mask_parameters"]["y_2"]
    color = mask_conf["mask_color"]
    return utils.mask(image, x_1, x_2, y_1, y_2, color)


def take_project_photo():
    """Take photo of project"""
    image = utils.take_photo(CAMERA)
    cropped_project_photo = crop_project_photo(image)
    return cropped_project_photo
'''


def gen(project_name):
    """Generates camera stream"""

    while True:
        image = CAMERA.read()
        cropped_image = crop_project_photo(project_name, image)
        _, jpeg = cv2.imencode(".jpg", cropped_image)
        frame = jpeg.tobytes()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


def predict_project_photo(project_name):
    """Uses the trained model to make an evaluation of an image of a project"""
    path = get_projects.get_path_config(project_name)
    thresh_conf = get_projects.get_threshold_config(project_name)
    thresh = thresh_conf["threshold"]
    array = return_latest_image_array()
    cropped_array = crop_project_photo(project_name, array.copy())
    image_pred, score = predict.predict_image(cropped_array, path, thresh)
    image_pred_b64 = utils.ndarray_to_b64(image_pred)

    return image_pred_b64, score, thresh


def save_project_photo(project_name):
    """Saves an un-evaluated image of a project"""
    path_conf = get_projects.get_path_config(project_name)
    path = path_conf
    array = return_latest_image_array()  # TODO: Fix camera value 0
    cropped_array = crop_project_photo(project_name, array.copy())
    image = Image.fromarray(array)
    cropped_image = Image.fromarray(cropped_array)
    utils.save_photo(cropped_image, path + "/processed_images/", project_name)
    return utils.save_photo(image, path + "/images/", project_name)


def return_saved_project_photo(project_name):
    """Fetch photo from disc to display in gui"""
    images = []
    path_conf = get_projects.get_path_config(project_name)
    img_path = path_conf + "/images"
    for path in os.listdir(img_path):
        full_path = os.path.join(img_path, path)
        if os.path.isfile(full_path):
            images.append(full_path)
    if len(images) > 0:
        with Image.open(images[-1]) as im:
            b64image = utils.ndarray_to_b64(asarray(im))
    else:
        return None
    return b64image


"""
def update_project_camera(camera, camera_type):
    '''Updates the camera configuration'''
    if camera_type == "USB":
        camera = int(camera)
    update_projects.update_camera(PROJECT_NAME, camera, camera_type)


def update_project_threshold(threshold):
    '''Updates the threshold configuration'''
    update_projects.update_threshold(PROJECT_NAME, int(threshold))
"""


def update_project_crop(project_name, x_1, x_2, y_1, y_2):
    """Updates the camera configuration"""
    update_projects.update_crop(project_name, int(x_1), int(x_2), int(y_1), int(y_2))


def train(project_name):
    """Trains model on collected images"""
    path = get_projects.get_path_config(project_name)
    training.train(path)


def get_all_projects():
    return get_projects.get_all_projects()


def get_all_project_images(project_name):
    path = get_projects.get_path_config(project_name) + "/processed_images/"
    image_names_dict = get_projects.get_all_image_names(project_name)
    for image in image_names_dict["images"]:
        image_name = path + image["name"]
        with Image.open(image_name) as im:
            b64image = utils.ndarray_to_b64(asarray(im))
        image["image_b64"] = b64image
    return image_names_dict
