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

class Service(BaseModel):
    title: str = CharField(max_length=100, unique=True)
    description: str = TextField(null=True)
    price: DecimalField = DecimalField(max_digits=7, decimal_places=2)

class Appointment(BaseModel):
    client_name: str = CharField(max_length=100, null=False)
    client_phone: str = CharField(max_length=20, null=False)
    date: datetime = DateTimeField(default=datetime.now)
    master = ForeignKeyField(Master, backref='appointments')
    status: str = CharField(max_length=20, default='pending')

class MasterService(BaseModel):
    master = ForeignKeyField(Master)
    service = ForeignKeyField(Service)

def main():
    DB.connect()
    DB.create_tables([Master, Service, Appointment, MasterService, AppointmentService])

    AppointmentService.delete().execute()
    MasterService.delete().execute()
    Appointment.delete().execute()
    Service.delete().execute()
    Master.delete().execute()

    masters = Master.insert_many([
        {"first_name": "Иван", "last_name": "Иванов", "middle_name": "Сергеевич", "phone": "1234567890"},
        {"first_name": "Анна", "last_name": "Петрова", "middle_name": "Викторовна", "phone": "2345678901"},
        {"first_name": "Максим", "last_name": "Сидоров", "middle_name": None, "phone": "3456789012"},
    ]).execute()

