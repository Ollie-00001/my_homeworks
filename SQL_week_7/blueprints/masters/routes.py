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
from models import Master
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
        } for master in masters
    ]

    return jsonify(masters_list), 200

@masters_bp.route('/<id>', methods=['GET'])
def get_master_by_id(id):
    api_key = request.headers.get('X-API-KEY')
    if not is_valid_api_key(api_key):
        return jsonify({'error': 'Invalid API key'}), 401

    try:
        master = Master.get_by_id(id)
        return jsonify({
            'id': master.id,
            'first_name': master.name,
            'last_name': master.last_name,
            'middle_name': master.middle_name,
            'phone': master.phone,
        }), 200
    except DoesNotExist:
        return jsonify({'error': 'Master not found'}), 404


@masters_bp.route('/', methods=['POST'])
def create_master():
    """
    Контроллер, обрабатывающий POST-запрос по маршруту /masters
    Принимает данные о новом мастере в формате JSON:
    {
        "name": "Имя",
        "last_name": "Фамилия",
        "middle_name": "Отчество",
        "phone": "Номер телефона"
    }

    Записиси могут создавать только администраторы
    :return: JSON-ответ с созданным мастером

    :exception: IntegrityError, если мастер  с таким номером телефона уже существует
    """
    api_key = request.headers.get('X-API-KEY')
    if not is_valid_api_key(api_key) or not is_admin(api_key):
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    try:
        master = Master.create(**data)
        return jsonify({'id': master.id}), 201
    except IntegrityError as e:
        return jsonify({'error': str(e)}), 400


@masters_bp.route('/<id>', methods=['PUT'])
def update_master(id):
    """
    Контроллер, обрабатывающий PUT-запрос по маршруту /masters/<id>
    Обновляет данные мастера с указанным ID.
    Принимает JSON с новыми данными:
    {
        "name": "Новое имя",
        "last_name": "Новая фамилия",
        "middle_name": "Новое отчество",
        "phone": "Новый номер телефона"
    }

    Доступно только администраторам.

    :param id: ID мастера
    :return: JSON-ответ с обновлёнными данными или сообщение об ошибке
    :raises DoesNotExist: если мастер с таким ID не найден
    """
    api_key = request.headers.get('X-API-KEY')
    if not is_valid_api_key(api_key) or not is_admin(api_key):
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    try:
        master = Master.get_by_id(id)
        master.name = data.get('name', master.name)
        master.last_name = data.get('last_name', master.last_name)
        master.middle_name = data.get('middle_name', master.middle_name)
        master.phone = data.get('phone', master.phone)
        master.save()
        return jsonify({'message': 'Master updated'}), 200
    except DoesNotExist:
        return jsonify({'error': 'Master not found'}), 404

@masters_bp.route('/<id>', methods=['DELETE'])
def delete_master(id):
    """
    Контроллер, обрабатывающий DELETE-запрос по маршруту /masters/<id>
    Удаляет мастера с указанным ID.

    Доступно только администраторам.

    :param id: ID мастера
    :return: JSON-ответ с сообщением об успешном удалении или ошибкой
    :raises DoesNotExist: если мастер с таким ID не найден
    """
    api_key = request.headers.get('X-API-KEY')
    if not is_valid_api_key(api_key) or not is_admin(api_key):
        return jsonify({'error': 'Unauthorized'}), 403

    try:
        master = Master.get_by_id(id)
        master.delete_instance()
        return jsonify({'message': 'Master deleted'}), 200
    except DoesNotExist:
        return jsonify({'error': 'Master not found'}), 404