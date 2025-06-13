from flask import Flask
from peewee import *

# DB and Models
DB = SqliteDatabase('barbershop_peewee.db')


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