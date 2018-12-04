from flask_wtf import FlaskForm
from flask_debugtoolbar import DebugToolbarExtension
from wtforms.validators import InputRequired, Optional
from wtforms import StringField, IntegerField, SelectField


class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField(
        "Species",
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
        validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[InputRequired()])
    age = IntegerField("Age", validators=[InputRequired()])
    notes = StringField("Notes", validators=[Optional()])