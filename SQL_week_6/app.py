from flask import Flask
from peewee import *

# DB and Models
DB = SqliteDatabase('barbershop_peewee.db')

class BaseModel(Model):
    class Meta:
        database = DB

class Master(BaseModel):
    first_name = CharField(max_length = 50, null=False)
    last_name = CharField(max_length=50, null=False)
    middle_name = CharField(max_length=50, null=True)
    phone = CharField(max_length=16, unique=True)



# Flask Application
app = Flask(__name__)

@app.before_request
def db_connect():
    DB.connect()

@app.teardown_request
def db_close():
    DB.close()

@app.route("/")
def main():
    pass