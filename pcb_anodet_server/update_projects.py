from get_projects import load_conf
import json


def update(project_name, settings):
    with open(settings["path_config"]["path"] + project_name + "/conf.json", "w") as f:
        json.dump(settings, f, indent=4)


def update_crop(project_name, x_1, x_2, y_1, y_2):
    conf = load_conf(project_name)
    conf["crop_config"]["crop_parameters"] = {
        "x_1": x_1,
        "x_2": x_2,
        "y_1": y_1,
        "y_2": y_2,
    }
    update(project_name, conf)


def update_mask(project_name, x_1, x_2, y_1, y_2, color=255):
    conf = load_conf(project_name)
    conf["mask_config"]["mask_parameters"] = {
        "x_1": x_1,
        "x_2": x_2,
        "y_1": y_1,
        "y_2": y_2,
    }
    conf["mask_config"]["mask_color"] = color
    update(project_name, conf)


def update_camera(project_name, camera, camera_type):
    conf = load_conf(project_name)
    conf["camera_config"]["camera"] = camera
    conf["camera_config"]["camera_type"] = camera_type

    update(project_name, conf)


def update_threshold(project_name, thresh):
    conf = load_conf(project_name)
    conf["threshold_config"]["threshold"] = thresh
    update(project_name, conf)
