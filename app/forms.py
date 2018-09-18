from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    Hometown = StringField('Hometown', validators=[DataRequired()])
    Description = StringField('Description', validators=[DataRequired()])

    submit = SubmitField('Sign In')