from marshmallow import Schema, fields, pprint
from models import Blog


class BlogSchema(Schema):
    """
    blog schema for serialization & deserialization.
    """
    id = fields.Integer()
    account_number = fields.Str()
    url = fields.Str()

    class Meta:
        fields = ("id", "account_number", "url", "create_on", "updated_on", "feature")
        #exclude = ('password',)


blog_schema = BlogSchema()

def blog_deserializer(data):
    return blog_schema.load(data).data

def blog_after_get_many(result=None, search_params=None, **kw):
    result['objects'] = [blog_deserializer(obj) for obj in result['objects']]
