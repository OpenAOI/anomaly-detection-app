from flask import (
    Blueprint,
    redirect,
    json,
    render_template,
    request,
    url_for,
    Response,
    session,
)
from pcb_anodet_server import project_functions
from pcb_anodet_server.config import ip_address
from typing import Union
from pcb_anodet_server.views import api_blueprint, forms


@api_blueprint.route("/delete_project", methods=["GET", "POST"])
def delete_project() -> None:
    """Delete project"""
    project_name = session["project_name"]
    project_functions.delete_project(project_name)


def set_project(project_name: str) -> None:
    """Save project-name to session cookie"""
    session["project_name"] = project_name


@api_blueprint.route("/set_project_route", methods=["GET", "POST"])
def set_project_route() -> None:
    """Save project-route to session cookie"""
    project_name = request.args.get("project_name", None)

    session["project_name"] = project_name
    return "Success"


def get_project() -> str:
    """Get the project-name in session cookie"""

    return session["project_name"]


@api_blueprint.route("/", methods=["GET", "POST"])
@api_blueprint.route("/select_project", methods=["GET", "POST"])
def select_project_view() -> Union[Response, str]:
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
        "select_project.html", form=form, projects=projects, ip_address=ip_address
    )


@api_blueprint.route("/predict", methods=["GET", "POST"])
def predict_view() -> str:
    project_name = get_project()

    return render_template(
        "predict.html", project_name=project_name, ip_address=ip_address
    )


@api_blueprint.route("/edit/crop_camera", methods=["GET", "POST"])
def crop_camera_view() -> str:
    project_name = get_project()

    return render_template(
        "edit/crop_camera.html", project_name=project_name, ip_address=ip_address
    )


@api_blueprint.route("/edit/take_photo", methods=["GET", "POST"])
def take_photo_view() -> str:
    project_name = get_project()

    return render_template(
        "edit/take_photo.html", project_name=project_name, ip_address=ip_address
    )


@api_blueprint.route("/edit/view_images", methods=["GET", "POST"])
def view_images_view() -> str:
    project_name = get_project()
    # Load images
    images = project_functions.get_all_project_images(project_name)
    total_images = len(images["images"])

    return render_template(
        "edit/view_images.html",
        project_name=project_name,
        images=images,
        total_images=total_images,
        ip_address=ip_address,
    )


@api_blueprint.route("/edit/train_project", methods=["GET", "POST"])
def train_project_view() -> str:
    project_name = get_project()
    return render_template(
        "edit/train_project.html", project_name=project_name, ip_address=ip_address
    )


""" Error pages """


@api_blueprint.app_errorhandler(404)
def error_404(error: Response) -> str:
    return render_template("errors/404.html"), 404
