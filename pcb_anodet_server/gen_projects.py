from os import path, mkdir
from pcb_anodet_server.config import project_path, server_path


def create_project(project_name):
    full_path = project_path + project_name
    if path.isdir(full_path):
        return False  # returns False if path already exists

    mkdir(full_path)
    mkdir(full_path + "/distributions")
    mkdir(full_path + "/images")
    mkdir(full_path + "/processed_images")
    with open(server_path + "/conf_template.json", "r") as f, open(
        full_path + "/conf.json", "w"
    ) as to:

        to.write(f.read())
    return True  # returns True if created
