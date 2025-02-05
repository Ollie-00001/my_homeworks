
def password_checker(func):
    def wrapper(*args, **kwargs):
        password = input("Enter the password: ")
        if password == '12345':
            return func(*args, **kwargs)
        else:
                print("Incorrect password. Access denied.")
        return wrapper

