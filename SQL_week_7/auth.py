"""
Модуль авторизации пользователей
Имитирует базу данных пользователей с API ключами и ролями.
"""

USERS = [
    {
        "username": "admin",
        "api_key": "admin_secret_key_123",
        "role": "admin"
    },
    {
        "username": "user",
        "api_key": "user_readonly_key_456",
        "role": "user"
    }
]

def is_valid_api_key(api_key):
    """
    Проверяет, является ли ключ API действительным
    """
    return any(user["api_key"] == api_key for user in USERS)

def is_admin(api_key):
    """
    Проверяет, имеет ли пользователь с данным ключом API права администратора
    """
    return any(user["api_key"] == api_key and user["role"] == "admin" for user in USERS)
