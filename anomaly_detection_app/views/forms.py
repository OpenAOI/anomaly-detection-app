from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from anomaly_detection_app.project_functions import get_all_projects
from typing import Any


def validate_project_name(form: Any, field: Any) -> None:
    projects_object = get_all_projects()
    project = [i["name"] for i in projects_object["projects"]]
    if field.data in project:
        raise ValidationError("Project name already exists")


def validate_characters(form: Any, field: Any) -> None:
    for char in field.data:
        if (
            char
            not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.,"
        ):
            raise ValidationError("Only characters a-z, A-Z, 0-9 and .,_- is allowed.")


class ProjectForm(FlaskForm):
    project_name = StringField(
        "project_name",
        validators=[
            InputRequired(),
            Length(min=1, max=55),
            validate_project_name,
            validate_characters,
        ],
    )
    submit = SubmitField("Create project")
