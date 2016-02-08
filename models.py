from app import db
from werkzeug import generate_password_hash, check_password_hash


class User(db.Model):
    """
    user models to create user table.
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    contact = db.Column(db.String(128))

    def __init__(self,
                 username, password, firstname, lastname, email):
        self.username = username
        self.set_password(password)
        self.first_name = firstname
        self.last_name = lastname
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<username {}>'.format(self.username)
