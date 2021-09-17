from marshmallow import Schema, fields, EXCLUDE


class VietnamnetCommentSchema(Schema):
    user_id = fields.String(data_key='UserId', allow_none=True)
    full_name = fields.String(data_key='SenderFullName')

    class Meta:
        unknown = EXCLUDE
