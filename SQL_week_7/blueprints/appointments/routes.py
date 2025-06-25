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
from models import Master

# Создание блюпринта с префиксом /masters
appointments_bp = Blueprint('appointments', __name__, url_prefix='/appointments')

# Перенесите сюда соответствующие маршруты
@appointments_bp.route('/', methods=['GET'])
def get_appointments():
    # логика получения списка мастеров
    pass