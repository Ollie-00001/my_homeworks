from peewee import *
from datetime import datetime

DB = SqliteDatabase('barbershop_peewee.db')

class BaseModel ():
    class Meta:
        database = DB

class Master(BaseModel):
    first_name: str = CharField(max_length=50, null=False)
    last_name: str = CharField(max_length=50, null=False)
    middle_name: str = CharField(max_length=50, null=True)
    phone: str = CharField(max_length=20, unique=True)

