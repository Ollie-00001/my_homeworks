from flask import Flask, jsonify, request
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
    description = TextField(null=True)
    price = DecimalField(max_digits=5, decimal_places=2)

class Appointment(BaseModel):
    client_name = CharField(max_length=50)
    client_phone = CharField(max_length=16)
    datetime = DateTimeField(default=datetime.now)
    master = ForeignKeyField(Master, backref='appointments')
    status = CharField(max_length=20, default='pending')

class AppointmentService(BaseModel):
    appointment = ForeignKeyField(Appointment, backref='appointment_services')
    service = ForeignKeyField(Service, backref='service_appointments')

# Flask Application
app = Flask(__name__)

@app.before_request
def _db_connect():
    DB.connect(reuse_if_open=True)

@app.teardown_request
def _db_close(exc):
    if not DB.is_closed():
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

@app.route('/masters/<int:master_id>', methods=['GET'])
def get_master(master_id):
    try:
        master = Master.get_by_id(master_id)
        return jsonify({
            'id': master.id,
            'first_name': master.first_name,
            'last_name': master.last_name,
            'middle_name': master.middle_name,
            'phone': master.phone
        }), 200
    except Master.DoesNotExist:
        return jsonify({'error': 'Master not found'}), 404

@app.route('/masters', methods=['POST'])
def create_master():
    data = request.get_json()
    try:
        master = Master.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            middle_name=data.get('middle_name'),
            phone=data['phone']
        )
        return jsonify({'message': 'Master created', 'id': master.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/masters/<int:master_id>', methods=['PUT'])
def update_master(master_id):
    data = request.get_json()
    try:
        master = Master.get_by_id(master_id)
        master.first_name = data.get('first_name', master.first_name)
        master.last_name = data.get('last_name', master.last_name)
        master.middle_name = data.get('middle_name', master.middle_name)
        master.phone = data.get('phone', master.phone)
        master.save()
        return jsonify({'message': 'Master updated'}), 200
    except Master.DoesNotExist:
        return jsonify({'error': 'Master not found'}), 404
    
@app.route('/masters/<int:master_id>', methods=['DELETE'])
def delete_master(master_id):
    try:
        master = Master.get_by_id(master_id)
        master.delete_instance()
        return '', 204
    except Master.DoesNotExist:
        return jsonify({'error': 'Master not found'}), 404

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
            'date': a.datetime.strftime('%Y-%m-%d %H:%M'),
            'status': a.status,
            'services': services
        })
    return jsonify(appointments)

@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    try:
        a = Appointment.get_by_id(appointment_id)
        services = [asoc.service.title for asoc in a.appointment_services]
        return jsonify({
            'id': a.id,
            'client_name': a.client_name,
            'client_phone': a.client_phone,
            'master': f'{a.master.first_name} {a.master.last_name}',
            'date': a.datetime.strftime('%Y-%m-%d %H:%M'),
            'status': a.status,
            'services': services
        }), 200
    except Appointment.DoesNotExist:
        return jsonify({'error': 'Appointment not found'}), 404

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    try:
        appointment = Appointment.create(
            client_name=data['client_name'],
            client_phone=data['client_phone'],
            master=Master.get_by_id(data['master_id']),
            datetime=datetime.strptime(data.get('date', datetime.now().isoformat()), "%Y-%m-%dT%H:%M:%S"),
            status=data.get('status', 'pending')
        )
        for service_id in data['service_ids']:
            AppointmentService.create(appointment=appointment, service=Service.get_by_id(service_id))
        return jsonify({'message': 'Appointment created', 'id': appointment.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run
if __name__ == '__main__':
    DB.connect()
    DB.create_tables([Master, Service, Appointment, AppointmentService], safe=True)

    app.run(debug=True)