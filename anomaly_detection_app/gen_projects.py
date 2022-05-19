from os import path, mkdir
from anomaly_detection_app.config import project_path, server_path


def create_project(project_name: str) -> bool:
    """Create new project folders and config file."""
    full_path = project_path + project_name
    
    # Create project folder if it doesn't exist
    if not path.isdir(project_path):
        mkdir(project_path)

    mkdir(full_path)
    mkdir(full_path + "/distributions")
    mkdir(full_path + "/images")
    with open(server_path + "/conf_template.json", "r") as f, open(
        full_path + "/conf.json", "w"
    ) as to:

        to.write(f.read())
    return True  # returns True if created
