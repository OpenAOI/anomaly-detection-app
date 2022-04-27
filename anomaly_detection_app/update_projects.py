from anomaly_detection_app.config import project_path
from anomaly_detection_app import get_projects
import json
from typing import Any


def update(project_name: str, settings: dict) -> None:
    with open(project_path + project_name + "/conf.json", "w") as f:
        json.dump(settings, f, indent=4)


def update_crop(project_name: str, x_1: int, x_2: int, y_1: int, y_2: int) -> None:
    conf = get_projects.load_conf(project_name)
    conf["crop_config"]["crop_parameters"] = {
        "x_1": x_1,
        "x_2": x_2,
        "y_1": y_1,
        "y_2": y_2,
    }
    update(project_name, conf)


"""
def update_mask(project_name: str, x_1: int , x_2: int, y_1: int, y_2: int, color=255) -> None:
    conf = get_projects.load_conf(project_name)
    conf["mask_config"]["mask_parameters"] = {
        "x_1": x_1,
        "x_2": x_2,
        "y_1": y_1,
        "y_2": y_2,
    }
    conf["mask_config"]["mask_color"] = color
    update(project_name, conf)
"""


def update_camera(project_name: str, camera: Any, camera_type: Any) -> Any:
    conf = get_projects.load_conf(project_name)
    conf["camera_config"]["camera"] = camera
    conf["camera_config"]["camera_type"] = camera_type

    update(project_name, conf)


def update_threshold(project_name: str, thresh: float) -> None:
    conf = get_projects.load_conf(project_name)
    conf["threshold_config"]["threshold"] = thresh
    update(project_name, conf)
