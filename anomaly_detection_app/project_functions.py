from anomaly_detection_app import (
    gen_projects,
    utils,
    predict,
    get_projects,
    update_projects,
    training,
    camera_stream,
)
import cv2
import shutil
from PIL import Image
from numpy import asarray
from anomaly_detection_app.config import project_path
from typing import Any, Tuple


PRED_IMAGE = None
CAMERA = camera_stream.CameraStream()


def delete_project(project_name: str) -> None:
    """Delete project"""
    path = project_path + project_name
    shutil.rmtree(path)


def delete_image(project_name: str, image_name: str) -> None:
    """Delete image"""
    file_path = project_path + project_name + "/images/" + image_name
    utils.delete_file(file_path)


def return_latest_image_array() -> Any:
    """Return the latest array from camera class without claming the camera feed"""
    return CAMERA.return_image()


def return_latest_photo() -> str:
    """Returns the latest array as an image from camera class without claming the camera feed"""
    CAMERA.read()
    array = CAMERA.return_image()
    image_b64 = utils.ndarray_to_b64(array)
    return image_b64


def init_project(new_project_name: str) -> str:
    """Generate folders and config-files for a new project"""
    success = gen_projects.create_project(new_project_name)

    return success


def crop_project_photo(project_name: str, image: Any) -> Any:
    """Crop the image to the size specified in projects config json"""

    crop_conf = get_projects.get_crop_config(project_name)
    x_1 = crop_conf["x_1"]  # X start value
    y_1 = crop_conf["y_1"]  # Y start value
    x_2 = crop_conf["x_2"]  # X end value
    y_2 = crop_conf["y_2"]  # Y end value
    cropped_image = utils.crop(image, x_1, x_2, y_1, y_2)
    return cropped_image


'''
def mask_project_photo(project_name, image):
    """Will be implemented when someone needs to mask the images in their project"""
    """Mask out unwanted area of project image"""
    mask_conf = get_projects.get_mask_config(project_name)
    x_1 = mask_conf["mask_parameters"]["x_1"]
    x_2 = mask_conf["mask_parameters"]["x_2"]
    y_1 = mask_conf["mask_parameters"]["y_1"]
    y_2 = mask_conf["mask_parameters"]["y_2"]
    color = mask_conf["mask_color"]
    return utils.mask(image, x_1, x_2, y_1, y_2, color)
'''


def gen(project_name: str) -> Any:
    """Generates camera stream"""

    while True:
        image = CAMERA.read()
        cropped_image = crop_project_photo(project_name, image)
        _, jpeg = cv2.imencode(".jpg", cropped_image)
        frame = jpeg.tobytes()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


def predict_project_photo(project_name: str) -> Tuple[Any, float, int]:
    """Uses the trained model to make an evaluation of an image of a project"""
    thresh_conf = get_projects.get_threshold_config(project_name)
    thresh = thresh_conf["threshold"]
    model_path = project_path + project_name + "/distributions/"
    array = return_latest_image_array()
    cropped_array = crop_project_photo(project_name, array.copy())
    image_pred, score, image_class = predict.predict_image(
        cropped_array, thresh, model_path
    )
    image_pred_b64 = utils.ndarray_to_b64(image_pred)

    return image_pred_b64, score, thresh, image_class


def save_project_photo(project_name: str) -> str:
    """Saves an un-evaluated image of a project"""
    array = return_latest_image_array()  # TODO: Fix camera value 0
    cropped_array = crop_project_photo(project_name, array.copy())
    cropped_image = Image.fromarray(cropped_array)
    file_name = utils.save_photo(
        cropped_image, project_path + project_name + "/images/", project_name
    )
    return file_name


"""

def update_project_camera(camera, camera_type):
    '''Will be implemented when someone wants to put the camera choice in the front end'''
    '''Updates the camera configuration'''
    if camera_type == "USB":
        camera = int(camera)
    update_projects.update_camera(PROJECT_NAME, camera, camera_type)

"""


def update_project_threshold(project_name, threshold):
    """Updates the threshold configuration"""
    update_projects.update_threshold(project_name, int(threshold))


def update_project_crop(
    project_name: str, x_1: int, x_2: int, y_1: int, y_2: int
) -> None:
    """Updates the camera configuration"""
    update_projects.update_crop(project_name, (x_1), (x_2), (y_1), (y_2))


def train(project_name: str) -> None:
    """Trains model on collected images"""
    path = project_path + project_name
    training.train(path)


def get_all_projects() -> dict[str : list[dict[str:str]]]:
    """Get all projects"""
    return get_projects.get_all_projects()


def get_all_project_images(project_name: str) -> dict[str : list[dict[str:str]]]:
    """Get all images from the selected projects image folder"""
    path = project_path + project_name + "/images/"
    image_names_dict = get_projects.get_all_image_names(project_name)
    for image in image_names_dict["images"]:
        image_name_path = path + image["name"]
        with Image.open(image_name_path) as im:
            b64image = utils.ndarray_to_b64(asarray(im))
        image["image_b64"] = b64image
    return image_names_dict
