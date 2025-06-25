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

# Создание блюпринта с префиксом /masters
masters_bp = Blueprint('masters', __name__, url_prefix='/masters')

# Перенесите сюда соответствующие маршруты
@masters_bp.route('/', methods=['GET'])
def get_masters():
    # логика получения списка мастеров
    pass