"""
Feature modules.
"""
from app import db
from utils.base import BaseModel
from sqlalchemy.orm import relationship, backref


class Feature(BaseModel):
    """
    should create feature tables.
    """
    __tablename__ = 'feature'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(128))
    name = db.Column(db.String(128))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    blog = relationship('Blog', backref=backref('feature', lazy='dynamic'))


    def __init__(self, slug, name, blog_id):
        self.slug = slug
        self.name = name
        self.blog_id = blog_id
