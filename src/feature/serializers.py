from marshmallow import Schema, fields, pprint
from models import Feature


class FeatureSchema(Schema):
    """
    feature schema for serialization & deserialization.
    """
    id = fields.Integer()
    slug = fields.Str()
    name = fields.Str()
    blog_id = fields.Integer()

    class Meta:
        fields = ("id", "slug", "name", "blog_id", "created_on", "updated_on")
        exclude = ('blog',)

feature_schema = FeatureSchema()
def feature_deserializer(data):
    return feature_schema.load(data).data

def feature_after_get_many(result=None, search_params=None, **kw):
    result['objects'] = [feature_deserializer(obj) for obj in result['objects']]
