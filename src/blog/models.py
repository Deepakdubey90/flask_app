"""
Blog modules.
"""
from app import db
from utils.base import BaseModel
from sqlalchemy.orm import relationship, backref


class Blog(BaseModel):
    """
    should create blog tables.
    """
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(256))
    url = db.Column(db.String(128))

    def __init__(self, account_number, url):
        self.account_number = account_number
        self.url = url


class UserBlog(BaseModel):
    """
    should create user blog table.
    """
    __tablename__ = 'user_blog'

    id = db.Column(db.Integer, db.Sequence('user_blog_seq'), primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, blog_id, user_id):
        self.blog_id = blog_id
        self.user_id = user_id
