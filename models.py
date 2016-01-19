from app import db


class User(db.Model):
    __tablename__ = 'user'

    """
    user models to create user table.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    contact = db.Column(db.String(128))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


    def __repr__(self):
        return '<username {}>'.format(self.username)
