from peewee import *

db = PostgresqlDatabase('capitalsapi', user='stuartshapiro',
                        password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Capital(BaseModel):
    name = CharField()
    capital = CharField()

db.connect()