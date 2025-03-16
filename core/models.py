# from django.db import models
from mongoengine import Document, IntField, StringField

# Create your models here.


class User(Document):
    name = StringField(required=True)
    age = IntField()
