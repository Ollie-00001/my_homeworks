from peewee import *
from datetime import datetime

DB = SqliteDatabase('barbershop_peewee.db')

class BaseModel ():
    class Meta:
        database = DB

