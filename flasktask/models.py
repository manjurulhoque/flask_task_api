from google.cloud import ndb


class Contact(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()


class Student(ndb.Model):
    name = ndb.StringProperty(required=True)
    phone = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    roll = ndb.IntegerProperty(required=True)
    cls = ndb.StringProperty(required=True)
    address = ndb.StringProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)
