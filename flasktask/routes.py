from flask_cors import cross_origin

from flasktask import app, db
from flask import jsonify, request
from google.oauth2 import service_account

from flasktask.schemas import *

# credentials = service_account.Credentials.from_service_account_file("/home/rumi/Desktop/credentials.json")


@app.route("/", methods=['GET'])
@app.route("/students", methods=['GET'])
@app.route("/home", methods=['GET'])
def index():
    students = db.all_students()
    return jsonify(students_schema.dump(students))


# Create Student
@app.route('/', methods=['POST'])
@app.route('/students', methods=['POST'])
@cross_origin()
def create_student():
    print(request.get_json())
    data = {
        'name': request.get_json()['name'],
        'phone': request.get_json()['phone'],
        'email': request.get_json()['email'],
        'roll': int(request.get_json()['roll']),
        'cls': request.get_json()['cls'],
        'address': request.get_json()['address'],
    }
    student = db.create(**data)
    return student_schema.jsonify(student)


# Get Single Student
@app.route('/<key>', methods=['GET'])
@app.route('/student/<key>', methods=['GET'])
def get_student(key):
    student = db.get_student(key)
    return jsonify({'id': key, 'student': student_schema.dump(student)})


# Update Single Student
@app.route('/<key>', methods=['PUT'])
@app.route('/students/<key>', methods=['PUT'])
def update_student(key):
    data = {
        'name': request.get_json()['name'],
        'phone': request.get_json()['phone'],
        'email': request.get_json()['email'],
        'roll': int(request.get_json()['roll']),
        'cls': request.get_json()['cls'],
        'address': request.get_json()['address'],
    }
    # data = {
    #     'name': request.form['name'],
    #     'phone': request.form['phone'],
    #     'email': request.form['email'],
    #     'roll': int(request.form['roll']),
    #     'cls': request.form['cls'],
    #     'address': request.form['address'],
    # }
    student = db.update(key, **data)
    return jsonify({'id': key, 'student': student_schema.dump(student)})
    # return student_schema.jsonify(student)


# Update Single Student
@app.route('/<key>', methods=['DELETE'])
@app.route('/students/<key>', methods=['DELETE'])
def delete_student(key):
    db.delete(key)
    return jsonify({'id': key, 'status': True})
    # return student_schema.jsonify(student)
