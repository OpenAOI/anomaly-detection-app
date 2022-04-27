from flask import (
    json,
    request,
    Response,
    session,
)
from anomaly_detection_app import project_functions
from anomaly_detection_app.project_routes import api_blueprint


@api_blueprint.route("/ping", methods=["GET", "POST"])
def ping() -> str:
    """Ping to check connection to server"""
    return "pong"


@api_blueprint.route("/latest_photo", methods=["GET", "POST"])
def latest_photo() -> Response:
    """Return latest photo"""

    return Response(
        project_functions.return_latest_photo(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


@api_blueprint.route("/video_feed", methods=["GET", "POST"])
def video_feed() -> Response:
    """Use the camera class to generate images into a stream"""
    project_name = session["project_name"]

    return Response(
        project_functions.gen(project_name),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


@api_blueprint.route("/take_photo_and_predict", methods=["GET", "POST"])
def take_photo_and_predict() -> str:
    """Take picture, make prediction and return
    heatmap, score, threshhold and classification"""

    project_name = session["project_name"]
    (
        image_pred_b64,
        score,
        thresh,
        image_class,
    ) = project_functions.predict_project_photo(project_name)
    return json.dumps(
        {
            "image_pred_b64": image_pred_b64,
            "score": score,
            "thresh": thresh,
            "image_class": image_class,
        }
    )


@api_blueprint.route("/save_photo", methods=["GET", "POST"])
def save_photo() -> str:
    """Save the image to folder 'images'"""

    project_name = request.args.get("project_name", None)
    save_path = project_functions.save_project_photo(project_name)
    return save_path


@api_blueprint.route("/update_crop", methods=["GET", "POST"])
def update_crop() -> str:
    """Update the crop-values in the config file"""

    project_name = request.args.get("project_name", None)
    x_1 = request.args.get("x_1", None)
    x_2 = request.args.get("x_2", None)
    y_1 = request.args.get("y_1", None)
    y_2 = request.args.get("y_2", None)
    project_functions.update_project_crop(
        project_name, int(x_1), int(x_2), int(y_1), int(y_2)
    )
    return "success"


@api_blueprint.route("/update_camera", methods=["GET", "POST"])
def update_camera() -> str:
    """Udate which camera to use in config-file"""

    project_name = request.args.get("project_name", None)
    camera = request.args.get("camera", None)
    camera_type = request.args.get("camera_type", None)
    project_functions.update_project_camera(project_name, camera, camera_type)
    return "success"


@api_blueprint.route("/update_threshold", methods=["GET", "POST"])
def update_threshold() -> str:
    """Update threshhold value in config-file"""
    project_name = request.args.get("project_name", None)
    thresh = request.args.get("threshold", None)
    project_functions.update_project_threshold(project_name, thresh)
    return "success"


@api_blueprint.route("/train", methods=["GET", "POST"])
def train() -> str:
    """Train model on collected images"""
    project_name = request.args.get("project_name", None)
    project_functions.train(project_name)

    return "success"


@api_blueprint.route("/delete_image", methods=["GET", "POST"])
def delete_image() -> str:
    """Delete an image from project"""

    project_name = request.args.get("project_name", None)
    image_name = request.args.get("image_name", None)
    project_functions.delete_image(project_name, image_name)

    return "success"
