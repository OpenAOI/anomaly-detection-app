from flask import (
    redirect,
    render_template,
    request,
    url_for,
    Response,
    session,
)
from anomaly_detection_app import project_functions
from anomaly_detection_app.config import ip_address
from anomaly_detection_app.views import api_blueprint, forms
from typing import Union


""" Session methods """


def set_project(project_name: str) -> None:
    """Save project-name to session cookie"""
    session["project_name"] = project_name


@api_blueprint.route("/set_project_route", methods=["GET", "POST"])
def set_project_route() -> None:
    """Save project-route to session cookie"""
    project_name = request.args.get("project_name", None)
    session["project_name"] = project_name


@api_blueprint.route("/delete_project", methods=["GET", "POST"])
def delete_project() -> None:
    """Delete project in session cookie"""
    project_name = session["project_name"]
    project_functions.delete_project(project_name)
    return "success"


def get_project() -> str:
    """Get the project-name in session cookie"""
    return session["project_name"]


@api_blueprint.route("/", methods=["GET", "POST"])
def index_view() -> Union[Response, str]:
    """Select or create new project page"""
    projects = project_functions.get_all_projects()
    form = forms.ProjectForm()

    if request.method == "POST" and form.validate_on_submit():
        # Set project
        project_name = form.project_name.data
        set_project(project_name)
        project_functions.init_project(project_name)
        return redirect(url_for("views_blueprint.crop_camera_view"))

    return render_template(
        "index.html", form=form, projects=projects, ip_address=ip_address
    )


@api_blueprint.route("/evaluate", methods=["GET", "POST"])
def evaluate_view() -> str:
    project_name = get_project()

    return render_template(
        "evaluate/evaluate.html", project_name=project_name, ip_address=ip_address
    )


@api_blueprint.route("/train/crop_camera", methods=["GET", "POST"])
def crop_camera_view() -> str:
    project_name = get_project()

    return render_template(
        "train/crop_camera.html", project_name=project_name, ip_address=ip_address
    )


@api_blueprint.route("/train/take_image", methods=["GET", "POST"])
def take_image_view() -> str:
    project_name = get_project()

    return render_template(
        "train/take_image.html", project_name=project_name, ip_address=ip_address
    )


@api_blueprint.route("/train/preview_images", methods=["GET", "POST"])
def preview_images_view() -> str:
    project_name = get_project()
    # Load images
    images = project_functions.get_all_project_images(project_name)
    total_images = len(images["images"])

    return render_template(
        "train/preview_images.html",
        project_name=project_name,
        images=images,
        total_images=total_images,
        ip_address=ip_address,
    )


@api_blueprint.route("/train/train_project", methods=["GET", "POST"])
def train_project_view() -> str:
    project_name = get_project()
    return render_template(
        "train/train_project.html", project_name=project_name, ip_address=ip_address
    )


""" Error pages """


@api_blueprint.app_errorhandler(404)
def error_404_view(error: Response) -> str:
    return render_template("errors/404.html"), 404
