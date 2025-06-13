from flask import Flask, jsonify
from peewee import *
from datetime import datetime

# DB and Models
DB = SqliteDatabase('barbershop_flask.db')

class BaseModel(Model):
    class Meta:
        database = DB

class Master(BaseModel):
    first_name = CharField(max_length = 50)
    last_name = CharField(max_length=50)
    middle_name = CharField(max_length=50, null=True)
    phone = CharField(max_length=16, unique=True)

class Service(BaseModel):
    title = CharField(max_length=50, unique=True)
    description = TextField(max_length=100, null=True)
    price = DecimalField(max_digits=5, decimal_places=2)

class Appointment(BaseModel):
    client_name = CharField(max_length=50)
    client_phone = CharField(max_length=16)
    datetime = DateTimeField(default=datetime.now)
    master = ForeignKeyField(Master, backref='appointments')
    status = CharField(max_length=20, default='pending')

class AppoinmentService(BaseModel):
    appointment = ForeignKeyField(Appointment, backref='appointment_services')
    service = ForeignKeyField(Service, backref='service_appointments')

# Flask Application
app = Flask(__name__)

@app.before_request
def db_connect():
    DB.connect()

@app.teardown_request
def db_close():
    DB.close()

# Routes
@app.route('/masters', methods=['GET'])
def get_masters():
    masters = [
        {
            'id': m.id,
            'full_name': f'{m.last_name} {m.first_name} {m.middle_name or ''}',
            'phone': m.phone
        }
        for m in Master.select()
    ]
    return jsonify(masters)

@app.route('/services', methods=['GET'])
def get_services():
    services = [
        {
            'id': s.id,
            'title': s.title,
            'description': s.description,
            'price': float(s.price)
        }
        for s in Service.select()
    ]
    return jsonify(services)

@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = []
    for a in Appointment.select():
        services = [asoc.service.title for asoc in a.appointment_services]
    appointments.append ({
            'id': a.id,
            'client_name': a.client_name,
            'client_phone': a.client_phone,
            'master': f'{a.master.first_name} {a.master.last_name}',
            'date': a.date.strftime('%Y-%m-%d %H:%M'),
            'status': a.status,
            'services': services
        })
    return jsonify(appointments)

