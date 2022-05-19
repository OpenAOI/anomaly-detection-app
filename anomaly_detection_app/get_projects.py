import json
from os import listdir, path
from anomaly_detection_app.config import project_path
from typing import Union


def load_conf(project_name: str) -> str:
    """Read cofniguration file from the selected project."""
    with open(project_path + project_name + "/conf.json") as f:
        conf = json.load(f)

    return conf


def get_crop_config(project_name: str) -> str:
    """Load the crop-values from the active projects conf file"""
    conf = load_conf(project_name)

    return conf["crop_config"]["crop_parameters"]


def get_mask_config(project_name: str) -> str:
    """Load the mask-values from the active projects conf file"""
    conf = load_conf(project_name)

    return conf["mask_config"]


def get_camera_config(project_name: str) -> str:
    """Load the camera selection from the active projects conf file"""
    conf = load_conf(project_name)

    return conf["camera_config"]


def get_threshold_config(project_name: str) -> str:
    """Load the threshold from the active projects conf file"""
    conf = load_conf(project_name)

    return conf["threshold_config"]


def get_all_projects() -> dict[str : list[dict[str:str]]]:
    """Get all existing projects"""
    projects = listdir("anomaly_detection_app/projects/")
    project_dict = {"projects": []}

    # Return empty if no folder exist
    if not path.isdir(project_path):
        return project_dict

    projects = listdir(project_path)
    for p in projects:
        project_dict["projects"].append({"name": p})
    return project_dict


def get_all_image_names(project_name: str) -> dict[str : list[dict[str:str]]]:
    """Get all of the image names from the active projects image folder"""
    images = listdir(project_path + project_name + "/images/")
    image_names_dict = {"images": [{"name": i} for i in images]}
    return image_names_dict
