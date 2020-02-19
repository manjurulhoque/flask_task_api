from google.cloud import ndb
from google.cloud.ndb import Key
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_info({})


class Student(ndb.Model):
    name = ndb.StringProperty(required=True)
    phone = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    roll = ndb.IntegerProperty(required=True)
    cls = ndb.StringProperty(required=True)
    address = ndb.StringProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)


class Contact(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()


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

        student.put()
        return True


@ndb.transactional(retries=2)
def all_students():
    client = ndb.Client()
    with client.context():
        query = Student.query()
    return query


def get_student(key):
    return Student.query().filter(Student.key == int(key)).get()


def update(key, **kwargs):
    student = get_student(key)
    student['name'] = kwargs['name'] if 'name' in kwargs else student.name
    student['phone'] = kwargs['phone'] if 'phone' in kwargs else student.phone
    student['email'] = kwargs['email'] if 'email' in kwargs else student.email
    student['roll'] = kwargs['roll'] if 'roll' in kwargs else student.roll
    student['cls'] = kwargs['cls'] if 'cls' in kwargs else student.cls
    student['address'] = kwargs['address'] if 'address' in kwargs else student.address
    student['created_at'] = kwargs['created_at'] if 'created_at' in kwargs else student.created_at
    student['updated_at'] = kwargs['updated_at'] if 'updated_at' in kwargs else student.updated_at

    student.put()  # updating Model

    return student


def delete(key):
    student = get_student(key)
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
