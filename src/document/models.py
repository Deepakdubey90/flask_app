"""
document modules.
"""
from app import db
from utils.base import BaseModel


class Document(BaseModel):
    """
    should create document tables.
    """
    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(128))
    size = db.Column(db.String(128))

    def __init__(self, path, size):
        self.path = path
        self.size = size
