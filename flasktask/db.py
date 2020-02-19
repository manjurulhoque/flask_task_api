import os

from flask import jsonify
from google.cloud import ndb, datastore
from google.cloud.ndb.model import Key
from google.oauth2 import service_account
from flasktask.models import *
from flasktask.schemas import student_schema


# credentials = service_account.Credentials.from_service_account_info({})

# ancestor_key = ndb.Key("student", "work")


def create(**kwargs):
    client = ndb.Client()
    with client.context():
        student = Student(name=kwargs['name'],
                          phone=kwargs['phone'],
                          email=kwargs['email'],
                          roll=kwargs['roll'],
                          cls=kwargs['cls'],
                          address=kwargs['address'])

        key = student.put()
        print(key)
        return student


# def all_students():
#     client = ndb.Client()
#     with client.context():
#         query = Student.query()
#     return query


# def create(**kwargs):
#     student = Student(name=kwargs['name'],
#                       phone=kwargs['phone'],
#                       email=kwargs['email'],
#                       roll=kwargs['roll'],
#                       cls=kwargs['cls'],
#                       address=kwargs['address'])
#
#     key = student.put()
#     print(key)
#     return jsonify(student_schema.dump(student).data)


def all_students():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rumi/Desktop/credentials.json"
    # print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))
    datastore_client = datastore.Client()
    # ss = db.all_students()
    query = datastore_client.query(kind='Student')
    data = query.fetch()

    return data


def get_student(key):
    client = ndb.Client()
    with client.context():
        student = Student.query().filter(Student.key == ndb.Key('Student', int(key))).get()
        return student
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rumi/Desktop/credentials.json"
    # # print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))
    # datastore_client = datastore.Client()
    # query = datastore_client.query(kind='Student')
    # # return datastore_client.query(kind='Student').add_filter(Student.key, '=', int(key)).get()
    # # return query.add_filter('id', '=', key).get()
    # client = ndb.Client()
    # with client.context():
    #     student = Student.query().filter(Student.key == Key('Student', key))
    #     print(student)
    #     return student


def update(key, **kwargs):
    client = ndb.Client()
    student = get_student(key)
    with client.context():
        student.name = kwargs['name'] if 'name' in kwargs else student.name
        student.phone = kwargs['phone'] if 'phone' in kwargs else student.phone
        student.email = kwargs['email'] if 'email' in kwargs else student.email
        student.roll = kwargs['roll'] if 'roll' in kwargs else student.roll
        student.cls = kwargs['cls'] if 'cls' in kwargs else student.cls
        student.address = kwargs['address'] if 'address' in kwargs else student.address
        # student['created_at'] = kwargs['created_at'] if 'created_at' in kwargs else student.created_at
        # student['updated_at'] = kwargs['updated_at'] if 'updated_at' in kwargs else student.updated_at

        student.put()  # updating Model

        return student


def delete(key):
    student = get_student(key)
    client = ndb.Client()
    with client.context():
        student.key.delete()
        return True

# client = ndb.Client()
# with client.context():
#     # contact1 = Contact(name="John Smith",
#     #                    phone="555 617 8993",
#     #                    email="john.smith@gmail.com")
#     # contact1.put()
#     # contact2 = Contact(name="Jane Doe",
#     #                    phone="555 445 1937",
#     #                    email="jane.doe@gmail.com")
#     # contact2.put()
#     # query = Contact.query().filter(Contact.key == Key('Contact', 5634161670881280)).get()
#     # query.name = "Updated name"
#     # query.put()
#     query = Contact.query()
#     names = [c.key for c in query]
#     print(names)
