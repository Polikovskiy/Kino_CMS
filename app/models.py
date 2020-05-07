from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    image = db.Column(db.String(500))
    description = db.Column(db.String(10000))
    type = db.Column(db.String(64))
    trailer = db.Column(db.String(500))


class Galery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(500))
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))


class CEO_Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500))
    title = db.Column(db.String(64))
    keywords = db.Column(db.String(64))
    description = db.Column(db.String(10000))
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def create(self, username, email, password):
        user = User(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
