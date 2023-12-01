from peewee import *
from app import Capital
from app import db
import json

db.connect()
db.drop_tables([Capital])
db.create_tables([Capital])

file = open('capitals.json')
data = json.load(file)

Capital.insert_many(data).execute()
