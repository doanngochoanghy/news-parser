from marshmallow import Schema, fields, EXCLUDE, pre_load


class VnexpressCommentSchema(Schema):
    user_id = fields.String(data_key='userid', allow_none=True)
    full_name = fields.String(data_key='full_name')

    class Meta:
        unknown = EXCLUDE

    @pre_load
    def load_comment(self, data, **kwargs):
        data['userid'] = str(data['userid'])
        return data
