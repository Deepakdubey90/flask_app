import flask_wtf
from flask_wtf import Form
from wtforms import StringField, PasswordField
from models import db, User
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
    """
    register user form for validation
    """
    username = StringField('username', validators=[
        DataRequired(), Length(max=50)])
    firstname =StringField('firstname', validators=[DataRequired(), Length(max=30)])
    lastname = StringField('lastname', validators=[DataRequired(),  Length(max=30)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),  Length(max=70)])
    #contact = StringField('contact', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        user = User.query.filter_by(username = self.username.data.lower()).first()
        if user:
            self.username.errors.append("This User is already taken")
            return False
        else:
            return True


class SigninForm(Form):
    """
    login for login validation.
    """
    username = StringField('username', validators=[DataRequired("Enter username")])
    password = PasswordField('Password', validators=[DataRequired("Enter password")])


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(username = self.username.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.username.errors.append("Invalid username or password")
            return False
