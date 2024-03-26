#!/usr/bin/python3
# views.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_bootstrap import Bootstrap
from ecosortify import mail

app = Flask(__name__)
app.config.from_object('config.Config')
mail = Mail(app)
bootstrap = Bootstrap(app)

# Example of a WTForm for registration
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

# Routes for registration, login, and logout
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process registration form submission
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login form handling
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Logout logic
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)

