from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewArtistForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    Hometown = StringField('Hometown', validators=[DataRequired()])
    Description = StringField('Description', validators=[DataRequired()])


    submit = SubmitField('Sign In')