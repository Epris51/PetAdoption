from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class AddPetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('porcupine', 'Porcupine'), ('cat', 'Cat'), ('dog', 'Dog')],
                          validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField("Age", choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')],
                      validators=[InputRequired()])
    notes = SelectField("Notes", choices=[
        ('', 'Select an option'),
        ('Needs regular exercise', 'Needs regular exercise'),
        ('Requires special diet', 'Requires special diet'),
        ('Needs socialization training', 'Needs socialization training'),
        ('Requires grooming', 'Requires grooming'),
        ('Needs a calm environment', 'Needs a calm environment'),
        ('Requires supervision with children', 'Requires supervision with children'),
    ], validators=[Optional()], render_kw={'class': 'form-select'})


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")
