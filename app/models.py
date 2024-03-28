#!/usr/bin/python3
""" Creates database models for the app """
from flask import current_app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
import jwt


class User(db.Model):
    """ Users database table """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('Password is not a readable string!')

    @password.setter
    def password(self):
        self.password_hash = generate_password_hash(password)

    def verify_password(self):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=600):
        """ Generation of a confirmation token """
        token = jwt.encode(
            {
                "confirm": self.id,
                "exp": datetime.utcnow()
                + datetime.timedelta(seconds=expiration)
            },
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )
        return token

        def confirm(self, token):
            """ Confirm token """
            try:
                data = jwt.decode(
                    token,
                    current_app.config['SECRET_KEY'],
                    algorithms=["HS256"]
                )
            except jwt.ExpiredSignatureError:
                print("The token has expired.")
                return False
            except jwt.InvalidTokenError:
                print("The token is invalid")
                return False
            if data.get('confirm') != self.id:
                return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True


class Post(db.Model):
    """ Posts database table """
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(64))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    comments = db.relationship('Comment', backref='post', lazy='dynamic')


class Comment(db.Model):
    """ Comments database table """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    content = db.Column(db.Text)
