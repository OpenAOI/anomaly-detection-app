from os import path, mkdir
server_path = "/home/plejd/Desktop/AOI/pcb-anodet-server/hidden_aoi/pcb_anodet_server/"


def create_project(project_name):
    full_path = server_path + "projects/" + project_name
    if path.isdir(full_path):
        return False  # returns False if path already exists

    mkdir(full_path)
    mkdir(full_path + "/distributions")
    mkdir(full_path + "/images")

    with open(server_path + "conf_template.json", "r") as f, open(full_path + "/conf.json", "w") as to:

        to.write(f.read())
    return True  # returns True if created

