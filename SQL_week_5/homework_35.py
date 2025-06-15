from peewee import *
from datetime import datetime

DB = SqliteDatabase('barbershop_peewee.db')

class BaseModel(Model):
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

class AppointmentService(BaseModel):
    appointment = ForeignKeyField(Appointment)
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

    services = Service.insert_many([
        {"title": "Стрижка", "description": "Мужская классическая стрижка", "price": 1000.00},
        {"title": "Бритьё", "description": "Горячее полотенце и бритьё опасной бритвой", "price": 700.00},
        {"title": "Оформление бороды", "description": "Коррекция формы бороды", "price": 500.00},
        {"title": "Мытьё головы", "description": None, "price": 300.00},
    ]).execute()

    for master in Master.select():
        for service in Service.select().limit(2):
            MasterService.create(master=master, service=service)
    
    appointments = []
    for i in range(3):
        master = Master.select()[i % 3]
        appointment = Appointment.create(
            client_name=f"Клиент {i + 1}",
            client_phone=f"89001234{i:03}",
            master=master
        )

        for service in Service.select().limit(2):
            AppointmentService.create(appointment=appointment, service=service)
        
        appointments.append(appointment)

    print("=== Мастера ===")
    for m in Master.select():
        print(f"{m.id}. {m.last_name} {m.first_name} ({m.phone})")

    print("\n=== Услуги ===")
    for s in Service.select():
        print(f"{s.id}. {s.title} — {s.price} руб.")

    print("\n=== Заявки ===")
    for a in Appointment.select():
        services_list = ", ".join(
            [asoc.service.title for asoc in AppointmentService.select().where(AppointmentService.appointment == a)]
        )
        print(f"{a.id}. {a.client_name} ({a.client_phone}) → {a.master.first_name} {a.master.last_name}, услуги: {services_list}")

    DB.close()


if __name__ == "__main__":
    main()