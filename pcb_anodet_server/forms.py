from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


def validate_project_name(form, field):
    # TODO: Check if project name exist
    # raise ValidationError('Project name already exists')
    pass


class ProjectForm(FlaskForm):
    project_name = StringField(
        "project_name",
        validators=[InputRequired(), Length(min=1, max=55), validate_project_name],
    )
    submit = SubmitField("Create project")
