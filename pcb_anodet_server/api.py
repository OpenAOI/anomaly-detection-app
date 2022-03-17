from flask import Blueprint, json, render_template, request
import project_functions
import utils


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route("/ping", methods=["GET", "POST"])
def ping():
    """Ping to check connection to server"""
    return "pong"


@api_blueprint.route("/")
def index():
    """Testing videofeed js"""
    return render_template('index.html')


@api_blueprint.route("/take_photo", methods=["GET", "POST"])
def take_photo():
    """Take photo and convert to b_64"""
    image = project_functions.take_project_photo()
    image_b64 = utils.ndarray_to_b64(image)
    return json.dumps({"image_org_b64": image_b64})


@api_blueprint.route("/take_photo_and_predict", methods=["GET", "POST"])
def take_photo_and_predict():
    """Take picture, make, prediction and return original, heatmap, score and threshhold"""
    image_org, image_pred, score, thresh = project_functions.predict_project()
    image_org_b64 = utils.ndarray_to_b64(image_org)
    image_pred_b64 = utils.ndarray_to_b64(image_pred)
    return json.dumps({"image_org_b64": image_org_b64, "image_pred_b64": image_pred_b64, "score": score, "thresh": thresh})


@api_blueprint.route("/save_photo", methods=["GET", "POST"])
def save_photo():
    """Save the image to folder "images" """
    save_path = project_functions.save_project_photo()
    return save_path


@api_blueprint.route("/return_saved_photo", methods=["GET", "POST"])
def return_saved_photo():
    image = project_functions.return_saved_photo()
    return image


@api_blueprint.route("/update_crop", methods=["GET", "POST"])
def update_crop():
    x_1 = request.args.get('x_1', None)
    x_2 = request.args.get('x_2', None)
    y_1 = request.args.get('y_1', None)
    y_2 = request.args.get('y_2', None)
    project_functions.update_project_crop(x_1, x_2, y_1, y_2)
    return "success"


@api_blueprint.route("/update_camera", methods=["GET", "POST"])
def update_camera():
    camera = request.args.get('camera', None)
    camera_type = request.args.get('camera_type', None)
    project_functions.update_project_camera(camera, camera_type)
    return "success"


@api_blueprint.route("/init_project", methods=["GET", "POST"])
def init_project():
    new_project_name = request.args.get('new_project_name', None)
    project_functions.init_project(new_project_name)
    return "success"


@api_blueprint.route("/update_threshold", methods=["GET", "POST"])
def update_threshold():
    threshold = request.args.get('threshold', None)
    project_functions.update_project_threshold(threshold)
    return "success"


@api_blueprint.route("/change_project", methods=["GET", "POST"])
def change_project():
    project_name = request.args.get('project_name', None)
    project_functions.change_project(project_name)
    return "success"
