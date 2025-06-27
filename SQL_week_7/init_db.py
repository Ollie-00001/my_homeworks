# init_db.py

from models import DB, Master, Service, Appointment, AppointmentService

DB.connect()
DB.create_tables([Master, Service, Appointment, AppointmentService], safe=True)
DB.close()

print("✅ Таблицы успешно созданы!")