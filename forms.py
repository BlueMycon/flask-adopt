from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField
from wtforms.validators import Optional, URL, InputRequired

class AddPetForm(FlaskForm):
    """Forms for adopt app."""
    name = StringField(
        "Pet Name",
        validators=[InputRequired()])
    species = SelectField(
        "Species",
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()])
    age = SelectField(
        "Age",
        choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')])
    notes = StringField("Notes")
