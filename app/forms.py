from wtforms import *
from flask_wtf import *


class ContactForm(FlaskForm):

    name = StringField('Name', [validators.Length(min = 5, max = 22), validators.DataRequired()])
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    subject = StringField('Subject', [validators.Length(min = 1, max = 20), validators.DataRequired()])
    message = TextAreaField('Message', [validators.Length(max = 255), validators.DataRequired()], render_kw={'rows': 5, 'cols':60})
    csrf_token = csrf.CSRFProtect()
    submit = SubmitField('Send')