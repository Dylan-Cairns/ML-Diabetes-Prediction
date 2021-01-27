from flask_wtf import FlaskForm
from wtforms import BooleanField, RadioField, IntegerField, SubmitField
from wtforms.validators import InputRequired
from wtforms.widgets import html5


class FieldsRequiredForm(FlaskForm):
    """Require all fields to have content. This works around the bug that WTForms radio
    fields don't honor the `DataRequired` or `InputRequired` validators.
    """
    class Meta:
        def render_field(self, field, render_kw):
            if field.type == "_Option":
                render_kw.setdefault("required", True)
            return super().render_field(field, render_kw)


class DiagnoseForm(FieldsRequiredForm):
    age = IntegerField('Age',
                       widget=html5.NumberInput(min=1, max=140),
                       validators=[InputRequired()])
    gender = RadioField('Label',
                        choices=[(True, 'Male'),
                                 (False, 'Female')],
                        validators=[InputRequired()])
    polyuria = BooleanField('Polyuria')
    polydipsia = BooleanField('Polydipsia')
    sudden_wl = BooleanField('Sudden Weight Loss')
    genital_thrush = BooleanField('Genital Thrush')
    irritability = BooleanField('Irritability')
    delayed_healing = BooleanField('Delayed Healing')
    muscle_stiffness = BooleanField('Muscle Stiffness')
    alopecia = BooleanField('Alopecia')
    obesity = BooleanField('Obesity')
    submit = SubmitField('Get result')
