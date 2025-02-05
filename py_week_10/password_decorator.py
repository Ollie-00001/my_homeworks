from typing import Callable

#Decorator for password complexity check
def password_checker(func: Callable) -> Callable:
    def wrapper(password: str) -> str:
        if len(password) < 8:
            return "Пароль должен содержать минимум 8 символов."
        if not any(char.isdigit() for char in password):
            return "Пароль должен содержать хотя бы одну цифру."
        if not any(char.isupper() for char in password):
            return "Пароль должен содержать хотя бы одну заглавную букву."
        if not any(char.islower() for char in password):
            return "Пароль должен содержать хотя бы одну строчную букву."
        if not any(char in '!@#$%^&*()-_+=<>?/.,:;{}[]|' for char in password):
            return "Пароль должен содержать хотя бы один специальный символ."
        return func(password)
    return wrapper

@password_checker
def register_user(password: str) -> str:
    return "Добро пожаловать на страницу регистрации!"