from flask_wtf import FlaskForm
from wtforms import BooleanField, RadioField, SubmitField
from wtforms.validators import DataRequired


class DiagnoseForm(FlaskForm):
    gender = RadioField('Label',
                        choices=[(True, 'Male'), (False, 'Female')],
                        validators=[DataRequired()])
    polyuria = BooleanField('Polyuria')
    polydipsia = BooleanField('Polydipsia')
    sudden_wl = BooleanField('Sudden Weight Loss')
    obesity = BooleanField('Obesity')
    submit = SubmitField('Get result')
