from os import path, mkdir
from anomaly_detection_app import create_app
from anomaly_detection_app.config import project_path

app = create_app()

if not path.isdir(project_path): #Create projects folder if there is none
        mkdir(project_path) 

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
