from app import db


class BaseModel(db.Model):
    """
    basemodels to create common fields
    """
    __abstract__ = True

    create_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    deleted_on = db.Column(db.DateTime, server_default=None)
