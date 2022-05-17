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
│   ├── Media/
│   │   └── pcb-anodet-server-preview.gif
│   ├── project_routes/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── projects/
│   ├── static/
│   │   ├── css/
│   │   │   ├── cropper.css
│   │   │   ├── image-gallery.css
│   │   │   ├── main.css
│   │   │   └── train-menu-overview.css
│   │   └── js/
│   │       └── cropper.js
│   ├── templates/
│   │   ├── errors/
│   │   │   └── 404.html
│   │   ├── evaluate/
│   │   │   └── evaluate.html
│   │   ├── includes/
│   │   │   ├── guide.html
│   │   │   ├── navigation.html
│   │   │   ├── navigation_train.html
│   │   │   └── train_overview.html
│   │   ├── layouts/
│   │   │   ├── base.html
│   │   │   └── base_train.html
│   │   ├── train/
│   │   │   ├── crop_camera.html
│   │   │   ├── preview_images.html
│   │   │   ├── take_image.html
│   │   │   └── train_project.html
│   │   └── index.html
│   ├── views/
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── __init__.py
│   ├── camera_stream.py
│   ├── conf_template.json
│   ├── config.py
│   ├── gen_projects.py
│   ├── get_projects.py
│   ├── predict.py
│   ├── project_functions.py
│   ├── training.py
│   ├── update_projects.py
│   └── utils.py
├── .gitignore
├── README.md
├── requirements.txt
└── run.py

```

<br />


## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website
- [Cropper.js](https://github.com/fengyuanchen/cropperjs/) - JavaScript image cropper
- [Jinja Templates](https://appseed.us/jinja-template) - Jinja templates
- [Jinja2](https://jinja.palletsprojects.com/) - Render Engine: Flask
- [Bootstrap](https://getbootstrap.com/) - UI Kit: Swipe Bootstrap 3 (Free Version) by Themesberg
<br />



