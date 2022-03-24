import gen_projects
import utils
import cv2
import os
from PIL import Image
from predict import predict_image
import get_projects
import update_projects
import training
from numpy import asarray

CAMERA = cv2.VideoCapture(0)
PROJECT_NAME = ""


def change_project(selected_project):
    """Change the global variable that is the project you are currently working on"""
    global PROJECT_NAME, CAMERA
    PROJECT_NAME = selected_project
    cam_conf = get_projects.get_camera_config(selected_project)
    try:
        CAMERA.release()
    except:
        pass
    finally:
        CAMERA = cv2.VideoCapture(cam_conf["camera"])


def init_project(new_project_name):
    """Generate folders and config-files for a new project"""
    global PROJECT_NAME
    success = gen_projects.create_project(new_project_name)
    PROJECT_NAME = new_project_name

    return success


def crop_project_photo(image):
    """Crops the image to the size specified in projects config json """

    crop_conf = get_projects.get_crop_config(PROJECT_NAME)
    x_1 = crop_conf["x_1"]  # X start value
    y_1 = crop_conf["y_1"]  # Y start value
    x_2 = crop_conf["x_2"]  # X end value
    y_2 = crop_conf["y_2"]  # Y end value
    cropped_image = utils.crop(image, x_1, x_2, y_1, y_2)
    return cropped_image


def mask_project_photo(image):
    """Mask out unwanted area of project image"""
    mask_conf = get_projects.get_mask_config(PROJECT_NAME)
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


def predict_project_photo(image):
    """Uses the trained model to make an evaluation of an image of a project"""
    path_conf = get_projects.get_path_config(PROJECT_NAME)
    thresh_conf = get_projects.get_threshold_config(PROJECT_NAME)
    path = path_conf
    thresh = thresh_conf["threshold"]
    heatmap, score = predict_image(image, path, thresh)
    return image, heatmap, score, thresh


def save_project_photo():
    """Saves an un-evaluated image of a project"""
    path_conf = get_projects.get_path_config(PROJECT_NAME)
    path = path_conf
    array = utils.take_photo(CAMERA)
    cropped_array = crop_project_photo(array.copy())
    image = Image.fromarray(array)
    cropped_image = Image.fromarray(cropped_array)
    utils.save_photo(cropped_image, path + '/processed_images/', PROJECT_NAME)
    return utils.save_photo(image, path + '/images/', PROJECT_NAME)


def return_saved_project_photo():
    """Fetch photo from disc to display in gui"""
    images = []
    path_conf = get_projects.get_path_config(PROJECT_NAME)
    img_path = path_conf + '/processed_images'
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


def update_project_camera(camera, camera_type):
    """Updates the camera configuration"""
    if camera_type == "USB":
        camera = int(camera)
    update_projects.update_camera(PROJECT_NAME, camera, camera_type)


def update_project_threshold(threshold):
    """Updates the threshold configuration"""
    update_projects.update_threshold(PROJECT_NAME, int(threshold))


def update_project_crop(x_1, x_2, y_1, y_2):
    """Updates the camera configuration"""
    update_projects.update_crop(PROJECT_NAME, int(x_1), int(x_2), int(y_1), int(y_2))


def train():
    """Trains model on collected images"""
    path = get_projects.get_path_config(PROJECT_NAME)
    training.train(path)


def get_all_projects():
    return get_projects.get_all_projects()
