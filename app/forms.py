from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    phone = StringField('Phone #: ', validators=[DataRequired()])
    email = StringField('E-mail: ', validators=[DataRequired()])
    msg = StringField('Message: ', validators=[DataRequired()])
    submit = SubmitField('Submit')
