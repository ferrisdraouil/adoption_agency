from flask_wtf import FlaskForm
# from flask_debugtoolbar import DebugToolbarExtension== only for app.py
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length
from wtforms import StringField, IntegerField, SelectField, BooleanField


class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField(
        "Species",
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
        validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField(
        "Age", validators=[InputRequired(),
                           NumberRange(min=1, max=29)])
    notes = StringField("Notes", validators=[Optional(), Length(100)])


class EditPetForm(FlaskForm):
    """ Edit a pet form """

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")
