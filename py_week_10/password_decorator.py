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