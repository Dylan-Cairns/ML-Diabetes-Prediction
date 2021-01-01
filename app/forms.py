from flask_wtf import FlaskForm
from wtforms import BooleanField, RadioField, SubmitField
from wtforms.validators import InputRequired


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
    gender = RadioField('Label', choices=[(True, 'Male'), (False, 'Female')], validators=[InputRequired()])
    polyuria = BooleanField('Polyuria')
    polydipsia = BooleanField('Polydipsia')
    sudden_wl = BooleanField('Sudden Weight Loss')
    obesity = BooleanField('Obesity')
    submit = SubmitField('Get result')