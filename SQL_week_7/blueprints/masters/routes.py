"""
| Маршрут | Метод | Администратор | Обычный пользователь |
|---------|-------|---------------|---------------------|
| `/masters` | GET | ✅ | ✅ |
| `/masters/<id>` | GET | ✅ | ✅ |
| `/masters` | POST | ✅ | ❌ |
| `/masters/<id>` | PUT | ✅ | ❌ |
| `/masters/<id>` | DELETE | ✅ | ❌ |
"""

from flask import Blueprint, request, jsonify
from models import Master, Service, Appointment, MasterService, AppointmentService
from auth import is_valid_api_key, is_admin
from peewee import DoesNotExist, IntegrityError

masters_bp = Blueprint('masters', __name__, url_prefix='/masters')

@masters_bp.route('/', methods=['GET'])
def get_masters():
    """
    Контроллер, обрабатывающий GET-запрос по маршруту /masters
    """
    api_key = request.headers.get('X-API-KEY')

    # Проверка API-ключа
    if not is_valid_api_key(api_key):
        return jsonify({'error': 'Invalid API key'}), 401
    
    masters = Master.select()

    masters_list = [
        {
            'id': master.id,
            'first_name': master.name,
            'last_name': master.last_name,
            'middle_name': master.middle_name,
            'phone': master.phone,
        } 
        for master in masters
    ]

    return jsonify(masters_list), 200

@masters_bp.route('/masters/<id>', methods=['GET'])
def get_master_by_id(id):
    pass

@masters_bp.route('/masters', methods=['POST'])
def create_master():
    pass