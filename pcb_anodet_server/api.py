from flask import Blueprint, json, render_template, request, url_for, Response
import project_functions
import utils


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route("/ping", methods=["GET", "POST"])
def ping():
    """Ping to check connection to server"""
    return "pong"


@api_blueprint.route('/video_feed')
def video_feed():
    return Response(project_functions.gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@api_blueprint.route("/take_photo_and_predict", methods=["GET", "POST"])
def take_photo_and_predict():
    """Take picture, make, prediction and return original,
    heatmap, score and threshhold"""
    project_name = request.args.get('project_name', None)
    image = project_functions.return_latest_photo()
    image_org, image_pred, score, thresh = project_functions.predict_project_photo(project_name, image)
    image_org_b64 = utils.ndarray_to_b64(image_org)
    image_pred_b64 = utils.ndarray_to_b64(image_pred)
    return json.dumps({"image_org_b64": image_org_b64,
                       "image_pred_b64": image_pred_b64,
                       "score": score, "thresh": thresh})


@api_blueprint.route("/save_photo", methods=["GET", "POST"])
def save_photo():
    """Save the image to folder "images" """
    project_name = request.args.get('project_name', None)
    save_path = project_functions.save_project_photo(project_name)
    return save_path


@api_blueprint.route("/return_saved_photo", methods=["GET", "POST"])
def return_saved_photo():
    project_name = request.args.get('project_name', None)
    project_functions.save_project_photo(project_name)  # TODO Put in frontend
    image = project_functions.return_saved_project_photo(project_name)
    return image


@api_blueprint.route("/update_crop", methods=["GET", "POST"])
def update_crop():
    project_name = request.args.get('project_name', None)
    x_1 = request.args.get('x_1', None)
    x_2 = request.args.get('x_2', None)
    y_1 = request.args.get('y_1', None)
    y_2 = request.args.get('y_2', None)
    project_functions.update_project_crop(project_name, x_1, x_2, y_1, y_2)
    return "success"


"""
@api_blueprint.route("/update_camera", methods=["GET", "POST"])
def update_camera():
    project_name = request.args.get('project_name', None)
    camera = request.args.get('camera', None)
    camera_type = request.args.get('camera_type', None)
    project_functions.update_project_camera(project_name, camera, camera_type)
    return "success"
"""


@api_blueprint.route("/init_project", methods=["GET", "POST"])
def init_project():
    new_project_name = request.args.get('new_project_name', None)
    project_functions.init_project(new_project_name)
    return "success"


@api_blueprint.route("/update_threshold", methods=["GET", "POST"])
def update_threshold():
    project_name = request.args.get('project_name', None)
    threshold = request.args.get('threshold', None)
    project_functions.update_project_threshold(project_name, threshold)
    return "success"


@api_blueprint.route("/change_project", methods=["GET", "POST"])
def change_project():
    project_name = request.args.get('project_name', None)
    project_functions.change_project(project_name)
    return "success"


@api_blueprint.route("/train", methods=["GET", "POST"])
def train():
    """Train model on collected images"""
    project_name = request.args.get('project_name', None)
    project_functions.train(project_name)
    return "success"


@api_blueprint.route("/get_projects", methods=["GET", "POST"])
def get_projects():
    """Get all the project names"""
    projects = project_functions.get_all_projects()
    return projects


@api_blueprint.route("/get_all_project_images", methods=["GET", "POST"])
def get_all_project_images():
    """Get all the project names"""
    project_name = request.args.get('project_name', None)
    images = project_functions.get_all_project_images(project_name)
    return images


"""HTML routes"""


@api_blueprint.route('/predict', methods=["GET", "POST"])
def predictv():
    # project_name = request.args.get('project', None)
    # project_functions.change_project(project_name)
    return render_template("predict.html")


@api_blueprint.route('/edit/crop_camera', methods=["GET", "POST"])
def crop_camerav():
    return render_template("edit/crop_camera.html")


@api_blueprint.route('/edit/take_photo', methods=["GET", "POST"])
def take_photov():
    return render_template("edit/take_photo.html")


@api_blueprint.route('/edit/view_images', methods=["GET", "POST"])
def view_imagesv():
    return render_template("edit/view_images.html")


@api_blueprint.route('/edit/train_project', methods=["GET", "POST"])
def train_projectv():
    return render_template("edit/train_project.html")


""" Select project page """


@api_blueprint.route('/', methods=["GET", "POST"])
@api_blueprint.route('/select_project', methods=["GET", "POST"])
def select_projectv():
    return render_template("select_project.html")


""" Error pages """


@api_blueprint.errorhandler(404)
def error_404v(error):
    return render_template('errors/404.html'), 404
