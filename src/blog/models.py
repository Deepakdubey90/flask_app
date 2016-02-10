"""
Blog modules.
"""
from app import db
from utils.base import BaseModel


class Blog(BaseModel):
    """
    should create blog tables.
    """
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(256))
    url = db.Column(db.String(128))
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
    feature_id = db.Column(db.Integer, db.ForeignKey('feature.id'))

    def __init__(self, account_number, url, user_id, feature_id):
        self.account_number = account_number
        self.url = url
        self.user_id = user_id
        self.feature = feature_id
