from flask import Flask
from flask import render_template
from flask import request, url_for
import os
import datetime


app = Flask(__name__, instance_relative_config=True)

""" Predict page """
@app.route('/predict/<project_id>')
def predict(project_id):
    return render_template("predict.html", project_id=project_id)


""" New project routes """
@app.route('/edit/crop_camera/<project_id>')
def crop_camera(project_id):
    return render_template("edit/crop_camera.html", project_id=project_id)

@app.route('/edit/take_photo/<project_id>')
def take_photo(project_id):
    return render_template("edit/take_photo.html", project_id=project_id)

@app.route('/edit/view_images/<project_id>')
def view_images(project_id):
    return render_template("edit/view_images.html", project_id=project_id)

@app.route('/edit/train_project/<project_id>')
def train_project(project_id):
    return render_template("edit/train_project.html", project_id=project_id)


""" Select project page """
@app.route('/')
@app.route('/select_project')
def select_project():
    return render_template("select_project.html")


""" Error pages """
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404
