from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import Optional, URL, InputRequired, DataRequired, Length

class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField(
        "Pet Name",
        validators=[InputRequired(), Length(max=50)]
        )

    species = SelectField(
        "Species",
        choices=[('cat', 'Cat'),
                 ('dog', 'Dog'),
                 ('porcupine', 'Porcupine')
                 ],
        validators=[DataRequired()]
        )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
        )

    age = SelectField(
        "Age",
        choices=[('baby', 'Baby'),
                 ('young', 'Young'),
                 ('adult', 'Adult'),
                 ('senior', 'Senior'),
                 ],
        validators=[DataRequired()]
        )

    notes = StringField(
        "Notes",
        )

class EditPetForm(FlaskForm):
    """A form to edit a pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
        )

    notes = StringField(
        "Notes",
        )

    available = BooleanField(
        "Availabile",
    )