"""
| Маршрут | Метод | Администратор | Обычный пользователь |
|---------|-------|---------------|---------------------|
| `/appointments` | GET | ✅ | ✅ |
| `/appointments/<id>` | GET | ✅ | ✅ |
| `/appointments/master/<master_id>` | GET | ✅ | ✅ |
| `/appointments` | POST | ✅ | ❌ |
| `/appointments/<id>` | PUT | ✅ | ❌ |
| `/appointments/<id>` | DELETE | ✅ | ❌ |
"""

from flask import Blueprint, request, jsonify
from models import Master, Service, Appointment, MasterService, AppointmentService
from auth import is_valid_api_key, is_admin
from peewee import DoesNotExist, IntegrityError

appointments_bp = Blueprint('appointments', __name__, url_prefix='/appointments')

@appointments_bp.route('/', methods=['GET'])
def get_appointments():

    api_key = request.headers.get('X-API-KEY')

    if not is_valid_api_key(api_key):
        return jsonify({'error': 'Invalid API key'}), 401
    
    appointments = Appointment.select().join(AppointmentService).join(Service).join(Master)

    appointments_list = [
        {
            'id': appointment.id,
            'master_id': appointment.master_id,
            'client_name': appointment.client_name,
            'client_phone': appointment.client_phone,
            'comment': appointment.comment,
            'status': appointment.status,
            'master': appointment.master.name,
            'services': [service.title for service in appointment.services]
        }
        for appointment in appointments
    ]

    return jsonify(appointments_list), 200

@appointments_bp.route('/appointments/<id>', methods=['GET'])
def get_appointment_by_id(id):
    pass

@appointments_bp.route('/appointments/master/<master_id>', methods=['GET'])
def get_appointments_by_master(master_id):
    pass

@appointments_bp.route('/appointments', methods=['POST'])
def create_appointment():
    pass

@appointments_bp.route('/appointments/<id>', methods=['PUT'])
def update_appointment(id):
    """
    Контроллер, обрабатывающий PUT-запрос по маршруту /appointments/<id>
    Обновляет данные записи с указанным ID.

    Доступно только администраторам.

    Ожидаемый JSON-формат:
    {
        "master_id": 1,
        "client_name": "Новое имя",
        "client_phone": "Новый телефон",
        "comment": "Новый комментарий",
        "status": "Новый статус",
        "services": [1, 2]
    }

    :param id: ID записи
    :return: JSON-ответ с обновлённой записью или сообщением об ошибке
    :raises DoesNotExist: если запись не найдена
    """
    pass


@appointments_bp.route('/appointments/<id>', methods=['DELETE'])
def delete_appointment(id):
    """
    Контроллер, обрабатывающий DELETE-запрос по маршруту /appointments/<id>
    Удаляет запись с указанным ID.

    Доступно только администраторам.

    :param id: ID записи
    :return: JSON-ответ с подтверждением удаления или сообщением об ошибке
    :raises DoesNotExist: если запись не найдена
    """
    pass