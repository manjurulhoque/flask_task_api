from flasktask import ma
from marshmallow import fields


class StudentSchema(ma.Schema):
    # id = fields.Function(lambda obj: obj.key)

    class Meta:
        fields = ('id', 'name', 'roll', 'class', 'dob', 'address', 'phone', 'email', 'created_at', 'updated_at')


# Init schema
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
