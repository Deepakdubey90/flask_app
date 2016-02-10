"""
Feature modules.
"""
from app import db
from utils.base import BaseModel


class Feature(BaseModel):
    """
    should create feature tables.
    """
    __tablename__ = 'feature'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(128))
    name = db.Column(db.String(128))

    def __init__(self, slug, name):
        self.slug = slug
        self.name = name
