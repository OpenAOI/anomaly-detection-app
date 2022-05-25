# Web based interface for open/AOI

This is a web based interface for visual anomaly detection. It's built using Flask and Bootstrap. 
The focus of this project is to make training and evaluation easy for any and all end user. From collecting data (images) and training the model to evaluating anomalies in many different use cases.

<br />

> Links

- [Open AOI](https://github.com/OpenAOI) - Open AOI

<br />

## The web interface

Gif to demo project.

<br />

![Website preview](anomaly_detection_app/Media/pcb-anodet-server-preview.gif)

<br />

## Build from sources


<br />
Pytorch needs to be downloaded from https://pytorch.org/get-started/locally/
This is because the download and installation is dependent on your setup.
Pytorch is therefore not included in the requirements file.
<br />

```bash
$ # Clone the sources
$ git clone https://github.com/OpenAOI/pcb-anodet-server.git
$ cd anomaly-detection-app
$
$ # Virtualenv modules installation (Unix based systems)
$ python3 -m venv "anomaly-detection-app-env"
$ source anomaly-detection-app-env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ virtualenv anomaly-detection-app-env
$ .\anomaly-detection-app-env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Install anodet
$ # Check out the anodet repository README.md for a more detailed installation
$ git clone https://github.com/OpenAOI/anodet.git
$ cd anodet
$ python -m pip install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ (Unix/Mac) export FLASK_ENV=development
$ (Windows) set FLASK_ENV=development
$ (Powershell) $env:FLASK_ENV = "development"
$
$ # Run the Jinja Template
$ --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the UI in browser: 
$ http://127.0.0.1:5000/
```

<br />

## Code-base structure

The project has a simple structure, represented as bellow:

```bash
< PROJECT ROOT >
.
├── anomaly_detection_app/
│   │   
│   ├── Media/                                 # Media used by README.md
│   │   └── pcb-anodet-server-preview.gif
│   │   
│   ├── project_routes/                        # Handles projects routes
│   │   ├── __init__.py                        # Includes a blueprint object
│   │   └── routes.py                          # Define project routes
│   │   
│   ├── projects/                              # Containing unique projects folders for settings and data 
│   │   
│   ├── static/                                # CSS files, Javascripts files
│   │   │ 
│   │   ├── css/
│   │   │   ├── cropper.css                    # Used by cropper at crop_camera.html
│   │   │   ├── image-gallery.css              # Image gallery used by preview_images.html
│   │   │   ├── main.css                       # Main css style
│   │   │   └── train-menu-overview.css        # Train overview used by base_train.html
│   │   │ 
│   │   └── js/
│   │       └── cropper.js                     # Used by cropper at crop_camera.html
│   │   
│   ├── templates/                             # Templates used to render pages
│   │   │ 
│   │   ├── errors/                            # UI error pages
│   │   │   ├── 401.html                       # 401 authentication
│   │   │   └── 404.html                       # 404 not found
│   │   │ 
│   │   ├── evaluate/                          # UI evaluation pages
│   │   │   └── evaluate.html                  
│   │   │ 
│   │   ├── includes/                          # HTML chunks and components
│   │   │   ├── guide.html                     # Help guide component
│   │   │   ├── navigation.html                # Top menu component
│   │   │   ├── navigation_train.html          # Top menu component for training pages
│   │   │   └── train_overview.html            # Train overview component
│   │   │ 
│   │   ├── layouts/                           # Master pages
│   │   │   ├── base.html                      # Main master page
│   │   │   └── base_train.html                # Master page for training pages
│   │   │ 
│   │   ├── train/                             # UI training pages
│   │   │   ├── crop_camera.html               # Crop photo from camera
│   │   │   ├── preview_images.html            # Preview photos
│   │   │   ├── take_image.html                # Take photos from camera
│   │   │   └── train_project.html             # Train project
│   │   │ 
│   │   └── index.html                         # UI index page
│   │   
│   ├── views/                                 # Handles app views routes
│   │   ├── __init__.py                        # Includes a blueprint object
│   │   ├── forms.py                           # Form for creating a project
│   │   └── routes.py                          # Define view routes
│   │   
│   ├── __init__.py                            # Functions for creating a flask app
│   ├── camera_stream.py                       # On going camera stream
│   ├── conf_template.json                     # Project template settings
│   ├── config.py                              # Store server path, ip, device type
│   ├── gen_projects.py                        # For creating a new project
│   ├── get_projects.py                        # Get project settings
│   ├── predict.py                             # Connects to anodet for evaluation
│   ├── project_functions.py                   # Several functions for a project
│   ├── training.py                            # Connects to anodet for training a project
│   ├── update_projects.py                     # Update project settings
│   └── utils.py                               # Independent utils functions
├── .gitignore
├── README.md
├── requirements.txt                           # Development modules
└── run.py                                     # Start the app 

```

<br />
In the config.py file you should change the ip-adress to your local ip-adress. <br />
You can also change between 'cpu' and 'cuda' devices. If your computer is set up for use with a graphics card, you can run 'cuda'. Else choose 'cpu'. <br />
If you would like to use an ip-camera or a rtsp-stream instead of usb- camera, you can change the camera value in camera_stream.py. <br />
<br />

For example, this is usb camera 0 (passed in as an int): <br />
def __init__(self, stream_id=0) -> None: <br />
<br />
This is a rtsp stream (passed in as a string): <br />
def __init__(self, stream_id='rtsp://example.com/media.mp4') -> None:<br />


<br />
If the resolution of the training image is to be changed, that is done in the anodet/anodet/utils.py

<br />

## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website
- [Cropper.js](https://github.com/fengyuanchen/cropperjs/) - JavaScript image cropper
- [Jinja Templates](https://appseed.us/jinja-template) - Jinja templates
- [Jinja2](https://jinja.palletsprojects.com/) - Render Engine: Flask
- [Bootstrap](https://getbootstrap.com/) - UI Kit: Swipe Bootstrap 3 (Free Version) by Themesberg
<br />



