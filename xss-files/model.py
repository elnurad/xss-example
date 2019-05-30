import os

from peewee import Model, CharField, IntegerField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class Message(Model):
    content = CharField(max_length=1024, unique=True)

    class Meta:
        database = db
