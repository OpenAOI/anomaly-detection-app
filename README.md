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
$ cd pcb-anodet-server
$
$ # Virtualenv modules installation (Unix based systems)
$ python3 -m venv "pcb-anodet-server-env"
$ source pcb-anodet-server-env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv pcb-anodet-server-env
$ # .\pcb-anodet-server-env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Run the Jinja Template
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the UI in browser: http://127.0.0.1:5000/
```

<br />

## Code-base structure

The project has a simple structure, represented as bellow:

```bash
< PROJECT ROOT >
	|-- pcb_anodet_server/
	|   |-- projects/
	|   |-- static/
	|   |   |-- css/
	|   |   |   |-- cropper.css
	|   |   |   |-- image-gallery.css
	|   |   |   |-- main.css
	|   |   |   |-- stream.css
	|   |   |   +-- train-menu-overview.css
	|   |   |-- images/
	|   |   |   +-- modal-images.css
	|   |   +-- js/
	|   |       +-- cropper.js
	|   |-- templates/
	|   |   |-- edit/
	|   |   |   |-- base_edit.html
	|   |   |   |-- crop_camera.html
	|   |   |   |-- take_photo.html
	|   |   |   |-- train_project.html
	|   |   |   +-- view_images.html
	|   |   |-- errors/
	|   |   |   +-- 404.html
	|   |   |-- base.html
	|   |   |-- predict.html
	|   |   +-- select_project.html
	|   |-- __init__.py
	|   |-- api.py
	|   |-- camera_stream.py
	|   |-- conf_template.json
	|   |-- config.py
	|   |-- forms.py
	|   |-- gen_projects.py
	|   |-- get_projects.py
	|   |-- predict.py
	|   |-- project_functions.py
	|   |-- training.py
	|   |-- update_projects.py
	|   +-- utils.py
	|-- .gitignore
	|-- README.md
	+-- run.py

```

<br />


## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website
- [Cropper.js](https://github.com/fengyuanchen/cropperjs/) - JavaScript image cropper
- [Jinja Templates](https://appseed.us/jinja-template) - Jinja templates
- [Jinja2](https://jinja.palletsprojects.com/) - Render Engine: Flask
- [Bootstrap](https://getbootstrap.com/) - UI Kit: Swipe Bootstrap 3 (Free Version) by Themesberg
<br />



