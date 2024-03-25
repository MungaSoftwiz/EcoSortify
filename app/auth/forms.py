#!/usr/bin/python3
""" Contains authentication forms """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Length, DataRequired, Email, Regexp
from .. import User


class LoginForm(FlaskForm):
    """ Login form """
    email = StringField('Email', validators=[DataRequired(), Lemgth(1, 64),
                        Email()])
    keep_logged_in = Boolean Field('Keep me logged in')
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    """ Registration form """
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                        Email()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(1, 64),
                                                   Regexp('^[A-Za-z]'
                                                   '[A-Za-z0-9_.]*$'), 0],
                           'username must have only letters, numbers, '
                           'underscore or dots')
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password_2', message='Passwords must match.')
    ])
    password_2 = PasswordField('Confirm password', DataRequired())
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email.field.data.lower()).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken.')
