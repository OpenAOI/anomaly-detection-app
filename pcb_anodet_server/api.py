from flask import Blueprint, json, render_template, request, url_for, Response, session
import project_functions
import utils


api_blueprint = Blueprint("api_blueprint", __name__)


def set_project(project_name):
    """Save project-name to session cookie"""
    session["project_name"] = project_name


def clear_session():
    """Clear the project-name in session cookie"""
    session.clear()


@api_blueprint.route("/ping", methods=["GET", "POST"])
def ping():
    """Ping to check connection to server"""
    return "pong"


@api_blueprint.route("/latest_photo", methods=["GET", "POST"])
def latest_photo():
    """Return latest photo"""
    return Response(
        project_functions.return_latest_photo(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


@api_blueprint.route("/video_feed", methods=["GET", "POST"])
def video_feed():
    """Use the camera class to generate images into a stream"""
    project_name = session["project_name"]
    return Response(
        project_functions.gen(project_name),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


@api_blueprint.route("/take_photo_and_predict", methods=["GET", "POST"])
def take_photo_and_predict():
    """Take picture, make, prediction and return original,
    heatmap, score and threshhold"""
    project_name = request.args.get("project_name", None)
    image_pred_b64, score, thresh = project_functions.predict_project_photo(
        project_name
    )
    return json.dumps(
        {"image_pred_b64": image_pred_b64, "score": score, "thresh": thresh}
    )


@api_blueprint.route("/save_photo", methods=["GET", "POST"])
def save_photo():
    """Save the image to folder 'images'"""
    project_name = request.args.get("project_name", None)
    save_path = project_functions.save_project_photo(project_name)
    return save_path


@api_blueprint.route("/return_saved_photo", methods=["GET", "POST"])
def return_saved_photo():
    """Retrieves an image from"""
    project_name = request.args.get("project_name", None)
    project_functions.save_project_photo(project_name)  # TODO Put in frontend
    image = project_functions.return_saved_project_photo(project_name)
    return image


@api_blueprint.route("/update_crop", methods=["GET", "POST"])
def update_crop():
    project_name = request.args.get("project_name", None)
    x_1 = request.args.get("x_1", None)
    x_2 = request.args.get("x_2", None)
    y_1 = request.args.get("y_1", None)
    y_2 = request.args.get("y_2", None)
    project_functions.update_project_crop(project_name, x_1, x_2, y_1, y_2)
    return "success"


@api_blueprint.route("/update_camera", methods=["GET", "POST"])
def update_camera():
    project_name = request.args.get("project_name", None)
    camera = request.args.get("camera", None)
    camera_type = request.args.get("camera_type", None)
    project_functions.update_project_camera(project_name, camera, camera_type)
    return "success"


@api_blueprint.route("/init_project", methods=["GET", "POST"])
def init_project():
    new_project_name = request.args.get("new_project_name", None)
    set_project(new_project_name)
    print(session.get("project_name"))
    project_functions.init_project(new_project_name)
    return "success"


@api_blueprint.route("/update_threshold", methods=["GET", "POST"])
def update_threshold():
    project_name = request.args.get("project_name", None)
    threshold = request.args.get("threshold", None)
    project_functions.update_project_threshold(project_name, threshold)
    return "success"


@api_blueprint.route("/change_project", methods=["GET", "POST"])
def change_project():
    project_name = request.args.get("project_name", None)
    project_functions.change_project(project_name)
    return "success"


@api_blueprint.route("/train", methods=["GET", "POST"])
def train():
    """Train model on collected images"""
    project_name = request.args.get("project_name", None)
    project_functions.train(project_name)
    return "success"


@api_blueprint.route("/get_projects", methods=["GET", "POST"])
def get_projects():
    """Get all the project names"""
    projects = project_functions.get_all_projects()
    return projects


"""HTML routes"""


@api_blueprint.route("/", methods=["GET", "POST"])
@api_blueprint.route("/select_project", methods=["GET", "POST"])
def select_projectv():
    session.clear()
    return render_template("select_project.html")


@api_blueprint.route("/predict", methods=["GET", "POST"])
def predictv():
    # project_name = request.args.get('project', None)
    # project_functions.change_project(project_name)
    return render_template("predict.html")


@api_blueprint.route("/edit/crop_camera", methods=["GET", "POST"])
def crop_camerav():
    return render_template("edit/crop_camera.html")


@api_blueprint.route("/edit/take_photo", methods=["GET", "POST"])
def take_photov():
    return render_template("edit/take_photo.html")


@api_blueprint.route("/edit/view_images", methods=["GET", "POST"])
def view_imagesv():
    project_name = session["project_name"]
    # Load images
    images = project_functions.get_all_project_images(project_name)

    return render_template("edit/view_images.html", images=images)


@api_blueprint.route("/edit/train_project", methods=["GET", "POST"])
def train_projectv():
    return render_template("edit/train_project.html")





""" Error pages """


@api_blueprint.errorhandler(404)
def error_404v(error):
    return render_template("errors/404.html"), 404
