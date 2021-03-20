from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class weatherForm(FlaskForm):
    country = StringField(label='Country:', validators=[DataRequired()])
    city = StringField(label='City: ', validators=[DataRequired()])
    submit = SubmitField(label='Search')
