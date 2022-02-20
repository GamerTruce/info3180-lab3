from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import DataRequired  


class ContactForm(FlaskForm):
    name= StringField('Name', [validators.Length(min=4, max=25)])

    email= StringField('Email Address', [validators.Length(min=6, max=35)])
    
    subject= StringField('Subject', [validators.Length(min=4, max=25)])

    text_area = TextAreaField('Message', validators=[DataRequired()])

