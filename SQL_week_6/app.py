from flask import Flask
from peewee import *

app = Flask(__name__)

@app.route("/")
def main():
    pass