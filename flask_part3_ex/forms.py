from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    name = StringField('Vardas', [DataRequired()])
    surname = StringField('Pavarde', [DataRequired()])
    message = TextAreaField('Jūsų pranešimas', [DataRequired()])
    submit = SubmitField('Submit')