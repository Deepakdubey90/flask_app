from marshmallow import Schema, fields, pprint
from models import User


class UserSchema(Schema):
    """
    user schema for serialization & deserialization.
    """
    id = fields.Integer()
    username = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    password = fields.Str()

    class Meta:
        fields = ("id", "username", "first_name", "last_name", "email",
                  "create_on", "updated_on")
        #exclude = ('password',)


user_schema = UserSchema()

def user_deserializer(data):
    return user_schema.load(data).data

def user_after_get_many(result=None, search_params=None, **kw):
    #import pdb;pdb.set_trace();
    result['objects'] = [user_deserializer(obj) for obj in result['objects']]
