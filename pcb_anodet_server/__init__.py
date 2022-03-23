from flask import Flask
from flask import render_template
from flask import request, url_for
import os
import datetime


app = Flask(__name__, instance_relative_config=True)

""" Predict page """
@app.route('/predict')
def predict():
    return render_template("predict.html")


""" New project routes """
@app.route('/edit/crop_camera')
def crop_camera():
    return render_template("edit/crop_camera.html")

@app.route('/edit/take_photo')
def take_photo():
    return render_template("edit/take_photo.html")

@app.route('/edit/view_images')
def view_images():
    return render_template("edit/view_images.html")

@app.route('/edit/train_project')
def train_project():
    return render_template("edit/train_project.html")


""" Select project page """
@app.route('/')
@app.route('/select_project')
def select_project():
    return render_template("select_project.html")


""" Error pages """
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404
