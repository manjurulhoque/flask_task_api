from flasktask import app, ma, db
from flask import jsonify, request
from google.cloud import ndb

from flasktask.demo import students


class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'roll', 'class', 'dob', 'address', 'phone', 'email', 'created_at', 'updated_at')


# Init schema
student_schema = StudentSchema()


@app.route("/", methods=['GET'])
@app.route("/students", methods=['GET'])
@app.route("/home", methods=['GET'])
def index():
    ss = db.all_students()
    students = [s for s in ss]
    # return map(lambda s: {"house_name": s.name, "cover_url": s.cover_url,
    #                       "category": s.category, "view": s.view,
    #                       "num_of_subed": s.num_of_subed},
    #            house_list)
    return jsonify(students)


# Get Single Student
@app.route('/students', methods=['POST'])
def create_product():
    data = {
        'name': "John",
        'phone': "23232323",
        'email': "john@gmail.com",
        'roll': 12121,
        'cls': "Ten",
        'address': "Dhaka",
    }
    is_created = db.create(**data)
    return student_schema.jsonify(is_created)


# Get Single Student
@app.route('/student/<key>', methods=['GET'])
def get_product(key):
    student = students[0]
    return student_schema.jsonify(student)
