import csv
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

# Testing the first part of the task
print(register_user("Test123"))  # The password is too simple
print(register_user("TestPassword123!"))  # The password is valid

# Decorator for password complexity check with parameters
def password_validator(
    min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1, min_special_chars: int = 1
):
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> None:
            errors = []
            if len(password) < min_length:
                errors.append(f"Пароль должен содержать минимум {min_length} символов.")
            if sum(1 for char in password if char.isupper()) < min_uppercase:
                errors.append(f"Пароль должен содержать минимум {min_uppercase} заглавных букв.")
            if sum(1 for char in password if char.islower()) < min_lowercase:
                errors.append(f"Пароль должен содержать минимум {min_lowercase} строчных букв.")
            if sum(1 for char in password if char in '!@#$%^&*()-_+=<>?/.,:;{}[]|') < min_special_chars:
                errors.append(f"Пароль должен содержать минимум {min_special_chars} специальных символов.")
            if errors:
                raise ValueError("\n".join(errors))
            return func(username, password)
        return wrapper
    return decorator

# Decorator for username validation
def username_validator(func: Callable) -> Callable:
    def wrapper(username: str, password: str) -> None:
        if " " in username:
            raise ValueError("Имя пользователя не должно содержать пробелы.")
        return func(username, password)
    return wrapper

# Decorator for registration and CSV file writing
@password_validator(min_length=10, min_uppercase=2, min_lowercase=2, min_special_chars=2)
@username_validator
def register_user_with_csv(username: str, password: str) -> None:
    """
    Функция для регистрации нового пользователя и записи данных в CSV файл.

    Параметры:
        username (str): Имя пользователя.
        password (str): Пароль пользователя.

    Raises:
        ValueError: Если пароль или юзернейм не соответствует заданным условиям.
    """
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        print("Регистрация и запись в файл прошли успешно!")