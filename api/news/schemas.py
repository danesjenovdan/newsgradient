from marshmallow import Schema
from marshmallow import fields
from marshmallow import validate
from marshmallow import exceptions

from constants import Orientations
from constants import TimeRange


class MediumSchema(Schema):
    title = fields.String(dump_only=True)
    uri = fields.String(dump_only=True)
    slant = fields.String(dump_only=True)
    favicon = fields.String(dump_only=True)


class ArticleSchema(Schema):
    uri = fields.String(dump_only=True, data_key='id')
    url = fields.String(dump_only=True)
    title = fields.String(dump_only=True)
    content = fields.String(dump_only=True)
    social_score = fields.Integer(dump_only=True)
    image = fields.String(dump_only=True)
    datetime = fields.DateTime(dump_only=True)
    medium = fields.Nested(MediumSchema)


class EventArticlesSchema(Schema):
    articles = fields.Nested(ArticleSchema, many=True)
    title = fields.String(dump_only=True)
    description = fields.String(dump_only=True)
    og_image = fields.String(dump_only=True)
    social_score = fields.Integer(dump_only=True)


class EventSchema(Schema):
    uri = fields.String(dump_only=True, data_key='id')
    title = fields.String(dump_only=True)
    image = fields.String(dump_only=True)
    date = fields.DateTime(dump_only=True)
    first_publish = fields.String(dump_only=True, data_key='firstPublish')
    articles = fields.Nested(ArticleSchema, many=True)
    articles_count = fields.Int(dump_only=True, data_key='articleCount')
    all_articles_count = fields.Int(dump_only=True, data_key='allArticlesCount')
    social_score = fields.Integer(dump_only=True)

class DelimitedListField(fields.List):
    def _deserialize(self, value, attr, data, **kwargs):
        try:
            values = value.split(",")
            return [i for i in values if i]
        except AttributeError:
            raise exceptions.ValidationError(
                f"{attr} is not a delimited list it has a non string value {value}."
            )

class TopEventQPSchema(Schema):
    # timerange = fields.String(default=TimeRange.LAST_MONTH,
    #                           load_only=True,
    #                           required=False,
    #                           validate=validate.OneOf([t.value for t in TimeRange]))
    slant = fields.Int(default=Orientations.NEUTRAL,
                       load_only=True,
                       required=False,
                       validate=validate.OneOf([t.value for t in Orientations]))

class FilteredQPSchema(Schema):
    positive = DelimitedListField(fields.Int(
        required=False,
    ), required=False)
    negative = DelimitedListField(fields.Int(
        required=False,
    ), required=False)
    slightly_positive = DelimitedListField(fields.Int(
        required=False,
    ), required=False)
    slightly_negative = DelimitedListField(fields.Int(
        required=False,
    ), required=False)
    neutral = DelimitedListField(fields.Int(
        required=False,
    ), required=False)
    locations = DelimitedListField(fields.String(
        required=False,
    ), required=False)
