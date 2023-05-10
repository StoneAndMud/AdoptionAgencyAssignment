from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, URL, Length


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()],)
    species = SelectField("Pet Species", choices=[
                          ('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],)
    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(message="Not a Valid URL")],)
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(
        min=0, max=30, message="Not within Age Range")],)
    notes = TextAreaField("Pet Notes", validators=[
                          Optional(), Length(min=10)],)
    available = BooleanField("Pet Availability")


class EditPetForm(FlaskForm):
    """Form to edit Pet"""

    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(message="Not a Valid URL")],)
    notes = TextAreaField("Pet Notes", validators=[
                          Optional(), Length(min=10)],)
    available = BooleanField("Pet Availability")
